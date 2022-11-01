import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            line_content = file.read()
            content = [
                item for item in xmltodict.parse(
                    line_content)["dataset"]["record"]
            ]
            return content
