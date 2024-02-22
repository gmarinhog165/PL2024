# TPC2 - Conversão Markdown para HTML

## Enunciado
O objetivo deste TPC é criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" de MD.

* Heading: `# H1, ## H2, ### H3`.
* Bold: `**bold text**`.
* Italic: `italicized text`.
* Ordered: 
```md
1. First item
2. Second item
3. Third item
```
* Link: `[title](https://www.example.com)`
* Image: `![alt text](image.jpg)`

A minha solução faz uso de Regex de modo a identificar padrões num determinado texto e converte-os para o formato HTML. 
A execução deste programa para o exemplo que construí, de forma a garantir que funciona em qualquer ficheiro MD e não apenas em sintaxe individual, dá-se através do comando:

```bash
$ python3 MdToHtml.py < ex.md
```
