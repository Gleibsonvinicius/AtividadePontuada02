import os


os.system("cls||clear")


menu = {
    1: ("Lasanha", 20.00),
    2: ("Strogonoff", 25.00),
    3: ("Pizza Grande", 30.00),
    4: ("Bife", 15.00),
    5: ("Muqueca", 18.00),
    6: ("X-Burguer", 22.00),
    7: ("Batata frita", 27.00),
}

pedidos = [] # o colchete que eu utilizei foi pra criar uma lista com elementos no caso lasanha , pizza , X burger , etcs
total = 0.0

while True:
    print("\nMenu de Pratos:")
    for codigo, (nome, preco) in menu.items():
        print(f"Código: {codigo}, Nome: {nome}, Preço: R${preco:.2f}")

   
    try:
        codigo_pedido = int(input("Digite o código do prato desejado (ou '0' para finalizar): "))
    except ValueError:
        print("Código inválido. Tente novamente.")
        continue

    match codigo_pedido:
        case 0:
            break
        case _ if codigo_pedido in menu:
            pedidos.append(menu[codigo_pedido])  
            total += menu[codigo_pedido][1]      
            print(f"Você adicionou {menu[codigo_pedido][0]} ao seu pedido.")
        case _:
            print("Código inválido. Tente novamente.")

    
    continuar = input("Deseja fazer outro pedido? (s/n): ")
    if continuar.lower() != 's':
        break


if pedidos:
    forma_pagamento = input("Escolha a forma de pagamento (1 - À vista, 2 - Cartão de crédito): ")
    desconto_acrescimo = 0.0

    match forma_pagamento:
        case "1":
            desconto_acrescimo = total * 0.10 
            total -= desconto_acrescimo
            forma_pagamento_str = "À vista"
        case "2":
            desconto_acrescimo = total * 0.10  
            total += desconto_acrescimo
            forma_pagamento_str = "Cartão de crédito"
        case _:
            print("Forma de pagamento inválida. Considerando à vista por padrão.")
            desconto_acrescimo = total * 0.10  
            total -= desconto_acrescimo
            forma_pagamento_str = "À vista"

    
    print("\nResumo do Pedido:")
    for prato in pedidos:
        print(f"{prato[0]} - R${prato[1]:.2f}")

    print(f"Subtotal: R${sum(preco for _, preco in pedidos):.2f}")
    print(f"Forma de pagamento: {forma_pagamento_str}")
    print(f"Desconto ou acréscimo: R${desconto_acrescimo:.2f}")
    print(f"Total a pagar: R${total:.2f}")
else:
    print("Nenhum pedido foi realizado.")
