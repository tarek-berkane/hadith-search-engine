from elasticsearch import Elasticsearch


class Connector:
    def __init__(self, es: Elasticsearch):
        self.es: Elasticsearch = es

        self.started = False
        self.connected = False

    # def check_es_state(fn):
    #     def wraper(self, *args, **kwargs):
    #         if not self._started:
    #             self.connect()
    #
    #         if not self._connected:
    #             self.reconnect()
    #
    #         try:
    #             return fn(self, *args, **kwargs)
    #         except ConnectionError:
    #             self._connected = False
    #
    #     return wraper

    def get_engine_state(self):
        return self.check_connection()

    # connect to Elasticsearch
    def connect(self):
        if self.es:
            if self.check_connection():
                self._started = True
                self._connected = True
                return True
        return False

    # if connection lost reconnect to Elasticsearch
    def reconnect(self):
        if self.check_connection():
            self._connected = True
            return True
        return False

    # check if the connection was lost
    def check_connection(self):
        if self.es:
            return self.es.ping()
        return False
