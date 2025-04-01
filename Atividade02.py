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

subtotal = 0.0


print("Menu de Pratos:")
for codigo, (nome, preco) in menu.items():
    print(f"{codigo} - {nome} - R$ {preco:.2f}")
print("0 - Finalizar pedido")

while True:
    codigo = input("Digite o código do prato desejado: ")

    if codigo == "0":
        break
    codigo_int = int(codigo)  
    if codigo_int in menu:  
        prato, preco = menu[codigo_int]
        subtotal += preco
        print(f"{prato} adicionado ao pedido.")
    else:
        print("Código inválido. Tente novamente.")

forma_pagamento = input("Escolha a forma de pagamento (1 para à vista / 2 para cartão de crédito): ")


if forma_pagamento == "1":  
    desconto = subtotal * 0.10  
    valor_final = subtotal - desconto
    forma_pagamento_desc = "à vista"
    ajuste_desc = f"Desconto aplicado: R$ {desconto:.2f}"
elif forma_pagamento == "2":  
    ajuste = subtotal * 0.10  
    valor_final = subtotal + ajuste
    forma_pagamento_desc = "cartão de crédito"
    ajuste_desc = f"Acréscimo aplicado: R$ {ajuste:.2f}"
else:
    ajuste = 0
    valor_final = subtotal  
    forma_pagamento_desc = "inválida"



print("\nResumo do Pedido:")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Forma de pagamento: {forma_pagamento_desc}")
if ajuste_desc:
    print(ajuste_desc)
print(f"Valor final a ser pago: R$ {valor_final:.2f}")