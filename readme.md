# Sistema Bancário Simples em Python

Este é um projeto de um sistema bancário simples desenvolvido em Python. O projeto foi criado como parte do bootcamp "Backend Python" da [Digital Innovation One (DIO)](https://www.dio.me/).

O sistema simula operações bancárias básicas através de uma interface de linha de comando (CLI), permitindo que o usuário interaja com uma conta fictícia.

## ✨ Funcionalidades

O sistema permite realizar as seguintes operações:

1.  **[1] Depositar:** Permite ao usuário adicionar um valor positivo ao saldo da conta.
2.  **[2] Sacar:** Permite ao usuário retirar um valor da conta, sujeito às seguintes regras:
    *   O valor do saque não pode exceder o saldo disponível.
    *   Existe um limite de **R$ 500,00** por saque.
    *   O usuário pode realizar no máximo **3 saques**.
3.  **[3] Extrato:** Exibe todas as transações (depósitos e saques) realizadas e o saldo atual da conta.
4.  **[0] Sair:** Encerra a aplicação.

## 🛠️ Como Executar

Para rodar este projeto, você precisa ter o Python 3 instalado em sua máquina.

1.  Clone ou faça o download do arquivo `app.py`.
2.  Abra o seu terminal (Prompt de Comando, PowerShell, etc.).
3.  Navegue até o diretório onde você salvou o arquivo.
4.  Execute o script com o seguinte comando:

    ```bash
    python app.py
    ```
5.  Siga as instruções apresentadas no menu do terminal.

## 🧠 Conceitos de Python Praticados

Este projeto foi uma oportunidade para praticar:

-   **Variáveis e Tipos de Dados:** Utilização de `int`, `float` e `str` para armazenar saldo, valores de transações e o extrato.
-   **Constantes:** Definição de valores fixos como `LIMITE_SAQUES`.
-   **Entrada e Saída de Dados:** Interação com o usuário através de `input()` e `print()`.
-   **Estruturas Condicionais:** Uso de `if`, `elif` e `else` para controlar o fluxo do programa com base nas escolhas do usuário e nas regras de negócio.
-   **Estruturas de Repetição:** Emprego do laço `while` para manter o programa em execução até que o usuário decida sair.
-   **Formatação de Strings:** Uso de f-strings para formatar a exibição de valores monetários e o extrato.
-   **Módulos:** Importação e uso do módulo `os` para limpar a tela e pausar a execução, melhorando a experiência do usuário no terminal.

