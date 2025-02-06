import controller
import datetime
import re

sumario = 'Digite o número correspondente para fazer a ação desejada:\n1 - Criar Torneio \n2 - Ver Torneios\n9 - Finalizar Gestor de Torneios\nDigite: '

def selecao_inicial(indice):
    try:   
        match indice:
            case 1:
                return cria_torneio()
            case 2:
                return lista_torneios()
            case 9:
                return print('Obrigado por utilizar o gestor de torneios! Até a próxima!')
            case 'retorno':
                selecao_inicial(int(input(f'\nDe volta a seleção incial!\n{sumario}')))
            case _:
                return selecao_inicial(int(input(f'Valor {indice} inválido\n{sumario}')))
    except:
        return #tratar exeção
        

def lista_torneios():
    def altera_torneio():
        return

    def deleta_torneio():
        return

    sumario_torneio = 'Digite o número correspondente para fazer a ação desejada:\n1 - Ver Partidas\n2 - Alterar Torneio \n3 - Excluir Torneio\n9 - Finalizar Gestor de Torneios\nDigite: '

    def selecao_torneio(indice):
        match indice:
            case 1:
                return print(lista_partidas(input('Digite o código do torneio: ')))
            case 2:
                return altera_torneio(input('Digite o código do torneio: '))
            case 3:
                return deleta_torneio()
            case 9:
                return print('Obrigado por utilizar o gestor de torneios! Até a próxima!')
            case _:
                return selecao_torneio(int(input(f'Valor {indice} inválido\n{sumario_torneio}')))
            
    
    selecao_torneio(int(input(sumario_torneio)))
    return selecao_inicial('retorno')

def cria_torneio():
    def tentar_novamente(tentar): 
        match tentar.upper():
            case 'S': 
                return cria_torneio()
            case 'N': 
                return print('Até a próxima e obrigado por usar o gestor de torneios!')
            case _:
                return tentar_novamente(input(f'Valor {tentar} inválido\nDigite S/N: '))

    def validaTimes(times):
        try:
            lista_de_times = list(map(int, times.split(' ')))
        except:
            return False
        return True

    def calcula_tier():
        return 'tier'

    try:
        nome = input('\nVamos criar um torneio! Para isso precisamos de algumas informações.\nQual o nome do seu torneio?\nDigite: ')
        #insert('torneios', 'nome', nome)
        
        contador = 0
        dataInvalida = True
        while dataInvalida:
            if contador >= 3:
                raise print('Data invália! Limite máximo de tentativas excedido')
            
            data_inicial = input('\nEm que data ele começa?\nDigite a data conforme o exemplo (01 01 2025): ')
            data_final = input('\nEm que data ele termina?\nDigite a data conforme o exemplo (01 01 2025): ')
            
            if re.match(controller.regexData, data_inicial):
                if re.match(controller.regexData, data_final):
                    dataInvalida = False
                else:
                    print("Data final em formado inválido!")
            else:
                print("Data inicial em formado inválido!")
            contador += 1

        contador = 0
        print(lista_organizadores())
        organizador = ''
        while organizador not in organizadores:
            if contador >= 3:
                raise print('Organizador inválido! Limite máximo de tentativas excedido')
            organizador = input('\nQual o organizador?\nDigite apenas o código: ')
            contador += 1
        
            
        contador = 0
        patrocinador = ''
        print(lista_patrocinadores())
        while patrocinador not in patrocinadores:
            if contador >= 3:
                raise print('Patrocinador Inválido! Limite máximo de tentativas excedido')
            patrocinador = input('\nPossui algum patrocinador?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nCaso não possua nenhum patrocinador, apenas deixe em branco\nDigite: ')
            contador += 1
        
        contador = 0
        regiao = ''
        print(lista_regioes())
        while regiao not in regioes:
            if contador >= 3:
                raise print('Região invália! Limite máximo de tentativas excedido')

            regiao = input('\nQual a região?\nDigite apenas o código: ')
            contador += 1      

        contador = 0
        inputTimes = '\nQuais são os times?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nDigite: '
        print(lista_times())
        while not(validaTimes(input(inputTimes))):
          if contador >= 3:
                raise print('Times inválidos! Limite máximo de tentativas excedido')
          validaTimes(input('\nVocê cometeu um erro ao digitar!\n'+inputTimes))  
          contador += 1

        #insert('torneios', 'data_inicial', data_inicial)
        #insert('torneios', 'data_final', data_final)
        #insert('torneios', 'organizador', organizador)
        #insert('torneios', 'patrocinador', patrocinador)
        #insert('torneios', 'data_final', data_final)
        #insert('torneios', 'tier', calcula_tier())

        controller.criar_partidas()
         
    except:
        tentar_novamente(input('Ocorreu um erro ao criar o seu torneio, deseja tentar novamente?\nDigite S/N: '))
        return
        
    print('Torneio criado com sucesso!')
    
    return selecao_inicial('retorno')



def lista_partidas(cod_torneio):
    return 'lista de partidas'

def lista_organizadores():
    global organizadores
    organizadores = ['teste']
    return 'lista de organizadores'

def lista_patrocinadores():
    global patrocinadores
    patrocinadores = ['teste']
    return 'lista de patrocinadores'

def lista_regioes():
    global regioes
    regioes = ['teste']
    return 'lista de regioes'

def lista_times():
    global times
    times = [1,2,3]
    return 'lista de times'

def listar_partidas():
    global partidas
    partidas = ['teste']
    return


selecao_inicial(int(input(f'Seja bem vindo ao gestor de torneios!\n{sumario}')))

