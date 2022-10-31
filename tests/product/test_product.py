from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        id=1,
        nome_do_produto="Bach Floral",
        nome_da_empresa="Institute Bach",
        data_de_fabricacao="2022-10-31",
        data_de_validade="2023-10-31",
        numero_de_serie="IBF 254",
        instrucoes_de_armazenamento="local seco",
    )
    assert new_product.id == 1
    assert new_product.nome_do_produto == "Bach Floral"
    assert new_product.nome_da_empresa == "Institute Bach"
    assert new_product.data_de_fabricacao == "2022-10-31"
    assert new_product.data_de_validade == "2023-10-31"
    assert new_product.numero_de_serie == "IBF 254"
    assert new_product.instrucoes_de_armazenamento == "local seco"
