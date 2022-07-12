from pprint import pprint

import requests


class FourDevs:

    def generate_company(self):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = "acao=gerar_empresa&pontuacao=S&estado=SP&idade=5"
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            return response.text
        return None

    def generate_person(self):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = 'acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&cep_estado=&txt_qtde=1&cep_cidade='
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            return response.json()
        return None

    def generate_cpf(self):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = "acao=gerar_cpf&pontuacao=S&cpf_estado="
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            return response.text
        return None

    def generate_lorem_ipsum(self, quantity, options):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        if options == "words":
            options = "pala"
        elif options == "paragraph":
            options = "para"

        payload = f"acao=gerar_textos&txt_quantidade={quantity}&opcoes={options}&tipo_texto=texto&iniciar=N"
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            return response.text
        return None

    def validate_cpf(self, cpf):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = f"acao=validar_cpf&txt_cpf={cpf}"
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if 'Falso' in response.text:
            return False
        return True

    def validate_cnpj(self, cnpj):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = f"acao=validar_cnpj&txt_cnpj={cnpj}"
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if 'Falso' in response.text:
            return False
        return True

    def validate_cnh(self, cnh):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = f"acao=validar_cnh&txt_cnh={cnh}"
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if 'Falso' in response.text:
            return False
        return True

    def validate_credit_card_number(self, credit_card_number, flag):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = f"acao=validar_cc&txt_cc={credit_card_number}&bandeira={flag}"
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if 'Falso' in response.text:
            return False
        return True
