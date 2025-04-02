# 📌 TPC6 - Analisador Léxico e Sintático de Expressões Matemáticas

## 📅 Data
**02/04/2025**

## 👤 Autor
- **Nome:** Sara Catarina Loureiro da Silva  
- **Número de Aluno:** A104608  
<img src="../sarasilva.jpg" alt="Sara Silva" width="200" />

## 📖 Resumo

Este trabalho consistiu na implementação de um analisador léxico e sintático em Python com o auxílio da biblioteca PLY, para interpretar expressões matemáticas simples.

O programa é capaz de:

✅ **Reconhecer tokens léxicos** como números e operadores aritméticos (+, -, *, /);  
✅ **Interpretar expressões com base na gramática definida**, respeitando a precedência dos operadores;  
✅ **Avaliar e imprimir o resultado final da expressão introduzida pelo utilizador**;   
✅ **Reportar erros sintáticos em expressões inválidas**.

## 📊 Funcionalidades

### 📌 1. Analisador Léxico com PLY
O ficheiro `alt_lex.py` define os seguintes tokens:

`NUMBER`: Números inteiros

`PLUS`, `MINUS`, `TIMES`, `DIVIDE`: Operadores matemáticos básicos

🔹 Exemplo de tokenização:

``` plaintext
Input: 2 * 4 + 1

Output:
LexToken(NUMBER,2,1,0)
LexToken(TIMES,'*',1,2)
LexToken(NUMBER,4,1,4)
LexToken(PLUS,'+',1,6)
LexToken(NUMBER,1,1,8)
```

### 📌 2. Analisador Sintático com Precedência

O ficheiro `alt_sin.py` define uma gramática que:

- Respeita a precedência de multiplicação/divisão sobre adição/subtração

- Avalia corretamente expressões aninhadas (ex: 2 + 3 * 5 resulta em 17)

- Suporta apenas números inteiros

**-> Exemplo de interpretação:**

``` plaintext
Input: 2 + 3 * 4

Output:
Resultado da expressão: 14
Expressão válida: 2 + 3 * 4
```

**-> Exemplo de erro sintático:**

``` plaintext
Input: 2 + *

Output:
Erro sintático: LexToken(TIMES,'*',1,4)
Expressão inválida: 2 + *
```

## 🛠️ Execução
1. Executar o analisador sintático:

``` bash
python alt_sin.py
```

2. Introduzir expressões matemáticas diretamente no terminal:

``` plaintext
Digite uma expressão matemática: 10 + 5 * 2
Resultado da expressão: 20
```

## 📎 Ficheiros
- `alt_lex.py` - Analisador léxico com PLY.
- `alt_sin.py` - Analisador sintático com gramática e avaliação.
- `README.md` - Documentação do trabalho.
