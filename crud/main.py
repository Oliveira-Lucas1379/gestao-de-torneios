import controller
import datetime
import re

sumario = 'Digite o número correspondente para fazer a ação desejada:\n1 - Criar Torneio \n2 - Ver Torneio\n9 - Finalizar Gestor de Torneios\nDigite: '


def selecao_inicial(indice):
    match indice:
        case 1:
            return cria_torneio()
        case 2:
            return ver_torneio()
        case 9:
            return print('Obrigado por utilizar o gestor de torneios! Até a próxima!')
        case 'retorno':
            selecao_inicial(int(input(f'\nDe volta a seleção incial!\n{sumario}')))
        case _:
            return init(True)

def ver_torneio():
    def altera_torneio(cod_torneio):
        return

    def deleta_torneio(cod_torneio):
        return

    sumario_torneio = 'Digite o número correspondente para fazer a ação desejada:\n1 - Ver Partidas\n2 - Alterar Torneio \n3 - Excluir Torneio\n9 - Finalizar Gestor de Torneios\nDigite: '

    print(f'\nEstes sãos os torneios já cadastrados:\n{lista_torneios()}')
    def selecao_torneio(indice):
        match indice:
            case 1:
                return print(f'\nEstas são as partidas do torneio:\n{lista_partidas(input("Digite o código do torneio: "))}')
            case 2:
                return altera_torneio(input('Digite o código do torneio: '))
            case 3:
                return deleta_torneio(input('Digite o código do torneio: '))
            case 9:
                return print('Obrigado por utilizar o gestor de torneios! Até a próxima!')
            case _:
                return selecao_torneio(int(input(f'Valor {indice} inválido\n{sumario_torneio}')))                
    try:
        selecao_torneio(int(input(sumario_torneio)))
    except:
        selecao_torneio(int(input(f'\nValor inválido!\n{sumario_torneio}')))

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
        while True:
            if contador >= 3:
                raise print('Organizador inválido! Limite máximo de tentativas excedido')
            organizador = int(input('\nQual o organizador?\nDigite apenas o código: '))
            contador += 1
            if any(tupla[0] == organizador for tupla in organizadores):
                break
        
            
        contador = 0
        patrocinador = ''
        print(lista_patrocinadores())
        existe = False
        while not existe:
            if contador >= 3:
                raise print('Patrocinador Inválido! Limite máximo de tentativas excedido')
            patrocinador = input('\nPossui algum patrocinador?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nCaso não possua nenhum patrocinador, apenas deixe em branco\nDigite: ')
            patrocinadorCod = patrocinador.split("/")
            contador += 1
            existe = True
            for patrocinador in patrocinadorCod:
                if not any(tupla[0] == patrocinador for tupla in patrocinadores):
                    existe = False
                    break

        
        contador = 0
        regiao = ''
        print(lista_regioes())
        while True:
            if contador >= 3:
                raise print('Região invália! Limite máximo de tentativas excedido')

            regiao = input('\nQual a região?\nDigite apenas o código: ')
            contador += 1   
            if any(tupla[0] == regiao for tupla in regioes):
                break   

        contador = 0
        inputTimes = '\nQuais são os times?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nDigite: '
        print(lista_times())
        while not(validaTimes(input(inputTimes))):
          if contador >= 3:
                raise print('Times inválidos! Limite máximo de tentativas excedido')
          validaTimes(input('\nVocê cometeu um erro ao digitar!\n'+inputTimes))  
          contador += 1
        
        controller.criar_partidas()
        #insert('torneios', 'nome', nome)
        #insert('torneios', 'data_inicial', data_inicial)
        #insert('torneios', 'data_final', data_final)
        #insert('torneios', 'organizador', organizador)
        #insert('torneios', 'patrocinador', patrocinador)
        #insert('torneios', 'data_final', data_final)
        #insert('torneios', 'tier', calcula_tier())
        
    except:
        tentar_novamente(input('Ocorreu um erro ao criar o seu torneio, deseja tentar novamente?\nDigite S/N: '))
        return
        
    print('Torneio {nome} criado com sucesso!')
    
    return selecao_inicial('retorno')



def lista_torneios():
    global torneios
    torneios = ['teste']
    return torneios

def lista_partidas(cod_torneio):
    global partidas
    partidas = ['teste']
    return partidas

def lista_organizadores():
    global organizadores
    viewOrganizadores = f"\n\nOrganizadores: \n Codigo    |    NOME\n"
    organizadores = controller.get_all("organizadores", ["*"])
    viewOrganizadores += "\n".join(f" {o[0]}    -    {o[1]}" for o in organizadores) + "\n"
    return viewOrganizadores

def lista_patrocinadores():
    global patrocinadores
    patrocinadores = controller.get_all("patrocinadores", ["*"])
    viewPatrocinadores = f"\n\Patrocinadores: \n CODIGO    |        NOME         |        ORIGEM      \n"
    viewPatrocinadores += "\n".join(f" {p[0]}     -     {p[1]} -    {p[2]}" for p in patrocinadores) + "\n"
    return viewPatrocinadores

def lista_regioes():
    global regioes
    regioes = controller.get_all("regiao", ["*"])
    viewRegioes = f"\n\nRegioes: \n CODIGO   |        NOME         |          LOCALIZACAO     \n"
    viewRegioes += "\n".join(f"{r[0]}    -      {r[1]}       -        {r[2]}" for r in regioes)
    return viewRegioes

def lista_times():
    global times
    times = controller.get_all("times", ["codtime", "nome"])
    viewTimes = f"\n\Times: \n CODIGO   |        NOME\n"
    viewTimes += "\n".join(f"{t[0]}    -      {t[1]}" for t in times)
    return viewTimes

def init(erro):
    if erro:
        try:
            selecao_inicial(int(input(f'\nValor inválido!\n{sumario}')))
        except:
            selecao_inicial(int(input(f'\nValor inválido!\n{sumario}')))
    else:
        try:
            selecao_inicial(int(input(f'Seja bem vindo ao gestor de torneios!\n{sumario}')))
        except:
            selecao_inicial(int(input(f'\nValor inválido!\n{sumario}')))

print(lista_organizadores())
init(False)
