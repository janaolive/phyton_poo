from inventory_report.reports.simple_report import (
    SimpleReport,
    earliest_manufacturing_date,
    nearest_expiration_date,
    company_with_more_products,
)


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        expirations = [item["data_de_validade"] for item in list]
        manufactures = [item["data_de_fabricacao"] for item in list]
        company_and_products = {item["nome_da_empresa"]: 0 for item in list}
        for item in list:
            company_and_products[item["nome_da_empresa"]] += 1
        expiration = nearest_expiration_date(expirations)
        manufacture = earliest_manufacturing_date(manufactures)
        company = company_with_more_products(company_and_products)
        products_by_company = [
            f"- {empresa}: {quantidade}\n"
            for empresa, quantidade in company_and_products.items()            
        ]
        response = "".join(products_by_company)
        return (
            f"Data de fabricação mais antiga: {str(manufacture)}\n"
            f"Data de validade mais próxima: {str(expiration)}\n"
            f"Empresa com mais produtos: {str(company)}\n"
            f"Produtos estocados por empresa:\n"
            f"{response}"
        )
