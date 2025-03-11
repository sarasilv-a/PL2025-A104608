# 📌 TPC4 - Analisador Léxico para Queries

## 📅 Data
**28/02/2025**

## 👤 Autor
- **Nome:** Sara Catarina Loureiro da Silva  
- **Número de Aluno:** A104608  
<img src="../sarasilva.jpg" alt="Sara Silva" width="200" />

## 📖 Resumo

Este trabalho consistiu em:

- Implementar um **analisador léxico** em Python para reconhecer tokens numa linguagem de query semelhante a SPARQL.
- O programa recebe um ficheiro de input que contém a query e realiza a tokenização.
- Foram utilizadas **expressões regulares (regex)** para identificar e classificar diferentes elementos da query.
- O analisador suporta a identificação dos seguintes tokens:
    1. **Palavras-chave** (`SELECT`, `WHERE`, `LIMIT`)
    2. **Variáveis** (exemplo: `?nome`, `?desc`)
    3. **Identificadores URI** (exemplo: `dbo:MusicalArtist`)
    4. **Literais** (exemplo: `"Chuck Berry"@en`)
    5. **Operador RDF** (`a`)
    6. **Delimitadores** (`{` e `}`)
    7. **Pontos finais** (`.`)
    8. **Números** (`1000`)
- O programa também **verifica erros na tokenização**, indicando a linha onde o erro ocorre.

## 📊 Funcionalidades

### ✅ **Identificação de Tokens**
O programa consegue reconhecer os elementos da query e classificá-los corretamente. Exemplo de input:
```sparql
SELECT ?nome ?desc WHERE {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

Saída esperada:
```bash
✅ Tokens reconhecidos:
('PALAVRA_CHAVE', 'SELECT')
('VARIAVEL', '?nome')
('VARIAVEL', '?desc')
('PALAVRA_CHAVE', 'WHERE')
('DELIMITADOR', '{')
('VARIAVEL', '?s')
('OPERADOR_RDF', 'a')
('PREFIXO_URI', 'dbo:MusicalArtist')
('PONTO', '.')
...
```

### ✅ **Deteção de Erros**
Se for encontrado um token inválido, o programa indica a **linha exata** do erro:
```bash
🚫 Erro na linha 4: Token inválido encontrado perto de 'xyz_invalid_token...'
```

## 🛠️ Execução
Para correr o programa, basta executar:
```bash
python analisador.py query.txt
```

Certifica-te de que o ficheiro `query.txt` está na mesma pasta.

## 📚 Ficheiros
- `query.txt` - Contém a query a ser analisada.
- `analisador.py` - Código Python do analisador léxico.
- `README.md` - Documentação do trabalho.

