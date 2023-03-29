# Web Scraping Python Live

## Conceitos

1. Web scraping
    - Consiste em extrair (raspar) dados de uma página web
2. Web crawler
    - O processo de raspagem de dados é automatizado por um bot chamado de web crawler
3. Arquivo `robots.txt`
    - Serve para determinar quais páginas um crawler de um buscador pode acessar
    - Por meio deste arquivo é possível determinar qual(ais) páginás serão exibidas ou não pelo Google
    - Mais informações [aqui](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
    - Exemplo de arquivo [`robots.txt`](https://www.mercadolivre.com.br/robots.txt)
    - Algumas aplicações deixam claro que o uso de crawlers são proibidas, como é o [caso do LinkedIn](https://www.linkedin.com/robots.txt)
4. [XPath](https://www.w3schools.com/xml/xpath_intro.asp) e CSS

## Opções existentes

1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/)
2. Scrapy

[Qual escolher?](https://coderslegacy.com/scrapy-vs-beautifulsoup/)

## Comandos úteis Scrapy

1. Criar um projeto

`scrapy startproject <project_name>`

2. Executar um spider individualmente

`scrapy runspider <file_name>.py`


