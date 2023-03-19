import re

# url = "https://www.bytebank.com.br/cambio"

padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
compara_padrao = padrao.match("https://www.bytebank.com.br/cambio")
if not compara_padrao:
    raise ValueError("URL inválida")
