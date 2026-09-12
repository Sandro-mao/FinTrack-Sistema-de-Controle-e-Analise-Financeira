saldo_conta = 0
movimentacao = []

while True:
    opcao = input("""
========== FINTRACK ==========
    1 - Registrar receita
    2 - Registrar despesa
    3 - Ver movimentações
    4 - Consultar saldo
    5 - Sair
===============================

--> """)

    if opcao == "1":
        tipo = "receita"
        valor = input("Digite o valor da receita: ")
        print("\n")      
   
        try:
            receita_atual = float(valor)
 
            if receita_atual <= 0:
                print("Esse valor não pode ser adicionado como receita.")
            else:
                origem = input("Descrição(fonte): ")
                saldo_conta += receita_atual
                nova_movimentacao = {
                "tipo": tipo,
                "origem": origem,
                "valor": receita_atual
                }
                movimentacao.append(nova_movimentacao)     
        except ValueError:
            print("O valor que digitou é invalido. Tente novamente.")
            
    elif opcao == "2":
        tipo = "despesa"
        valor = input("Digite o valor da despesa: ")
        print("\n")
        
        try:
            despesa_atual = float(valor)

            if despesa_atual <= 0:
                print("Valor inválido.")

            elif despesa_atual > saldo_conta:
                print("Saldo em conta insuficiente.")

            else:
                destino = input("Descrição(destino): ")
                saldo_conta -= despesa_atual
                nova_movimentacao = {
                    "tipo": tipo,
                    "destino": destino,
                    "valor": despesa_atual
                }
                movimentacao.append(nova_movimentacao)
        except ValueError:
            print("O valor que digitou é invalido. Tente novamente.")

    elif opcao == "3":
        print("""
================== MOVIMENTAÇÃO =====================
""")
        for item in movimentacao:
            print(item)
    elif opcao == "4":
        print(f"Saldo: {saldo_conta}")
    elif opcao == "5":
        break
    else:
        print("Opção inválida")