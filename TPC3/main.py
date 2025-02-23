"""
Conversor de MarkDown para HTML
"""
import sys
import re

import sys
import re

def markdown2html(text):
    # headers
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)

    # italico
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)

    # lista numerada
    text = re.sub(r'^\d+\. (.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    ## faltam os oLS 

    # links
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)

    # imagens
    text = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
    # imagem com erro 

    return text

def main():
    texto = """
# Título
## Subtítulo
### Subsubtítulo
**bold**
*italico*
1. lista numerada
2. lista numerada
33. lista numerada

Como pode ser consultado em [página da UC](http://www.uc.pt)

![imagem dum coelho](http://www.coellho.com) ...
    """
    print(markdown2html(texto))


main()