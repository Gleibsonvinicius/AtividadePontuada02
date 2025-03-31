import os

os.system ("cls||clear")



menu = {
    1: ("Lasanha", 20.00),
    2: ("Strogonoff", 25.00),
    3: ("Pizza Grande", 30.00),
    4: ("Bife", 15.00),
    5: ("Muqueca", 18.00),
    6: ("X-Burguer", 22.00),
    7: ("Batata frita", 27.00),

}


pedidos = input
valor_total = 0.0


print("Menu de Pratos:")
for codigo, (nome, preco) in menu.items():
    print(f"Código: {codigo}, Nome: {nome}, Preço: R$ {preco:.2f}")


while True:
    codigo = int(input("Digite o código do prato desejado (ou 0 para finalizar): "))
    
    if codigo == 0:
        break
    
    if codigo in menu:
        pedidos += (menu[codigo],)  
        valor_total += menu[codigo][1]
        print(f"Prato {menu[codigo][0]} adicionado ao pedido.")
    else:
        print("Código inválido. Tente novamente.")

   
    continuar = input("Deseja adicionar mais pratos? (s/n): ")
    if continuar != 's':
        break


while True:
    forma_pagamento = input("Escolha a forma de pagamento (1 - À vista, 2 - Cartão de crédito): ")
    
    match forma_pagamento:
        case '1':
            desconto = valor_total * 0.10
            valor_final = valor_total - desconto
            tipo_pagamento = "À vista"
            break
        case '2':
            acrescimo = valor_total * 0.10
            valor_final = valor_total + acrescimo
            tipo_pagamento = "Cartão de crédito"
            break
        case _:
            print("Forma de pagamento inválida. Tente novamente.")


print("\nResumo do Pedido:")
for prato in pedidos:
    print(f"Prato: {prato[0]}, Preço: R$ {prato[1]:.2f}")

print(f"Subtotal: R$ {valor_total:.2f}")
print(f"Forma de pagamento: {tipo_pagamento}")

if forma_pagamento == '1':
    print(f"Desconto aplicado: R$ {desconto:.2f}")
else:
    print(f"Acréscimo aplicado: R$ {acrescimo:.2f}")

print(f"Valor final a ser pago: R$ {valor_final:.2f}")