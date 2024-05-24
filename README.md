# Desafio: Criando um Sistema Bancário

## Versão 1
### Objetivo Geral

- Criar um sistema bancário com as operações: <i>sacar</i>, <i>depositar</i> e <i>visualizar extrato</i>.

### Regras
- <b>Operação de depósito:</b> Deve ser possível depositar valores positivos para a conta bancária, na primeira versão o projeto trabalha apenas com um usuário, sem precisar se preocupar no momento com identificação de número de agência e conta. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
- <b>Operação de saque:</b> O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00. Caso o usuário não tenha saldo em conta, deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
- <b>Operação de extrato:</b> O sistema deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve exibir o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$xxx,xx.

## Versão 2
### Objetivo Geral

- Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: <i>sacar</i>, <i>depositar</i> e <i>visualizar extrato</i>. Criar duas novas funções: <i>cadastrar usuário</i> e <i>cadastrar conta bancária</i>.

### Regras

- <b>Separando em Funções:</b> Criar funções para todas as operações do sistema, para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas pode ser definida livremente.
    - <b>Saque</b>: Essa função deve receber os argumentos apenas por nome (keyword only).
    - <b>Depósito:</b> Essa função deve receber os argumentos apenas por posição (positional only). 
    - <b>Extrato:</b> Essa função deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo. Argumentos nomeados: extrato.

- <b>Novas Funções:</b> Precisamos criar duas novas funções: <i>criar usuário</i> e <i>criar conta corrente</i>.
    - <b>Criar Usuário:</b> O programa deve armazenar o usuário em uma lista, sendo ele composto por: nome, data de nascimento, cpf e endereço. O endereço precisa ser uma string com formato: "Logradouro, nro - Bairro - Cidade/Sigla Estado". Armazenar apenas o número do CPF, sem caracteres especiais, como tipo string. Não pode ser possível cadastrar dois usuários com o mesmo CPF.
    - <b>Criar Conta Corrente:</b> O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
