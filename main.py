from ExtratorURL import *
import re

url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100".replace(" ", "")

extratorUrl = ExtratorUrl(url)

valor_quantidade = extratorUrl.get_valor_parametro("moedaOrigem")

print(f"Valor QTD: {valor_quantidade}")

endereco = "rua das antas, 222, osasco-sp cep: 06266-000 , brasil , america latina"
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
valor = padrao.search(endereco)
if valor:
    cep = valor.group()
    print(f"O CEP É : {cep}")
else:
    print(f"valor não encontrado {valor} - {padrao}")
