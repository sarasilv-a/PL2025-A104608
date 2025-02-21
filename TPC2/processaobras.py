import re

def formatar_csv(ficheiro_entrada, ficheiro_saida):
    """ Normaliza o ficheiro CSV, removendo quebras de linha dentro dos campos. """
    with open(ficheiro_entrada, 'r', encoding='utf-8') as entrada, \
         open(ficheiro_saida, 'w', encoding='utf-8') as saida:
        conteudo = entrada.read()
        normalizado = re.sub(r'\n\s+', ' ', conteudo)
        saida.write(normalizado)

def ler_csv(ficheiro):
    with open(ficheiro, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    cabecalho = linhas[0].strip().split(';')
    dados = []
    for linha in linhas[1:]:
        valores = linha.strip().split(';')
        if len(valores) == len(cabecalho):
            dados.append(dict(zip(cabecalho, valores)))
    
    return dados

def ordenar_compositores(dados):
    """ Retorna uma lista ordenada dos compositores sem valores duplicados. """
    return sorted({dado.get('compositor', 'Desconhecido').strip() for dado in dados})

def contar_obras_por_periodo(dados):
    """ Conta quantas obras existem por período. """
    periodos = {}
    for dado in dados:
        periodo = dado.get('periodo', 'Desconhecido').strip()
        periodos[periodo] = periodos.get(periodo, 0) + 1
    return periodos

def listar_titulos_por_periodo(dados):
    """ Retorna um dicionário com títulos de obras organizados por período. """
    periodos = {}
    for dado in dados:
        periodo = dado.get('periodo', 'Desconhecido').strip()
        titulo = dado.get('nome', 'Sem título').strip()
        periodos.setdefault(periodo, []).append(titulo)
    
    for periodo in periodos:
        periodos[periodo].sort()
    
    return periodos

def main():
    ficheiro_entrada = 'obras.csv'
    ficheiro_formatado = 'obras_normalizado.csv'
    
    formatar_csv(ficheiro_entrada, ficheiro_formatado)

    dados = ler_csv(ficheiro_formatado)
    
    compositores_ordenados = ordenar_compositores(dados)
    obras_por_periodo = contar_obras_por_periodo(dados)
    titulos_por_periodo = listar_titulos_por_periodo(dados)

    print("\n📌 Compositores Ordenados:")
    for compositor in compositores_ordenados:
        print(f"  - {compositor}")

    print("\n📌 Distribuição das Obras por Período:")
    for periodo, quantidade in obras_por_periodo.items():
        print(f"  - {periodo}: {quantidade} obras")

    print("\n📌 Obras por Período:")
    for periodo, titulos in titulos_por_periodo.items():
        if (len(titulos) == 1): 
            print(f"\n🔹 {periodo} ({len(titulos)} obra):")
        else:
            print(f"\n🔹 {periodo} ({len(titulos)} obras):")
        for titulo in titulos:
            print(f"  - {titulo}")

if __name__ == '__main__':
    main()
