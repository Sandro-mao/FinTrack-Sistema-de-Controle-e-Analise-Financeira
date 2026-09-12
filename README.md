# 💰 FinTrack — Sistema de Controle e Análise Financeira

O **FinTrack** é um projeto desenvolvido em Python com o objetivo de praticar conceitos de programação aplicados a um cenário financeiro.

A proposta é construir o sistema de forma evolutiva, começando com um controle financeiro básico e, posteriormente, adicionando recursos de análise e uma estrutura utilizando Programação Orientada a Objetos (POO).

---

## 🎯 Objetivo do Projeto

O FinTrack será desenvolvido em **3 etapas**, permitindo acompanhar a evolução do projeto desde os fundamentos da programação até uma estrutura mais organizada e orientada a objetos.

### Etapa 1 — Núcleo Financeiro

Construção da primeira versão funcional do sistema utilizando os fundamentos de Python:

- Variáveis
- Entrada e saída de dados
- Estruturas condicionais
- Estruturas de repetição
- Listas
- Dicionários
- Tratamento de exceções
- Operadores matemáticos

### Etapa 2 — Análise Financeira

A segunda versão terá como objetivo transformar os dados registrados em informações úteis para análise financeira.

Serão adicionados recursos como:

- Total de receitas
- Total de despesas
- Saldo financeiro
- Maior despesa
- Análise das movimentações
- Indicadores financeiros

### Etapa 3 — Programação Orientada a Objetos

Na terceira versão, o sistema será reorganizado utilizando conceitos de POO estudados durante o desenvolvimento.

Serão aplicados:

- Classes e objetos
- Atributos e métodos
- Encapsulamento
- Herança
- Polimorfismo
- Classes abstratas

---

# 🚀 Versão 1.0 — Núcleo Financeiro

A primeira versão do FinTrack tem como objetivo criar a base do sistema e permitir o registro e controle das movimentações financeiras.

## Funcionalidades

### 💵 Registrar Receita

Permite registrar uma entrada de dinheiro informando:

- Valor da receita
- Descrição da fonte da receita

Exemplos:

- Salário
- Uber
- Venda de produto
- Freelance
- Reembolso

### 💸 Registrar Despesa

Permite registrar uma saída de dinheiro informando:

- Valor da despesa
- Descrição do destino da despesa

Exemplos:

- Mercado
- Combustível
- Faculdade
- Internet
- Parcela de veículo

O sistema também verifica se:

- O valor é maior que zero
- Existe saldo suficiente para realizar a despesa

### 📋 Ver Movimentações

Exibe todas as receitas e despesas registradas durante a execução do programa.

Cada movimentação contém informações como:

- Tipo
- Origem ou destino
- Valor

### 💰 Consultar Saldo

Permite consultar o saldo atual da conta após as movimentações realizadas.

### 🚪 Encerrar Sistema

Permite sair do sistema através do menu principal.

---

## 🖥️ Menu Atual

```text
========== FINTRACK ==========

    1 - Registrar receita
    2 - Registrar despesa
    3 - Ver movimentações
    4 - Consultar saldo
    5 - Sair

===============================
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