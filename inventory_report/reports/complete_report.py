from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def produtos_estocados(list):
        empresas = {}
        retorno = ""
        for produto in list:
            empresa = produto["nome_da_empresa"]
            if empresa in empresas:
                empresas[empresa] += 1
            else:
                empresas[empresa] = 1
        for empresa, qtdade in empresas.items():
            retorno += f"- {empresa}: {qtdade}\n"

        return retorno

    @classmethod
    def generate(cls, list):
        report = super().generate(list)
        return (
            f"{report}\n"
            f"Produtos estocados por empresa:\n{cls.produtos_estocados(list)}"
        )
