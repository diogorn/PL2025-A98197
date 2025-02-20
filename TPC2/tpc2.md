# Processamento de Linguagens 2025

## Objetivo do TPC


Neste TPC, é proibido usar o módulo CSV do Python;
Deverás ler o dataset, processá-lo e criar os seguintes resultados:
. Lista ordenada alfabeticamente dos compositores musicais;
. Disrtribuição das obras por período: quantas obras catalogadas em cada período;
. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período. 

---

## Abordagem 

Visto que cada entrada do csv pode ser multi-linha utilizei uma expressão regular para identificar corretamente os 7 campos de cada registro. 
A expressão utilizada foi:

r'^([^;]+);"?([\s\S]*?)"?;([^;]+);([^;]+);([^;]+);([^;]+);([^;]+)$'

### Explicação

^ ->  inicio da linha

([^;]+) -> Captura o primeiro campo-título da obra, até encontrar ;

; -> Delimitador que separa os campos no CSV

"? -> Permite aspas opcionais no início do campo **desc**

([\s\S]*?) ->  descrição da obra. O \s\S assegura que todos os caracteres sejam incluídos, incluindo quebras de linha

"? -> permite fechar aspas opcionais do campo **desc**

;([^;]+) -> Captura o campo anoCriacao

;([^;]+) -> Captura o campo periodo da obra

;([^;]+) -> Captura o campo compositor

;([^;]+) -> Captura o campo duração

;([^;]+)$ -> Captura o campo id, garantindo que seja o último da linha

A flag re.MULTILINE é utilizada para garantir que cada linha do CSV seja tratada separadamente, mesmo quando a descrição da obra contenha múltiplas linhas.

## Resultados obtidos (parciais)
<img width="945" alt="image" src="https://github.com/user-attachments/assets/7e9c39b5-6431-4d52-bb40-caaeaedf4b07" />




---

## Identificação

**Nome:** Diogo do Rego Neto  
**Número:** A98197  
**Data:** 13-02-2025  

![Identificação](https://github.com/user-attachments/assets/385c7dc7-ea9c-4c82-b595-82a84b63bac0)

> **Sobre a Foto:**  
> A imagem utilizada neste documento é referenciada através de uma URL. Eu não possuo nenhuma foto sua; a imagem foi incluída conforme o exemplo fornecido nas especificações do TPC. Caso deseje alterar ou remover a imagem, basta atualizar a URL ou removê-la do arquivo Markdown.

---

Este trabalho evidencia a aplicação de técnicas avançadas de processamento de texto e o uso estratégico de expressões regulares para manipular dados em formato CSV sem recorrer ao módulo `csv` do Python, demonstrando a versatilidade na extração e organização de informações.

