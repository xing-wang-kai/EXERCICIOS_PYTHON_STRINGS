import re

url1 = "bytebank.com/cambio"
url2 = "bytebank.com.br/cambio"
url3 = "www.bytebank.com/cambio"
url4 = "www.bytebank.com.br/cambio"
url5 = "http://www.bytebank.com/cambio"
url6 = "http://www.bytebank.com.br/cambio"
url7 = "https://www.bytebank.com/cambio"
url8 = "https://www.bytebank.com.br/cambio"

url9 = "https://bytebank/cambio"
url0 = "https://bytebank.naoexiste/cambio"
url11 = "ht://bytebank.naoexiste/cambio"

regex = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = regex.match(url0)

if not match:
    raise ValueError("A url não é válida!")
