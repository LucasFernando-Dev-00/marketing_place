def layout():
    print('\n==BEM VINDO==')
    print('==NANDO LOJA EXPRESSA ONLINE==\n')
#layout do site//

def login():
    print('====LOGIN====\n')
    nome = input('Digite seu nome:\n').strip().lower()
    idade = int(input('Digite sua idade:\n'))
    senha = input('Digite sua senha:\n')
    print('====LOGIN CONCLUÍDO COM SUCESSO====\n')
    return nome, idade, senha
#login onde você guarda os seua dados na variáveis//

def verif():
    print('====LOGIN NA SUA CONTA====\n')
    log = input('Digite seu nome:\n').strip().lower()
    log1 = int(input('Digite sua idade:\n'))
    log2 = input('Digite sua senha:\n')
    return log, log1, log2
#verificação para ver se você colocou seus dados corretamente//

def pagnicial():
    print('\n====PÁGINA INICIAL====\n')
    print('0-Sair do Site')
    print('1-Ver saldo')
    print('2-Depositar dinheiro')
    print('3-Produtos Marketing Place\n')
#pagnicial onde você pode depositar dinheiro para comprar outros produtos//
    op = input('Digite uma opção:')
    return op

saldo = 0

def produtos():
    lista_produtos = ["1-Camisa Polo", "2-Blusa de Frio Preta", "3-Regata Preta", "4-Regata Branca", "5-Camisa de Time"]
    lista_precos = ["180,00", "370,00", "110,00", "110,00", "320,00"]

    for i in range(len(lista_produtos)):
        print(lista_produtos[i], '-' ,lista_precos[i])
    #este for exibe a lista na tela//


    compra = input('\nQual opção deseja levar:')

    return lista_produtos, lista_precos, compra

def compra_produtos(saldo, preco):

    qtde = float(input('Quantas deseja levar:\n'))

    valor = preco * qtde


    if valor > saldo:
        print("Saldo insuficiente...")
        print(f'Saldo: {saldo}')
        continuar_compra = input("Deseja continuar(s/n):").strip().lower()
                    
        if continuar_compra == 'n':
            print(f'Saldo: {saldo}')
            return False, saldo
        
        elif continuar_compra == 's':
            return True, saldo
        #se o saldo for insuficiente ai este bloco entra em ação, caso contário segue//

    saldo = saldo - valor
        #saldo subitraido pelo valor//

    print(f'Valor da Compra: {valor:.2f}')
        #valor da compra, se no cas ele quiser comprr mais eu tenho que somar valor + valor = valor total atual//
    print(f'Saldo: {saldo:.2f}')


    continuar_compr = input('\nDeseja continuar(s/n):').strip().lower()
            
    if continuar_compr == 'n':
        return False, saldo
                #logo abaixo vou dar um jeito dele entrar na pagina inicial já que ele não vai comprar mais//
    elif continuar_compr == 's':
        return True, saldo

layout()
nome, idade, senha = login()

while True:
    op = pagnicial()

    if op == '0':
        print('Saindo da Conta...')
        print('Voltando ao menu principal...\n')
        layout()
        log, log1, log2 = verif()
        while not (log == nome and log1 == idade and log2 == senha):
            print("LOGIN INVÁLIDO...")
            log, log1, log2 = verif()

        print('====ACESSO VALÍDO====\n')        

    elif op == '1':
        print(f'Saldo: R${saldo:.2f}\n')

    elif op == '2':
        adc = float(input('\nQuanto dinheiro você que adicionar a conta:\n'))
        saldo = saldo + adc
        print(f'\nO valor adicionado foi de R${adc:.2f}\nSeu saldo agora é de: R${saldo:.2f}\n')

    elif op == '3':
        while True:
            lista_produtos, lista_precos, compra = produtos()

            precos = {
            '1': 180.00,
            '2': 370.00,
            '3': 110.00,
            '4': 110.00,
            '5': 320.00
            }
            if compra not in precos:
                print('OPÇÃO INVÁLIDA!')
                continue

            preco = precos[compra]

            continuar, saldo = compra_produtos(saldo,preco)
            if not continuar:
                break