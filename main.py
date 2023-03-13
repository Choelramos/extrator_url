url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_url = url.find('?')
url_base = url[:indice_url]
print(url_base)

url_parametros = url[indice_url+1:]
print(url_parametros)

