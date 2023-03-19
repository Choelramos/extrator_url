import re  # biblioteca ReGex, Regular Expression
endereco = "Mauricio Gonçalves costa 230, Vila Antonute, 15200-000 José Bonifácio"

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
