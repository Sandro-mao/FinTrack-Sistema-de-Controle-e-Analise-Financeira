# 💰 FinTrack — Sistema de Controle e Análise Financeira

O **FinTrack** é um projeto desenvolvido em Python com o objetivo de praticar conceitos de programação aplicados a um cenário financeiro real.

O sistema está sendo construído de forma evolutiva, passando por diferentes etapas de complexidade até chegar em uma estrutura orientada a objetos.

---

## 📌 Status do Projeto

- ✅ **Etapa 1 — Núcleo Financeiro** → Concluída com sucesso  
- ✅ **Etapa 2 — Análise Financeira** → Concluída com sucesso  
- ⏳ **Etapa 3 — Programação Orientada a Objetos** → Em breve

---

## 🚀 Versão 2.0 — Análise Financeira

Nesta versão, o sistema foi reorganizado com o uso de **funções** e ganhou recursos de análise financeira.

### Funcionalidades

- **Registrar Receita**  
  Adiciona entradas de dinheiro com valor e descrição da fonte.

- **Registrar Despesa**  
  Registra saídas de dinheiro com validação de valor positivo e saldo suficiente.

- **Ver Movimentações**  
  Exibe todas as receitas e despesas registradas.

- **Consultar Saldo**  
  Mostra o saldo atual da conta.

- **Análise Financeira**  
  Gera um relatório com:
  - Total de receitas e despesas
  - Quantidade de cada tipo de movimentação
  - Maior despesa
  - Percentual de despesas sobre as receitas
  - Resultado financeiro (Positivo / Negativo / Equilibrado)

### Menu Atual

```text
========== FINTRACK ==========
    0 - Sair
    1 - Registrar receita
    2 - Registrar despesa
    3 - Ver movimentações
    4 - Consultar saldo
    5 - Análise Financeira
===============================
```
### Exemplo de Análise Financeira

```text
========== ANÁLISE FINANCEIRA ==========
| 
| Total de receitas: R$ 3500.00
| Total de despesas: R$ 1200.50
| Saldo atual: R$ 2299.50
| 
| Quantidade de receitas: 2
| Quantidade de despesas: 3
| 
| Maior despesa: R$ 600.00
| Percentual de despesas: 34.30%
| Resultado financeiro: POSITIVO
=========================================
```

## 🗂️ Estrutura dos Dados

As movimentações são armazenadas utilizando uma lista de dicionários.

```text
Exemplo de uma receita:

{
    "tipo": "receita",
    "origem": "Salário",
    "valor": 2500.00
}

Exemplo de uma despesa:

{
    "tipo": "despesa",
    "destino": "Combustível",
    "valor": 150.00
}
```

### 🛠️ Tecnologias

* Python
* Git
* GitHub
* Visual Studio Code

### 📌 Evolução do Projeto

O desenvolvimento será registrado através de commits, mostrando a evolução do sistema:

Commit 1 — Núcleo do FinTrack

Implementação do controle financeiro básico, incluindo registro de receitas, despesas, movimentações e consulta de saldo.

Commit 2 — Análise Financeira

Adição de recursos para transformar as movimentações registradas em informações e indicadores financeiros.

Commit 3 — Aplicação de POO

Reestruturação do sistema utilizando Programação Orientada a Objetos.

## 📚 Objetivo de Aprendizado

Este projeto está sendo desenvolvido como prática dos conhecimentos adquiridos em Python, buscando transformar conceitos teóricos em uma aplicação prática relacionada ao mercado financeiro.

O projeto também servirá como parte do meu portfólio de desenvolvimento na área de Dados, IA e Mercado Financeiro.

### 👨‍💻 Autor

Alessandro Souza da Silva

[LinkedIn](https://www.linkedin.com/in/alessandro--souza/) • [GitHub](https://github.com/Sandro-mao)