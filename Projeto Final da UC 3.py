#banco de estoque😔✌️
estoque = {
    1: {"nome": "tokyo ghoul cap 1", "preco": 50.00, "quantidade":10 },
    2: {"nome": "bleach cap 24", "preco": 59.90, "quantidade":5 },
    3: {"nome": "jujutsu kaisen cap 9", "preco": 35.32, "quantidade":4 },
    4: {"nome": "shingeki no kyojin cap 33", "preco": 55.00, "quantidade":15 },
}
carrinho = []

def visualizar_estoque():
    print("\n===== ESTOQUE =====")
    print(f"{'ID':<5}{'Nome':<30}{'Preço(R$)':<15}{'Quantidade'}")

    for id_produto, produto in estoque.items():
        print(
            f"{id_produto:<5}"
            f"{produto['nome']:<30}"
            f"R${produto['preco']:<13.2f}"
            f"{produto['quantidade']}"
        )


def adicionar_carrinho():

    visualizar_estoque()

    try:
        id_produto = int(input("\nDigite o ID do produto: "))
        quantidade = int(input("Digite a quantidade: "))

    except ValueError:
        print("Digite apenas números.")
        return

    if id_produto not in estoque:
        print("Produto inexistente.")
        return

    if quantidade <= 0:
        print("Quantidade inválida.")
        return

    if quantidade > estoque[id_produto]["quantidade"]:
        print("Estoque insuficiente.")
        return

    produto = estoque[id_produto]

    encontrado = False

    for item in carrinho:
        if item["id"] == id_produto:
            item["quantidade"] += quantidade
            encontrado = True
            break

    if not encontrado:
        carrinho.append({
            "id": id_produto,
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": quantidade
        })

    estoque[id_produto]["quantidade"] -= quantidade

    print("Item adicionado ao carrinho.")


def visualizar_carrinho():

    if len(carrinho) == 0:
        print("\nCarrinho vazio.")
        return

    subtotal = 0

    print("\n===== CARRINHO =====")

    for item in carrinho:

        total_item = item["preco"] * item["quantidade"]
        subtotal += total_item

        print(
            f"{item['nome']} | "
            f"Qtd: {item['quantidade']} | "
            f"Unit: R${item['preco']:.2f} | "
            f"Total: R${total_item:.2f}"
        )

    print(f"\nSubtotal: R${subtotal:.2f}")


def devolver_estoque():

    for item in carrinho:
        estoque[item["id"]]["quantidade"] += item["quantidade"]


def finalizar_compra():

    if len(carrinho) == 0:
        print("Carrinho vazio.")
        return

    subtotal = 0

    for item in carrinho:
        subtotal += item["preco"] * item["quantidade"]

    cupom = input(
        "\nDigite um cupom (ENTER para ignorar): "
    ).upper()

    desconto = 0

    if cupom == "DEV10":
        desconto = subtotal * 0.10

    elif cupom == "DEV20":
        if subtotal > 500:
            desconto = subtotal * 0.20
        else:
            print("DEV20 disponível apenas acima de R$500.")

    elif cupom != "":
        print("Cupom inválido.")

    total = subtotal - desconto

    print("\n===== RESUMO DO PEDIDO =====")
    print(f"Subtotal: R${subtotal:.2f}")
    print(f"Desconto: R${desconto:.2f}")
    print(f"Total a pagar: R${total:.2f}")

    confirmar = input(
        "\nConfirmar pagamento? (S/N): "
    ).upper()

    if confirmar == "S":
        carrinho.clear()
        print("Compra finalizada com sucesso!")

    elif confirmar == "N":
        devolver_estoque()
        carrinho.clear()
        print("Compra cancelada e estoque restaurado.")

    else:
        print("Opção inválida.")



# MENU 😝

while True:

    print("""
===== MENU ✌️😔 =====

[1] Visualizar Estoque
[2] Adicionar Item ao Carrinho
[3] Visualizar Carrinho
[4] Finalizar Compra
[0] Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        visualizar_estoque()

    elif opcao == "2":
        adicionar_carrinho()

    elif opcao == "3":
        visualizar_carrinho()

    elif opcao == "4":
        finalizar_compra()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
