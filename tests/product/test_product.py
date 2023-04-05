import pytest
from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(1, 'Geladeira', 'Brastemp', '12/12/2020', '12/12/2050',
                      '123456', 'local seco')
    assert produto.id == 1
    assert produto.nome_do_produto == 'Geladeira'
    assert produto.nome_da_empresa == 'Brastemp'
    assert produto.data_de_fabricacao == '12/12/2020'
    assert produto.data_de_validade == '12/12/2050'
    assert produto.numero_de_serie == '123456'
    assert produto.instrucoes_de_armazenamento == 'local seco'

    with pytest.raises(TypeError):
        Product()
