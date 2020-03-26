from influxdb import InfluxDBClient
import colorlog
from typing import List
from misc.config import Config


class DB(object):

    def __init__(self, config: Config):
        self.logger = colorlog.getLogger(self.__class__.__name__)
        self.config = config

        ssl = self.config.db['ssl'] if 'ssl' in self.config.db.keys() else False
        verify_ssl = self.config.db['verify_ssl'] if 'verify_ssl' in self.config.db.keys() else False

        self.client = InfluxDBClient(host=self.config.db['host'], port=self.config.db['port'], username=self.config.db['user'], password=self.config.db['password'])

        self.client.switch_database(self.config.db['table'])

    def close(self):
        self.client.close()

    def write(self, data: List):
        self.client.write_points(data)
        #self.logger.info(f"writing: {data}")
