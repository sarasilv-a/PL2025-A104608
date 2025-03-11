import re
import sys

# Padrões para os diferentes tipos de tokens
TOKENS = [
    (r'^\s*SELECT', 'PALAVRA_CHAVE'),
    (r'^\s*WHERE', 'PALAVRA_CHAVE'),
    (r'^\s*LIMIT', 'PALAVRA_CHAVE'),
    (r'^\s*a', 'OPERADOR_RDF'),  # ✅ Adicionado para reconhecer o operador "a"
    (r'^\s*\?[a-zA-Z_]+', 'VARIAVEL'),
    (r'^\s*[a-zA-Z_]+:[a-zA-Z_]+', 'PREFIXO_URI'),
    (r'^\s*"[a-zA-Z0-9\s]+"\@[a-zA-Z]+', 'LITERAL'),
    (r'^\s*[\{\}]', 'DELIMITADOR'),
    (r'^\s*\.', 'PONTO'),
    (r'^\s*\d+', 'NUMERO')
]

def tokenizar_query(query):
    tokens = []
    query = query.strip()  # Remover espaços em branco no início e no fim

    # 💡 **Ignorar Comentários**
    linhas = query.split("\n")
    linhas = [linha for linha in linhas if not linha.strip().startswith("#")]

    query = "\n".join(linhas)  # Rejuntar as linhas sem os comentários

    while query:
        for pattern, token_type in TOKENS:
            match = re.match(pattern, query, re.IGNORECASE)
            if match:
                token_value = match.group().strip()
                tokens.append((token_type, token_value))
                query = query[len(match.group()):].strip()  # Remover token processado
                break
        else:
            raise ValueError(f"❌ Erro: Token inválido encontrado perto de: '{query[:30]}...'")
    return tokens

# Ler o ficheiro passado como argumento
if len(sys.argv) != 2:
    print("Uso: python analisador.py <ficheiro>")
    sys.exit(1)

try:
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        query_text = f.read()

    tokens = tokenizar_query(query_text)

    print("✅ Tokens reconhecidos:")
    for token in tokens:
        print(token)

except FileNotFoundError:
    print("❌ Erro: Ficheiro não encontrado!")
except ValueError as e:
    print(e)
