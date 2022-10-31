from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "Bach Floral"
    nome_da_empresa = "Institute Bach"
    data_de_fabricacao = "2022-10-31"
    data_de_validade = "2023-10-31"
    numero_de_serie = "IBF 254"
    instrucoes_de_armazenamento = "local seco"

    new_product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    new_product_response = (
        f"O produto {nome_do_produto}"
        f" fabricado em {data_de_fabricacao}"
        f" por {nome_da_empresa} com validade"
        f" até {data_de_validade}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}."
    )
    assert str(new_product) == new_product_response
