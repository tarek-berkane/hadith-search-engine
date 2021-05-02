# ENGINE:
# es adapter:
# - connect to ES
# - reconnect to ES
# - check connection
# text analyzer
# - get text analyzer
# - analyze text
# search
# - search text
# - advance search text
# - extract data
# - build reslult data
# indexing
# - get index
# - creat index
# - check index
# loader
# - load data

import logging

from elasticsearch.client import Elasticsearch
from elasticsearch.exceptions import ConnectionTimeout, ConnectionError
from urllib3.exceptions import NewConnectionError

from .searcher import simple_search
from .text_analyzer import process_text_stemm
from .extractor import result_extractor
from .elasticsearch_adapter.connecter import connect

logger = logging.getLogger(__name__)


class Engine:
    def __init__(self, index=None):
        self.es: Elasticsearch = None
        self.index = index

        self._started = False
        self._connected = False

    # decorators

    def check_es_state(fn):
        def wraper(self, *args, **kwargs):
            if self._started:
                if self._connected:
                    try:
                        return fn(self, *args, **kwargs)
                    except ConnectionError:
                        self._connected = False

        return wraper

    def get_engine_state(self):
        return self.check_connection()

    # connect to Elasticsearch
    def connect(self):
        try:
            self.es = connect()
            if self.es:
                if self.check_connection():
                    logger.info('elasticSearch connected!')
                    self._started = True
                    self._connected = True
        except NewConnectionError:
            logger.error('elasticSearch not connected!')

    # if connection lost reconnect to Elasticsearch
    def reconnect(self):
        if self.check_connection():
            self._connected = True

    # check if the connection was lost
    def check_connection(self):
        if self.es:
            return self.es.ping()
        return False

    # text Analyzer

    def _get_text_analyzer(self):
        pass

    # process text [tokenize,stemming,etc]
    def analyze_text(self, text: str):
        return process_text_stemm(text=text)

    # Search Arae

    # internal funciton
    @check_es_state
    def _execute_search(self, text):
        if self.check_connection():
            return simple_search(self.es, self.index, text)

    def search(self, text):
        text = self.analyze_text(text)
        result = self._execute_search(text)
        return result_extractor(result)

    def advance_search(self):
        pass

    def extract_data(self):
        pass

    def _build_result_data(self):
        pass

    def get_result(self):
        pass

    def load_data(self):
        pass

    # index area
    def _load_index(self):
        pass
