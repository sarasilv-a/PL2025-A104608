# 📌 TPC5 - Analisador Léxico para Queries

## 📅 Data
**14/03/2025**

## 👤 Autor
- **Nome:** Sara Catarina Loureiro da Silva  
- **Número de Aluno:** A104608  
<img src="../sarasilva.jpg" alt="Sara Silva" width="200" />

---

## 📖 Resumo
Este trabalho consistiu na implementação de um **simulador de máquina de venda automática** em Python, que permite ao utilizador interagir com a máquina através de comandos de texto.

A máquina suporta:

✅ **Listagem dos produtos** disponíveis com os respetivos preços e quantidades.  
✅ **Inserção de moedas** no sistema e acumulação de saldo.  
✅ **Seleção de produtos**, verificando disponibilidade e saldo.  
✅ **Receção de troco** corretamente no final da operação.  
✅ **Saída**, devolvendo o troco caso exista.  

O sistema utiliza um **ficheiro JSON (stock.json)** para guardar o stock dos produtos e processa diferentes comandos do utilizador.

---

## 📊 Funcionalidades

### 📌 **1. Listagem de Produtos**
O utilizador pode visualizar os produtos disponíveis na máquina, incluindo:
- **Código do produto**
- **Nome do produto**
- **Quantidade disponível**
- **Preço**

🖥 **Comando:**
```bash
LISTAR
```
🔹 Exemplo de Output:

```markdown
maq:
cod    |  nome         |  quantidade  |  preço
---------------------------------
A23    Água 0.5L      8             0.7€
B12    Sumo Laranja   5             1.2€
C34    Chocolate      3             1.5€
```

### 📌 2. Inserção de Moedas

O utilizador pode inserir moedas válidas:
💰 1e, 50c, 20c, 10c, 5c, 2c, 1c

🖥 Comando:

```bash
MOEDA 1E
MOEDA 50C
```

🔹 Exemplo de Output:

```makefile
maq: Saldo = 150c
```


### 📌 3. Seleção de Produto

Se o saldo for suficiente, o produto é dispensado. Caso contrário, o sistema alerta sobre saldo insuficiente.

🖥 Comando:

```bash
SELECIONAR A23
```

🔹 Exemplo de Output (Compra bem-sucedida):

```vbnet
Copiar
Editar
maq: Pode retirar o produto dispensado "Água 0.5L"
maq: Saldo = 80c
```
🔹 Exemplo de Output (Saldo insuficiente):

```makefile
maq: Saldo insuficiente para satisfazer o seu pedido
maq: Saldo = 80c; Pedido = 150c
```


### 📌 4. Sair e Receber Troco

Se houver saldo restante, o sistema devolve o troco corretamente.

🖥 Comando:

```bash
SAIR
```

🔹 Exemplo de Output:

```r
maq: Pode retirar o troco: 50c, 20c, 10c
maq: Até à próxima
```

### 🛠️ Execução

Para correr o programa, basta executar:

```bash
python vending.py
```

### 📎 Ficheiros
📜 vending.py - Código Python da máquina de venda automática.
📜 stock.json - Ficheiro JSON com o stock dos produtos.
📜 README.md - Documentação do trabalho.

