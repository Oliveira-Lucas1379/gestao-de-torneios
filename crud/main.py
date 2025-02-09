import controller
import datetime
import re
from datetime import datetime, date

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
    sumario_torneio = 'Digite o número correspondente para fazer a ação desejada:\n1 - Ver Partidas\n2 - Alterar Torneio \n3 - Excluir Torneio\n9 - Finalizar Gestor de Torneios\nDigite: '

    print(f'\nEstes sãos os torneios já cadastrados:\n{lista_torneios()}')
    def selecao_torneio(indice):
        match indice:
            case 1:
                return print(f'\nEstas são as partidas do torneio:\n{lista_partidas(input("Digite o código do torneio: "))}')
            case 2:
                return altera_torneio(int(input('Digite o código do torneio que deseja alterar: ')))
            case 3:
                return deleta_torneio(int(input('Digite o código do torneio que deseja deletar: ')))
            case 9:
                return print('Obrigado por utilizar o gestor de torneios! Até a próxima!')
            case _:
                return selecao_torneio(int(input(f'Valor {indice} inválido\n{sumario_torneio}')))                
    try:
        selecao_torneio(int(input(sumario_torneio)))
    except:
        selecao_torneio(int(input(f'\nValor inválido!\n{sumario_torneio}')))

    return selecao_inicial('retorno')

def altera_torneio(cod_torneio):
    def altera(tipo, novo_dado):
        if tipo == 'times':
            controller.delete('torneio_time', f'codtorneio = {cod_torneio}')
            for e in novo_dado:
                controller.insert('torneio_time', ['codtorneio, codtime'],[cod_torneio, e])
            altera('partidas')

        elif tipo == 'partidas':
            controller.delete('partidas', f'codtorneio = {cod_torneio}')
            controller.criar_partidas(cod_torneio)

        else:
            controller.update('torneio', {tipo:novo_dado}, {'codtorneio':cod_torneio})

    try:
        indice_altera = int(input('O que você deseja alterar?\n1 - Partidas\n2 - Nome\n3 - Data de Inicio\n4 - Data Final\n5 - Organizador\n6 - Patrocinador\n7 - Times\n9 - Sair\nDigite: '))
    except:
        print('Valor de alteração iválido!')
        return selecao_inicial('retorno')
    
    match indice_altera:
        case 1:
            return altera('partidas')
        case 2:
            return altera('nome', input('Novo nome: '))
        case 3:
            return altera('data_inicio', get_data(0, input('\nAlterar data inicial\nDigite a data conforme o exemplo (01 01 2025): ')))
        case 4:
            return altera('data_fim', get_data(0, input('\nAlterar data final\nDigite a data conforme o exemplo (01 01 2025): ')))
        case 5:
            return altera('codorganizador', get_organizador(0, int(input('\nQual o Novo Organizador?\nDigite apenas o código: '))))
        case 6:
            return altera('codpatrocinador', get_patrocinador(0, input('\nVamos alterar os patrocinadores\nDigite os novos códigos separados por "/"\nExemplo: 01/02/03\nCaso não possua nenhum patrocinador, apenas deixe em branco\nDigite: ')))
        case 7:
            return altera('times', get_times(0, input(inputTimes)))
        case 9:
            return selecao_inicial('retorno')
        case _:
            print('Valor de alteração iválido!')
            return selecao_inicial('retorno')


def deleta_torneio(cod_torneio):
    if input('\nVocê tem certeza que deseja DELETAR o torneio?\nTodas partidas e informações relacionadas ao torneio também serão deletadas.\nEsta ação é irrevesível\nDigite S para deletar permanentemente: ').upper == 'S': 
        controller.delete('torneios', f'codtorneio = {cod_torneio}')
    else:
        print(f'O torneio NÃO foi deletado')
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

    def calcula_tier(times):
        return 1

    try:
        nome = input('\nVamos criar um torneio! Para isso precisamos de algumas informações.\nQual o nome do seu torneio?\nDigite: ')
        
        data_inicial = get_data(0, input('\nEm que data ele começa?\nDigite a data conforme o exemplo (2025-01-01): '))
        data_final = get_data(0, input('\nEm que data ele termina?\nDigite a data conforme o exemplo (2025-01-01): '))

        print(lista_organizadores())
        organizador = get_organizador(0, int(input('\nQual o organizador?\nDigite apenas o código: ')))
        
        print(lista_patrocinadores())
        patrocinadores = get_patrocinador(0, input('\nPossui algum patrocinador?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nCaso não possua nenhum patrocinador, apenas deixe em branco\nDigite: '))   
        
        print(lista_regioes())
        regiao = get_regiao(0, int(input('\nQual a região?\nDigite apenas o código: ')))
        
        global inputTimes 
        inputTimes = '\nQuais são os times?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nDigite: '
        print(lista_times())
        times = get_times(0, input(inputTimes))
        
        cod_torneio = int(controller.get_all('torneio',['MAX(codtorneio)'])[0][0]) + 1
        tier = calcula_tier(times)
        controller.criar_partidas(cod_torneio)

        '''
        insert correto
        controller.insert('torneio',
                        ['codtorneio','nome', 'data_inicial', 'data_final', 'organizador', 'regiao', 'tier'], 
                        [cod_torneio, nome, data_inicial, data_final, organizador, regiao, tier])
        '''        
        #insert parcial
        controller.insert('torneio', ['codtorneio' ,'nome', 'datainicial', 'datafinal', 'codregiao', 'codtier'],
                          [(cod_torneio, nome, data_inicial, data_final, regiao, tier)])

        controller.insert('torneio_organizador', ['codtorneio', 'codorganizador'], [(cod_torneio, organizador)])  
          
        if patrocinadores:
            for patrocinador in patrocinadores:
                controller.insert('torneio_patrocinador', ['codtorneio', 'codpatrocinador'], [(cod_torneio, patrocinador)])

        # Aparentemente não tem o torneio_times
        '''
        for time in times:
            controller.insert('torneio_times', ['codtorneio'], [(time)])
            '''
        
    except:
        tentar_novamente(input('Ocorreu um erro ao criar o seu torneio, deseja tentar novamente?\nDigite S/N: '))
        return
        
    print(f'Torneio {nome} criado com sucesso!')
    
    return selecao_inicial('retorno')

def get_data(contador, data):
    if contador >= 3:
        raise print('Data invália! Limite máximo de tentativas excedido')

    if not re.match(controller.regexData, data):
        return get_data(contador + 1, input("Data em formado inválido!\nDigite a data conforme o exemplo (2025-01-01): "))
    
    return data  
  
def get_organizador(contador, organizador):
    if contador >= 3:
        raise print('Organizador inválido! Limite máximo de tentativas excedido')
    
    if not any(tupla[0] == organizador for tupla in organizadores):
        return get_organizador(contador + 1, int(input('Organizador inválido!\nTente novamente: ')))
    
    return organizador

def get_patrocinador(contador, patrocinador):
    if patrocinador == '':
        return patrocinador
    
    if contador >= 3:
        raise print('Patrocinador Inválido! Limite máximo de tentativas excedido')

    patrocinadorCod = list(map(int, patrocinador.split("/")))

    for e in patrocinadorCod:
        if not any(tupla[0] == e for tupla in todos_os_patrocinadores):
            return get_patrocinador(contador + 1, input('\nPatrocinador inválido!\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nCaso não possua nenhum patrocinador, apenas deixe em branco\nDigite: '))
    
    return patrocinadorCod

def get_regiao(contador, regiao):
    if contador >= 3:
        raise print('Região invália! Limite máximo de tentativas excedido')

    if not any(tupla[0] == regiao for tupla in regioes):
        return get_regiao(contador+1, int(input('\nregião inválida!\nDigite apenas o código: ')))  
    
    return regiao

def get_times(contador, times):
    if contador >= 3:
        raise print('Times inválidos! Limite máximo de tentativas excedido')
    
    timesCod = list(map(int, times.split('/')))

    for e in timesCod:
        if not any(tupla[0] == e for tupla in todos_os_times):
            return get_times(contador + 1, input('\nVocê cometeu um erro ao digitar!\n'+inputTimes))
    
    return timesCod

def validaTimes(times):
    try:
        list(map(int, times.split('/')))
    except:
        return False
    return True

def lista_torneios():
    global torneios
    torneios = controller.get_all("torneio", ["*"])
    return formatacao_dados(["CODIGO", "NOME", "DATA-INICIAL", "DATA-FINAL", "CODIGO-REGIAO", "CODIGO-TIER"], torneios)

def lista_partidas(cod_torneio):
    condition = f'torneio.codtorneio = {cod_torneio}'
    columns = ["partidas.codpartida", "partidas.data", "torneio.nome", "resultados.resultado", "tv.nome", "tp.nome", "tier.divisao"]
    join_clause = [("torneio", "partidas.codtorneio", "torneio.codtorneio"),
                ("resultados", "partidas.idresultado", "resultados.id"),
                ("times tv", "resultados.CodTimeVencedor", "tv.codtime"),
                ("times tp", "resultados.CodTimePerdedor", "tp.codtime"),
                ("tier", "tier.codtier", "torneio.codtier")]
    global partidas
    partidas = controller.get_all("partidas", columns, join_clause, condition)
    return formatacao_dados(["CODIGO", "DATA", "NOME-TORNEIO", "RESULTADO", "TIME-VENCEDOR", "TIME-PERDEDOR", "TIER"], partidas)

def lista_organizadores():
    global organizadores
    organizadores = controller.get_all("organizadores", ["*"])
    return formatacao_dados(["CODIGO", "NOME"], organizadores)

def lista_patrocinadores():
    global todos_os_patrocinadores
    todos_os_patrocinadores = controller.get_all("patrocinadores", ["*"])
    return formatacao_dados(["CODIGO", "NOME", "ORIGEM"], todos_os_patrocinadores)

def lista_regioes():
    global regioes
    regioes = controller.get_all("regiao", ["*"])
    return formatacao_dados(["CODIGO", "NOME", "LOCALIZACAO"], regioes)

def lista_times():
    global todos_os_times
    todos_os_times = controller.get_all("times", ["codtime", "nome"])
    return formatacao_dados(["CODIGO", "NOME"], todos_os_times)

def formatacao_dados(cabecalhos, dados):
    larguras = [max(len(str(item))for item in coluna) for coluna in zip(cabecalhos, *dados)]
    tabela = "  ".join(header.ljust(larguras[i]) for i, header in enumerate(cabecalhos)) + "\n"
    tabela += "-".join("-" * (largura + 2) for largura in larguras) + "\n"
    for linha in dados:
        tabela += "  ".join(str(item).ljust(larguras[i]) for i, item in enumerate(linha)) + "\n"
    return tabela

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

init(False)

