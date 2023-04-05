import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('.json'):
            with open(path, 'r') as file:
                data = file.read()
                return json.loads(data)
        else:
            raise ValueError('Arquivo inválido')
