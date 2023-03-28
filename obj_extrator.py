import re


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
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("URL inválida")

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
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(url)

    def __str__(self):
        return "URL: " + self.url + "\n" + "URL parâmetros: " + self.get_url_parametros() + "\n" + "URL base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.25  # 1 dolar em REAL
moeda_origem = extrator_url.get_valor_parametros("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametros("moedaDestino")
quantidade = extrator_url.get_valor_parametros("quantidade")

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print("O valor em R$" + quantidade + " é igual a $" + (str(round(valor_conversao, 2))) + " dólares!")
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_concersao = int(quantidade) * VALOR_DOLAR
    print(("O valor em dolar é $" + quantidade + " que é igual a " + str(valor_concersao) + " reais!"))
else:
    print(f'O cambio de {moeda_origem} para {moeda_destino} não está disponível!')





#  Meus testes:
# print(extrator_url)
# print("O tamanho da URL é: ", len(extrator_url))
# valor_quantidade = extrator_url.get_valor_parametros("quantidade")
# print(valor_quantidade)
# print('__str__' in dir())  # Com o dir podemos ver os métodos da classe
