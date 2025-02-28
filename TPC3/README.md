# 📌 TPC3 - Conversor de Markdown para HTML

## 📅 Data
**26/02/2025**

## 👤 Autor
- **Nome:** Sara Catarina Loureiro da Silva  
- **Número de Aluno:** A104608  
<img src="../sarasilva.jpg" alt="Sara Silva" width="200" />

## 📖 Resumo
Este trabalho consistiu em:

- Implementar um programa em Python para converter ficheiros Markdown em ficheiros HTML.
- O conversor suporta a transformação de elementos da secção **Basic Syntax** da Cheat Sheet de Markdown, nomeadamente:
    1. **Cabeçalhos** (`#`, `##`, `###`)
    2. **Texto em negrito** (`**texto**`)
    3. **Texto em itálico** (`*texto*`)
    4. **Listas numeradas** (`1. item`)
    5. **Links** (`[texto](url)`)
    6. **Imagens** (`![alt](url)`)

- A leitura e a escrita dos ficheiros é realizada diretamente com `open()`, sem usar bibliotecas externas além de `re`.
- O uso de **expressões regulares (regex)** foi fundamental para reconhecer e transformar os elementos de Markdown em HTML.

## 📊 Funcionalidades

### ✅ **Cabeçalhos:**
- `# Título` é transformado em `<h1>Título</h1>`
- `## Subtítulo` é transformado em `<h2>Subtítulo</h2>`
- `### Subsubtítulo` é transformado em `<h3>Subsubtítulo</h3>`

### ✅ **Texto Formatado:**
- `**bold**` é transformado em `<b>bold</b>`
- `*itálico*` é transformado em `<i>itálico</i>`

### ✅ **Listas Numeradas:**
- Conjuntos de linhas numeradas (`1. item`, `2. item`, ...) são envolvidas em `<ol>` e cada item é colocado dentro de `<li>`.

### ✅ **Links:**
- `[texto](url)` é transformado em `<a href="url">texto</a>`

### ✅ **Imagens:**
- `![alt](url)` é transformado em `<img src="url" alt="alt"/>`

## 🛠️ Execução
Para correr o programa e converter um ficheiro Markdown para HTML:
```bash
python conversor.py teste.md
