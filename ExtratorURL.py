import re

class ExtratorUrl:
    def __init__(self, url):
        self.__url = self.ajustarURL(url)
        self.validarURL()

    def ajustarURL(self, valor):
        if type(valor) == str:
            return valor.replace(" ", "").strip()
        else:
            return ""

    def validarURL(self):
        if not self.__url:
            raise ValueError("\033[041m ATENÇÃO: \033[0m A URL NÃO PODE ESTA EM BRANCO!")

        regex = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = regex.match(self.__url)

        if not match:
            raise ValueError("A url não é válida!")

    def get_url_base(self):
        interrogacao = self.__url.find("?")
        base_url = self.__url[:interrogacao]  # url.split("?")
        return base_url

    def get_url_parametro(self):
        interrogacao = self.__url.find("?")
        url_parametro = self.__url[interrogacao + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_busca = indice_parametro + len(parametro_busca) + 1
        indice_final_busca = self.get_url_parametro().find("&", indice_busca)

        if indice_final_busca == -1:
            valor_parametro = self.get_url_parametro()[indice_busca:]
        else:
            valor_parametro = self.get_url_parametro()[indice_busca:indice_final_busca]
        return valor_parametro
    def __len__(self):
        return len(self.__url)

    def __str__(self):
        return f"--> URL: {self.__url}\n" \
               f"--> Parametro: {self.get_url_parametro()}\n" \
               f"--> BASE URL: {self.get_url_base()}"

    def __eq__(self, other):
        return self.__url == other.__url
