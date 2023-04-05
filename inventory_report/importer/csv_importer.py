import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(path):
        if path.endswith('.csv'):
            with open(path, 'r') as file:
                data = csv.DictReader(file)
                return [row for row in data]
        else:
            raise ValueError('extensão do arquivo inválida')
