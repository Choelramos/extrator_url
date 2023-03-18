class ExtratorURL:
    def __init__(self, url):
        self.url = url
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str():
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
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


extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametros("quantidade")
url_base = extrator_url.get_url_base()
url_parametros = extrator_url.get_url_parametros()

print(valor_quantidade)
print(url_base)
print(url_parametros)
