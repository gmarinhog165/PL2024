import re
import sys

import re

def replace_with_li_tags(match):
    list_items = match.group(0).strip().split('\n')
    pattern = r'\d+\. (.+)\n?'
    li_tags = '\n'.join([f"\t<li>{re.match(pattern, item).group(1)}</li>" for item in list_items])
    return f"<ol>\n{li_tags}\n</ol>"

def headersMDtoHtml(text):
    texto = re.sub(r'(#{1,3}) (.*)', lambda match: f'<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>',
                   text, flags=re.MULTILINE)
    return texto


def boldMDtoHtml(text):
    texto = re.sub(r'\*{2}(.*)\*{2}', r'<b>\g<1></b>', text)
    return texto


def italicMDtoHtml(text):
    texto = re.sub(r'\*(.*)\*', '<i>\g<1></i>', text)
    return texto


def listsMDtoHtml(markdown):
    text = re.sub(r'(\d+\. (.+)\n?)+', replace_with_li_tags, markdown)
    return text


def linksMDtoHtml(texto):
    text = re.sub(r'^([^!]*)\[(.*)\]\((.+)\)$', '\g<1><a href="\g<3>">\g<2></a>', texto)
    return text


def imgsMDtoHtml(texto):
    text = re.sub(r'(.*)!\[(.+)\]\((.+)\)', '\g<1><img src="\g<3>" alt="\g<2>"/>', texto)
    return text


def basicSyntax(text):
    # headers
    texto = headersMDtoHtml(text)
    # bold
    texto = boldMDtoHtml(texto)
    # italico
    texto = italicMDtoHtml(texto)
    # listas
    texto = listsMDtoHtml(texto)
    # links
    texto = linksMDtoHtml(texto)
    # imagens
    texto = imgsMDtoHtml(texto)

    return texto


# python3 MdToHtml.py < <file.md>
def main():
    txt_data = sys.stdin.read()
    html = basicSyntax(txt_data)
    print(html)


if __name__ == '__main__':
    main()
