from bs4 import BeautifulSoup

class BeautifulSoupParser:

    @staticmethod
    def parseHtml(html):
        soup = BeautifulSoup(html, 'html.parser')
        dict_output = {}
        for div in soup.find_all('div', class_='row small-collapse'):
            key = div.find('input').get('id')
            value = str(div.find('input').get('value'))
            if key == 'ie':
                key = 'inscricao_estadual'
            dict_output[key] = value
        return dict_output