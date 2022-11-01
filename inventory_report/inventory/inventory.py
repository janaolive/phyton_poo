import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport


def csv_import(path, type):
    with open(path) as file:
        line_content = csv.DictReader(file)
        content = [item for item in line_content]
        return content


def json_import(path, type):
    with open(path) as file:
        line_content = json.load(file)
        content = [item for item in line_content]
        return content


def xml_import(path, type):
    with open(path) as file:
        line_content = file.read()
        content = [
            item for item in xmltodict.parse(
                line_content)["dataset"]["record"]
        ]
        return content


class Inventory:
    @staticmethod
    def import_data(path, type):
        if ".csv" in path:
            content = csv_import(path, type)
        elif ".json" in path:
            content = json_import(path, type)
        else:
            content = xml_import(path, type)
        if type == "simples":
            type_report = SimpleReport.generate(content)
        elif type == 'completo':
            type_report = CompleteReport.generate(content)
        else:
            raise TypeError
        return type_report
