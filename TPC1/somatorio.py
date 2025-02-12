def calcular_soma_entrada():
    soma_total = 0
    estado_ativo = True
    buffer_estado = ""
    i = 0
    entrada = input("Digite o texto: ")
    
    while i < len(entrada):
        caractere = entrada[i]
        buffer_estado += caractere.lower()
        
        if len(buffer_estado) > 3:
            buffer_estado = buffer_estado[1:]
        
        if buffer_estado.endswith("on"):
            estado_ativo = True
            buffer_estado = ""
        elif buffer_estado.endswith("off"):
            estado_ativo = False
            buffer_estado = ""
        
        if caractere == '=':
            print(f"Soma atual: {soma_total}")
        
        if estado_ativo and caractere.isdigit():
            numero_atual = ""
            while i < len(entrada) and entrada[i].isdigit():
                numero_atual += entrada[i]
                i += 1
            if numero_atual:
                soma_total += int(numero_atual)
            continue
        
        i += 1
    
    print(f"Soma final: {soma_total}")

if __name__ == "__main__":
    calcular_soma_entrada()
