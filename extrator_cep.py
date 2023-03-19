import re  # biblioteca ReGex, Regular Expression
endereco = "Mauricio Gonçalves costa 230, Vila Antonute, 15200-000 José Bonifácio"

padrao = re.compile("[0-9]{5}-{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)


