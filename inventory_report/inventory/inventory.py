import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def leitura(path):
        with open(path, 'r') as file:
            if path.endswith('.csv'):
                data = csv.DictReader(file)
                return [row for row in data]
            if path.endswith('.json'):
                data = file.read()
                return json.loads(data)
            if path.endswith('.xml'):
                data = xmltodict.parse(file.read())
                print(data)
                return data['dataset']['record']

    @classmethod
    def import_data(cls, path, type):
        data = cls.leitura(path)

        if type == 'simples':
            report = SimpleReport()
        if type == 'completo':
            report = CompleteReport()

        return report.generate(data)
