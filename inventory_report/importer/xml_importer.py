import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(path):
        if path.endswith('.xml'):
            with open(path, 'r') as file:
                data = xmltodict.parse(file.read())
                return data['dataset']['record']
        else:
            raise ValueError('extensão do arquivo inválida')
