import requests

class FourDevs:

    def generate_company(self):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = "acao=gerar_empresa&pontuacao=S&estado=SP&idade=5"
        headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        } 

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text

    def generate_person(self):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload='acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&cep_estado=&txt_qtde=1&cep_cidade='
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()


    def generate_cpf(self):
        url = "https://www.4devs.com.br/ferramentas_online.php"

        payload = "acao=gerar_cpf&pontuacao=S&cpf_estado="
        headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text

    