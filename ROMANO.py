#NÚMERO ROMANO

#definindo qual converção será feita
def romano_or_numeral():
    num=0
    while (num!=1) and (num!=2):
        num=int(input('Escolha a opção: \n \n 1- ROMANO PARA DECIMAL \n 2- DECIMAL PARA ROMANO \n \n Ditige 1 ou 2: ' ))
        print('')

        #mensagem de escolha inválida
        if (num!=1) and (num!=2):
            print('Número inválido, digite novamente.')
            print('')

    #direcionamento para a converção de romano para numeral
    if num==1:
        geral_romano()

    #direcionamento para a converção de numeral para romano
    else:
        geral_numeral()

# FUNÇÃO GERAL DE CONVERÇÃO NUMERAL_ROMANO
def geral_numeral():
    
    #chamando funcão que recebe e valida o número 
    num=prepara_numerico()
    lista_numero=converte_numerico(num)
    convercao=soma_lista(lista_numero,2)
    print('')
    print(f'O número {num} em númerico é {convercao}')

# FUNÇÃO GERAL DE CONVERÇÃO ROMANO_NUMERAL
def geral_romano():
    
    #chamando funcão que recebe e prepara os números romanos para a converção 
    lista, romano = prepara_romano()

    #função converte de romano para decimal
    lista= converte_romano(lista)

    #soma os valores da lista
    convercao= soma_lista(lista,1)

    print('')
    print(f'O número romano {romano} em númerico é {convercao}')

#RECEBENDO E PREPARANDO NUMERO ROMANO
def prepara_romano():
    lista=[]

    #PEGANDO O NÚMERO ROMANO
    y=str(input('Digite um número romano: '))
    print('')
    y=y.upper()

    #VERIFICANDO SE O NÚMERO É VALIDO, SE VALIDO: SEPARA CADA NUMERO EM UMA LISTA PARA CONVERÇÃO
    for i in y:
        if i!='I' and i!='V' and i!='X' and i!='L' and i!='C' and i!='D' and i!='M':
            print('Número romano inválido.')
            print('')
            prepara_romano()
        lista.append(i)
    return lista, y

#CONVERTENDO NUMERO ROMANO
def converte_romano(lista):
    convercao=[]
    #contador de indice da lista
    for i in range(0,len(lista)-1):
        # verificando se o item já foi executado ou não
        if lista[i]!=0:

            #VERIFICANDO I
            if lista[i]=='I':
                # se houver V depois registrar 4 
                if lista[i+1]=='V':
                    convercao.append(4)
                    lista[i+1]=0

                # se houver X depois registrar 9 
                elif lista[i+1]=='X':
                    convercao.append(9)
                    lista[i+1]=0
                # se nao houver V nem X depois, registrar 1
                else:
                    convercao.append(1)

            #VERIFICANDO V
            elif lista[i]=='V':
                    convercao.append(5)

            #VERIFICANDO X     
            if lista[i]=='X':
                if lista[i+1]=='L':
                    convercao.append(40)
                    lista[i+1]=0
                elif lista[i+1]=='C':
                    convercao.append(90)
                    lista[i+1]=0
                else:
                    convercao.append(10)

            #VERIFICANDO L
            elif lista[i]=='L':
                    convercao.append(50)

            #VERIFICANDO C    
            if lista[i]=='C':
                if lista[i+1]=='D':
                    convercao.append(400)
                    lista[i+1]=0
                elif lista[i+1]=='M':
                    convercao.append(900)
                    lista[i+1]=0
                else:
                    convercao.append(100)

            #VERIFICANDO L
            elif lista[i]=='D':
                    convercao.append(500)

            #VERIFICANDO L
            elif lista[i]=='M':
                        convercao.append(1000)
    return convercao

#SOMANDO OS NUMEROS DA LISTA 
def soma_lista(lista,x):
    if x==1:
        soma=0
        for i in lista:
            soma=soma+i
        return soma
    else:
        soma=''
        for i in lista:
            soma=soma+i
        return soma

#RECEBENDO O NÚMERO
def prepara_numerico():
    
    #PEGANDO O NÚMERO e verificando se ele é válido 
    y=-1
    while y<0:
        y=int(input('Digite um número inteiro positivo: '))
        #mensagem de aviso se o numero for inválido
        if y<0:
            print('')
            print('Número negativo, por favor digite novamente')
            print('')
    print('')
    return y

#CONVERTE NUMERO PARA ROMANO
def converte_numerico(num):
    lista_numero=[]
    while num!=0:
        if (num//1000)!=0:
            lista_numero.append('M')
            num=num-1000

        elif (num//900)!=0:
            lista_numero.append('CM')
            num=num-900

        elif (num//500)!=0:
            lista_numero.append('D')
            num=num-500

        elif (num//400)!=0:
            lista_numero.append('CD')
            num=num-400

        elif (num//100)!=0:
            lista_numero.append('C')
            num=num-100

        elif (num//90)!=0:
            lista_numero.append('XC')
            num=num-90

        elif (num//50)!=0:
            lista_numero.append('L')
            num=num-50

        elif (num//40)!=0:
            lista_numero.append('XL')
            num=num-40

        elif (num//10)!=0:
            lista_numero.append('X')
            num=num-10

        elif (num//9)!=0:
            lista_numero.append('IX')
            num=num-9
        
        elif (num//5)!=0:
            lista_numero.append('V')
            num=num-5
        
        elif (num//4)!=0:
            lista_numero.append('IV')
            num=num-4

        elif (num//1)!=0:
            lista_numero.append('I')
            num=num-1
        
    return lista_numero   

#http://www.climaat.angra.uac.pt/produtos/calculadoras/numeros_romanos.htm

romano_or_numeral()
