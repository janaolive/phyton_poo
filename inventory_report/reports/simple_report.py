from datetime import date


def earliest_manufacturing_date(list):
    year, month, day = list[0].split("-")
    manufacturing_date = date(int(year), int(month), int(day))
    for data in list:
        year, month, day = data.split("-")
        date_changed = date(int(year), int(month), int(day))
        if date_changed < manufacturing_date:
            manufacturing_date = date_changed
    return manufacturing_date


def nearest_expiration_date(list):
    year, month, day = list[0].split("-")
    expiration_date = date(int(year), int(month), int(day))
    for data in list:
        year, month, day = data.split("-")
        date_changed = date(int(year), int(month), int(day))
        if date_changed < expiration_date and date_changed >= date.today():
            expiration_date = date_changed
    return expiration_date


def company_with_more_products(list):
    company = ""
    quantity = 0
    for empresa, quantidade in list.items():
        if quantidade >= quantity and company is not None:
            quantity = quantidade
            company = empresa
    return company


class SimpleReport:
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
        return (
            f"Data de fabricação mais antiga: {str(manufacture)}\n"
            f"Data de validade mais próxima: {str(expiration)}\n"
            f"Empresa com mais produtos: {str(company)}"
        )
