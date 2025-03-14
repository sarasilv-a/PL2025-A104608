import json
import os
import re

# Nome do ficheiro JSON onde o stock será armazenado
STOCK_FILE = "stock.json"

# Carregar o stock do ficheiro JSON
if os.path.exists(STOCK_FILE):
    with open(STOCK_FILE, "r", encoding="utf-8") as f:
        stock = json.load(f)
else:
    stock = []

saldo = 0  # Saldo do utilizador em cêntimos
MOEDAS_VALIDAS = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}

def listar_produtos():
    print("maq:")
    print("cod    |  nome      |  quantidade  |  preço")
    print("---------------------------------")
    for produto in stock:
        print(f"{produto['cod']}    {produto['nome']}    {produto['quant']}    {produto['preco']}€")

def inserir_moedas(comando):
    global saldo
    moedas = re.findall(r'(\d+[eE]|\d+[cC])', comando)  # Agora reconhece maiúsculas também
    print(f"DEBUG: moedas = {moedas}")  # <-- Mantém para testar

    adicionadas = []

    for moeda in moedas:
        moeda = moeda.lower()  # Converte para minúsculas para compatibilidade com `MOEDAS_VALIDAS`
        if moeda in MOEDAS_VALIDAS:
            saldo += MOEDAS_VALIDAS[moeda]
            adicionadas.append(moeda)
        else:
            print(f"maq: Atenção! Moeda inválida ignorada: {moeda}")

    print(f"DEBUG: saldo = {saldo}")  # <-- Mantém para testar
    if adicionadas:
        print(f"maq: Saldo = {saldo}c")



def selecionar_produto(codigo):
    global saldo
    for produto in stock:
        if produto["cod"] == codigo:
            preco = int(float(produto["preco"]) * 100)  # Converter euros para cêntimos
            if produto["quant"] == 0:
                print("maq: Produto esgotado.")
                return
            if saldo >= preco:
                saldo -= preco
                produto["quant"] -= 1
                print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                print(f"maq: Saldo = {saldo}c")
            else:
                print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                print(f"maq: Saldo = {saldo}c; Pedido = {preco}c")
            return
    print("maq: Produto inexistente.")

def calcular_troco():
    global saldo
    troco = []
    for moeda, valor in sorted(MOEDAS_VALIDAS.items(), key=lambda x: -x[1]):  # Ordenar do maior para o menor
        while saldo >= valor:
            saldo -= valor
            troco.append(moeda)
    if troco:
        print("maq: Pode retirar o troco:", ", ".join(troco))
    print("maq: Até à próxima")

def main():
    global saldo
    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    while True:
        comando = input(">> ").strip().upper()
        print(f"DEBUG: comando recebido = {comando}")
        if comando == "LISTAR":
            listar_produtos()
        elif comando.startswith("MOEDA"):
            inserir_moedas(comando)
        elif comando.startswith("SELECIONAR"):
            partes = comando.split()
            if len(partes) == 2:
                selecionar_produto(partes[1])
            else:
                print("maq: Comando inválido. Utilize 'SELECIONAR <código>'")
        elif comando == "SAIR":
            calcular_troco()
            break
        else:
            print("maq: Comando inválido.")
    # Guardar stock atualizado no ficheiro JSON
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)

if __name__ == "__main__":
    main()
