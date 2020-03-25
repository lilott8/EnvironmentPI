from influxdb import InfluxDBClient
import json
import colorlog
from typing import List


class DB(object):

    def __init__(self, db_config: str):
        self.logger = colorlog.getLogger(self.__class__.__name__)

        self.logger.info(db_config)

        with open(db_config) as f:
            self.config = json.load(f)

        ssl = self.config['ssl'] if 'ssl' in self.config.keys() else False
        verify_ssl = self.config['verify_ssl'] if 'verify_ssl' in self.config.keys() else False

        self.client = InfluxDBClient(host=self.config['host'], port=self.config['port'], username=self.config['user'], password=self.config['password'])

        self.client.switch_database(self.config['database'])

    def close(self):
        self.client.close()

    def write(self, data: List):
        self.client.write_points(data)
        #self.logger.info(f"writing: {data}")
