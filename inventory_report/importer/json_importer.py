import json
from inventory_report.importer.importer import Importer


class JsonIMporter(Importer):
    @classmethod
    def import_data(path):
        with open(path, 'r') as file:
            data = file.read()
            return json.loads(data)
