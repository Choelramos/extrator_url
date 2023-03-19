class ExtratorURL:
    def __init__(self, url):
        self.url = url
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:  # Se bool URL for falso, bool false, vai retornar o valor
            raise ValueError('URL vazia')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametros(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_valor_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor

    def comeca_com_https(self):
        retorno = self.url.startswith("https")
        if retorno:
            return print("Começa com https")
        else:
            return print("Não começa com https")


    def fim_da_base(self):
        fim_base = self.get_url_base().endswith("/cambio")
        if fim_base:
            return print("O fim da base termina com: /cambio")
        else:
            return print("O fim da base não termina com: /cambio")


extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real")
extrator_url.comeca_com_https()
extrator_url.fim_da_base()
