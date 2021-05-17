import logging

from elasticsearch.client import Elasticsearch
from elasticsearch.exceptions import ConnectionError

from core.engine.components.searcher import simple_search, Searcher
from core.engine.components.extractor import Extractor
from core.engine.components.text_analyzer import process_text_stemm
from core.engine.components.extractor import result_extractor
from core.engine.components.elasticsearch_adapter.connecter import connect

from core.data.fields import QUERY, P_QUERY
from .components.extractor import result_extractor

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Engine:
    def __init__(self, index=None):
        self.index = index

        self.es: Elasticsearch = None

        # components of components
        # need for elasticsearch instance
        self._searcher: Searcher = None

        # no need for elasticsearch instance
        self._extractor: Extractor = Extractor()

        # self._analyzer = None #not implemented yet
        # self._indexer = None #not implemented yet
        # self._loader = None #not implemented yet

        self._started = False
        self._connected = False

    # Engine properties
    @property
    def searcher(self) -> Searcher:
        return self._searcher

    @property
    def extractor(self) -> Extractor:
        return self._extractor

    # text Analyzer
    def text_analyzer(self):
        raise NotImplementedError

    def connector(self):
        raise NotImplementedError

    def loader(self):
        raise NotImplementedError

    def indexer(self):
        raise NotImplementedError

    # decorators

    def check_es_state(fn):
        def wraper(self, *args, **kwargs):
            if not self._started:
                self.connect()

            if not self._connected:
                self.reconnect()

            try:
                return fn(self, *args, **kwargs)
            except ConnectionError:
                self._connected = False

        return wraper

    def get_engine_state(self):
        return self.check_connection()

    # connect to Elasticsearch
    def connect(self):
        self.es = connect()
        if self.es:
            if self.check_connection():
                logger.info('elasticSearch connected!')
                self._searcher = Searcher(es=self.es, index=self.index)
                self._started = True
                self._connected = True

    # if connection lost reconnect to Elasticsearch
    def reconnect(self):
        if self.check_connection():
            self._connected = True

    # check if the connection was lost
    def check_connection(self):
        if self.es:
            return self.es.ping()
        return False

    # process text [tokenize,stemming,etc]
    def analyze_text(self, text: str):
        return process_text_stemm(text=text)

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

    def simple_search_engine(self, serializer, **kwargs):
        processed_text = process_text_stemm(serializer.get_data()[QUERY])

        extra_option = {P_QUERY: processed_text}

        result = self._searcher.simple_search(serializer=serializer, **extra_option, **kwargs)
        # result = result_extractor(result)
        result = self.extractor.extract(result)

        return result

    def get_random_hadith_search_engine(self, serializer, **kwargs):
        result = self._searcher.get_random_hadith_search(serializer=serializer, **kwargs)
        result = result_extractor(result)
        return result

    def get_hadith_id_search_engine(self, serializer, **kwargs):
        result = self._searcher.get_hadith_id_search(serializer=serializer, **kwargs)
        result = result_extractor(result)
        return result
