from datetime import datetime, timedelta


class SimpleReport:

    def data_antiga(list):
        data_mais_antiga = datetime.now()
        for produto in list:
            produto_data = produto['data_de_fabricacao']
            data_fabricacao = datetime.strptime(f"{produto_data}", '%Y-%m-%d')
            if data_fabricacao < data_mais_antiga:
                data_mais_antiga = data_fabricacao

        return data_mais_antiga.strftime('%Y-%m-%d')

    def validade_proxima(list):
        data_atual = datetime.now()
        diferenca = timedelta(days=9999999)
        data_proxima = None
        for produto in list:
            produto_data = produto['data_de_validade']
            data_validade = datetime.strptime(f"{produto_data}", '%Y-%m-%d')
            if data_validade > data_atual:
                dif = data_validade - data_atual
                if dif.days < diferenca.days:
                    data_proxima = data_validade
                    diferenca = dif

        return data_proxima.strftime('%Y-%m-%d')

    def empresa_produtos(list):
        empresas = {}
        for produto in list:
            empresa = produto['nome_da_empresa']
            if empresa in empresas:
                empresas[empresa] += 1
            else:
                empresas[empresa] = 1

        return max(empresas, key=empresas.get)

    @classmethod
    def generate(cls, list):
        return (
            f"Data de fabricação mais antiga: {cls.data_antiga(list)}\n"
            f"Data de validade mais próxima: {cls.validade_proxima(list)}\n"
            f"Empresa com mais produtos: {cls.empresa_produtos(list)}"
        )
