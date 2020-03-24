from influxdb import InfluxDBClient
import json


class DB(object):

    def __init__(self, db_config: str):
        self.config = json.load(db_config)
        ssl = self.config['ssl'] if 'ssl' in self.config.keys() else False
        verify_ssl = self.config['verify_ssl'] if 'verify_ssl' in self.config.keys() else False

        self.client = InfluxDBClient(host=self.config['host'], port=self.config['port'], username=self.config['user'], password=self.config['password'])

        self.client.switch_database(self.client['database'])

    def write(self, data: list):
        pass
