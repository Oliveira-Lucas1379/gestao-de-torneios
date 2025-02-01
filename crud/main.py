sumario = 'Digite o número correspondente para fazer a ação desejada:\n1 - Criar Torneio \n2 - Ver Torneios\n9 - Finalizar Gestor de Torneios\nDigite: '

def selecao_inicial(indice):   
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
    
def lista_torneios():
    def altera_torneio():
        return

    def deleta_torneio():
        return

    sumario_torneio = 'Digite o número correspondente para fazer a ação desejada:\n1 - Ver Partidas\n2 - Alterar Torneio \n3 - Excluir Torneio\n9 - Finalizar Gestor de Torneios\nDigite: '

    def selecao_torneio(indice):
        match indice:
            case 1:
                return print(lista_partidas())
            case 2:
                return altera_torneio()
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


    def calcula_tier():
        return 'tier'

    try:
        nome = input('Vamos criar um torneio! Para isso precisamos de algumas informações.\nQual o nome do seu torneio?\nDigite: ')

        
        while False: #data_inicial e data_final não é timestamp
            data_inicial = input('Em que data ele começa?\nDigite a data conforme o exemplo (): ')
            data_final = input('Em que data ele termina?\nDigite a data conforme o exemplo (): ')
        
        print(lista_organizadores())
        while False: #organizador não está em organizadores
            organizador = input('Qual o organizador?\nDigite apenas o código: ')
        
        print(lista_patrocinadores())
        while False: #valida patrocinadores
            patrocinador = input('Possui algum patrocinador?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nCaso não possua nenhum patrocinador, apenas deixe em branco\nDigite: ')

        print(lista_regioes())
        while False: #região não está em regioes
            regiao = input('Qual a região?\nDigite apenas o código: ')
        
        print(lista_times())
        while False: #valida times
            time = input('Quais são os times?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nDigite: ')

        #Podemos fazer uma validação e mudar o texto caso o usuario tenha cometido erro ao digitar

        tier = calcula_tier()

        criar_partidas()
        
    
    except:
        tentar_novamente(input('Ocorreu um erro ao criar o seu torneio, deseja tentar novamente?\nDigite S/N: '))
        return
        
    print('Torneio criado com sucesso!')
    
    return selecao_inicial('retorno')



def lista_partidas():
    return 'lista de partidas'

def lista_organizadores():
    return 'lista de organizadores'

def lista_patrocinadores():
    return 'lista de patrocinadores'

def lista_regioes():
    return 'lista de regioes'

def lista_times():
    return 'lista de times'

def criar_partidas():
    return

def listar_partidas():
    return


selecao_inicial(int(input(f'Seja bem vindo ao gestor de torneios!\n{sumario}')))

