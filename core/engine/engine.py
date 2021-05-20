import logging

from elasticsearch.client import Elasticsearch
from elasticsearch.exceptions import ConnectionError

from core.engine.components.searcher import simple_search, Searcher
from core.engine.components.extractor import Extractor
from core.engine.components.text_analyzer import TextAnalyser, process_text_stemm
from core.engine.components.extractor import result_extractor
from core.engine.components.connector import Connector

from core.engine.components.elasticsearch_adapter.connecter import connect

from core.data.fields import QUERY, P_QUERY
from .components.extractor import result_extractor
from urllib3.exceptions import NewConnectionError, ConnectionError

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Engine:
    def __init__(self, index=None):
        self.index = index
        self.es: Elasticsearch = Elasticsearch([{"host": "localhost", "port": "9200"}])

        # components of engine
        self._searcher: Searcher = Searcher(es=self.es, index=self.index)
        self._connector: Connector = Connector(es=self.es)
        self._extractor: Extractor = Extractor()
        self._analyzer = TextAnalyser()

        # self._indexer = None #not implemented yet
        # self._loader = None #not implemented yet

        # todo : remove [_started, _connected] attributes
        # self._started = False
        # self._connected = False

    # Engine properties
    @property
    def searcher(self) -> Searcher:
        return self._searcher

    @property
    def extractor(self) -> Extractor:
        return self._extractor

    # text Analyzer
    @property
    def text_analyzer(self):
        return self._analyzer

    @property
    def connector(self):
        raise self._connector

    def loader(self):
        raise NotImplementedError

    def indexer(self):
        raise NotImplementedError

    # decorators

    def check_es_state(fn):
        def excute_function(self, first_time: bool, *args, **kwargs):
            engine_is_off_error = {"error": "engine is off"}

            if not self._connector.started:
                if not self._connector.connect():
                    return engine_is_off_error

            if not self._connector.connected:
                if not self._connector.reconnect():
                    return engine_is_off_error

            try:
                result = fn(self, *args, **kwargs)
                return result
            except Exception:
                self._connector.connected = False
                if first_time:
                    self._connector.reconnect()

                result = excute_function(self, False, *args, **kwargs)
                return result

            return engine_is_off_error

        def wraper(self, *args, **kwargs):

            result = excute_function(self, True, *args, **kwargs)
            return result

        return wraper

    def start_engine(self):
        self.es = self._connector.connect()
        # if (self._connector.check_connection(self.es)):
        #     self._started = True

    def get_engine_state(self):
        return self._connector.check_connection()

    # connect to Elasticsearch
    # def connect(self):
    #     self.es = connect()
    #     if self.es:
    #         if self.check_connection():
    #             logger.info('elasticSearch connected!')
    #             self._searcher = Searcher(es=self.es, index=self.index)
    #             self._started = True
    #             self._connected = True

    # if connection lost reconnect to Elasticsearch
    # def reconnect(self):
    #     if self.check_connection():
    #         self._connected = True

    # check if the connection was lost
    # def check_connection(self):
    #     if self.es:
    #         return self.es.ping()
    #     return False

    # process text [tokenize,stemming,etc]
    # def analyze_text(self, text: str):
    #     return process_text_stemm(text=text)

    # Search Arae

    # internal funciton

    @check_es_state
    def _execute_search(self, text):
        if self.check_connection():
            return simple_search(self.es, self.index, text)

    # def search(self, text):
    #     text = self.analyze_text(text)
    #     result = self._execute_search(text)
    #     return result_extractor(result)

    @check_es_state
    def simple_search_engine(self, serializer, **kwargs):
        processed_text = self._analyzer.process_text_stemm(serializer.get_data()[QUERY])
        extra_option = {P_QUERY: processed_text}

        result = self._searcher.simple_search(serializer=serializer, **extra_option, **kwargs)

        # result = self.extractor.extract(result)
        result = self._extractor.extract(result)

        return result

    @check_es_state
    def get_random_hadith_search_engine(self, serializer, **kwargs):
        result = self._searcher.get_random_hadith_search(serializer=serializer, **kwargs)
        result = result_extractor(result)
        return result

    @check_es_state
    def get_hadith_id_search_engine(self, serializer, **kwargs):
        result = self._searcher.get_hadith_id_search(serializer=serializer, **kwargs)
        result = result_extractor(result)
        return result
