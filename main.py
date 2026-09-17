saldo_conta = 0
movimentacao = []

def registrar_receita(saldo, movimentacao, valor, descricao):

        if valor <= 0:
            print("Esse valor não pode ser adicionado como receita.")
        else:
            saldo += valor
            nova_movimentacao = {
            "tipo": "receita",
            "origem": descricao,
            "valor": valor
            }
            movimentacao.append(nova_movimentacao)
        return saldo

def registrar_despesa(saldo, movimentacao, valor, descricao):

    if valor <= 0:
        print("Valor inválido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        nova_movimentacao = {
        "tipo": "despesa",
        "destino": descricao,
        "valor": valor
        }
        movimentacao.append(nova_movimentacao)
    return saldo

def analise_financeira(movimentacao, saldo_conta):

    if not movimentacao:
        msg_erro = "Não teve movimentações para fazer uma análise."
        return msg_erro
    
    total_receitas = 0
    total_despesas = 0
    qtd_rec = 0
    qtd_des = 0
    percentual_despesas = "0%"
    resultado_financeiro = ""
    maior_despesa = None

    for item in movimentacao:
        if item["tipo"] == "receita":
            total_receitas += item["valor"]
            qtd_rec += 1
        elif item["tipo"] == "despesa":
            total_despesas += item["valor"]
            qtd_des += 1
            if maior_despesa is None or item["valor"] > maior_despesa:
                maior_despesa = item["valor"]
    if maior_despesa is None:
        maior_despesa = "Não teve despesas"

    if total_receitas > 0:
        porcentagem = total_despesas / total_receitas * 100
        percentual_despesas = f"{porcentagem:.2f}%"

    if saldo_conta > 0:
        resultado_financeiro = "POSITIVO"
    elif saldo_conta < 0:
        resultado_financeiro = "NEGATIVO"
    else:
        resultado_financeiro = "EQUILIBRADO"
    
    return{
        "total_receitas": total_receitas, 
        "total_despesas": total_despesas, 
        "saldo": saldo_conta, 
        "qtd_receitas": qtd_rec, 
        "qtd_despesas": qtd_des, 
        "maior_despesa": maior_despesa,
        "percentual_despesas": percentual_despesas,
        "resultado_financeiro": resultado_financeiro
    }

def formatacao_informacao(infor):
    if isinstance(infor, str):
        return infor

    if isinstance(infor["maior_despesa"], (int, float)):
        maior_despesa = f"R$ {infor['maior_despesa']:.2f}"
    else:
        maior_despesa = infor["maior_despesa"]
    
    formatacao = (f"""
        ========== ANÁLISE FINANCEIRA ==========
        | 
        | Total de receitas: R$ {infor["total_receitas"]:.2f}
        | Total de despesas: R$ {infor["total_despesas"]:.2f}
        | Saldo atual: R$ {infor["saldo"]:.2f}
        | 
        | Quantidade de receitas: {infor["qtd_receitas"]}
        | Quantidade de despesas: {infor["qtd_despesas"]}
        | 
        | Maior despesa: {maior_despesa}
        | Percentual de despesas: {infor["percentual_despesas"]}
        | Resultado financeiro: {infor["resultado_financeiro"]}
        =========================================
        """)
    return formatacao
        


while True:
    opcao = input("""
========== FINTRACK ==========
    0 - Sair
    1 - Registrar receita
    2 - Registrar despesa
    3 - Ver movimentações
    4 - Consultar saldo
    5 - Análise Financeira
===============================

--> """)

    if opcao == "0":
        print("""
===============================
      Programa encerrado
===============================""")
        break        

    elif opcao == "1":

        valor = input("Digite o valor da receita: ")
        print("\n")

        try:
            receita_atual = float(valor)

            origem = input("Descrição(fonte): ")

            saldo_conta = registrar_receita(saldo_conta, movimentacao, receita_atual, origem) 
        except ValueError:
            print("O valor que digitou é invalido. Tente novamente.") 
        
    elif opcao == "2":

        valor = input("Digite o valor da despesa: ")
        print("\n")
        
        try:
            despesa_atual = float(valor)
        
            destino = input("Descrição(destino): ")
        
            saldo_conta = registrar_despesa(saldo_conta, movimentacao, despesa_atual, destino)

                    
        except ValueError:
            print("O valor que digitou é invalido. Tente novamente.")
        
    elif opcao == "3":
        print("""
================== MOVIMENTAÇÃO =====================
""")
        if not movimentacao:
            retorno = "Não teve movimentações até o momento."
            print(retorno)
        else:
            print(movimentacao)

    elif opcao == "4":
        print(f"Saldo: {saldo_conta}")

    elif opcao == "5":
        informacao = analise_financeira(movimentacao, saldo_conta)
        exibir = formatacao_informacao(informacao)
        print(exibir)

    else:
        print("Opçao inválida.")    