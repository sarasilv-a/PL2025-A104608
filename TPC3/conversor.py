import re

def conversor(texto):

    texto = re.sub(r'^# (.+)$', r'<h1>\1</h1>', texto, flags=re.MULTILINE)
    texto = re.sub(r'^## (.+)$', r'<h2>\1</h2>', texto, flags=re.MULTILINE)
    texto = re.sub(r'^### (.+)$', r'<h3>\1</h3>', texto, flags=re.MULTILINE)

    texto = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', texto)

    texto = re.sub(r'\*(.+?)\*', r'<i>\1</i>', texto)
    
    texto = re.sub(r'\n\d+\. (.+)', r'\n<li>\1</li>', texto)
    texto = re.sub(r'(?:<li>.+</li>\n?)+', lambda m: f'<ol>\n{m.group(0)}\n</ol>', texto)

    texto = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', texto)

    texto = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', texto)
    
    return texto

test_conversor = """
# Título Principal
## Subtítulo
### Subsubtítulo

Este é um **exemplo** de *itálico* e **bold**.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
"""

html_output = conversor(test_conversor)
print(html_output)
