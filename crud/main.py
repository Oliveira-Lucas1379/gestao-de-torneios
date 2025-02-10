import controller
import random
import time
import datetime
import re

sumario = 'Digite o número correspondente para fazer a ação desejada:\n1 - Criar Torneio \n2 - Ver Torneio\n9 - Finalizar Gestor de Torneios\nDigite: '

inputTimes = 'Quais são os times?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nDigite: '

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
                return altera_torneio(int(input('\nDigite o código do torneio que deseja alterar: ')))
            case 3:
                return deleta_torneio(int(input('\nDigite o código do torneio que deseja deletar: ')))
            case 9:
                return print('\nObrigado por utilizar o gestor de torneios! Até a próxima!')
            case _:
                return selecao_torneio(int(input(f'Valor {indice} inválido\n{sumario_torneio}')))                
    try:
        selecao_torneio(int(input(sumario_torneio)))
    except:
        selecao_torneio(int(input(f'\nValor inválido!\n{sumario_torneio}')))

    return selecao_inicial('retorno')

def altera_torneio(cod_torneio):
    def altera(tipo, novo_dado = None):
        if tipo == 'times':
            deletar_partidas(cod_torneio)
            criar_partidas(cod_torneio, novo_dado)

        elif tipo == 'codpatrocinador':
            columns = ["patrocinadores.codpatrocinador", "patrocinadores.nome", "torneio.nome"]
            condition = f'torneio.codtorneio = {cod_torneio}'
            join_clause = [("torneio_patrocinador", "torneio.codtorneio", "torneio_patrocinador.codtorneio", ''),
                           ("patrocinadores", "torneio_patrocinador.codpatrocinador", "patrocinadores.codpatrocinador", ''),
                           ]
            patrocinadores = controller.get_all("torneio", columns, join_clause, condition)
            print(formatacao_dados(["CODIGO", "NOME-PATROCINADOR", "NOME-TORNEIO"], patrocinadores))

            removerPatrocinio = input("Aperte enter caso não queira remover nenhum patrocinador!\nDigite o código do patrocinador que deseja remover do torneio:")
            if removerPatrocinio:
                controller.delete("torneio_patrocinador", {"codtorneio": cod_torneio, "codpatrocinador": int(removerPatrocinio)})

            print(lista_patrocinadores())
            adicionarPatrocinio = input("Aperte enter caso não queira adicionar nenhum patrocinador!\nDigite o código do patrocinador que deseja adicionar ao torneio: ")
            if adicionarPatrocinio:
                controller.insert("torneio_patrocinador", ["codtorneio", "codpatrocinador"], [(cod_torneio, int(adicionarPatrocinio))])

        else:
            controller.update('torneio', {tipo:novo_dado}, {'CodTorneio':cod_torneio})

    try:
        indice_altera = int(input('O que você deseja alterar?\n1 - Partidas\n2 - Nome\n3 - Data de Inicio\n4 - Data Final\n5 - Organizador\n6 - Patrocinador\n7 - Região\n8 - Tier\n9 - Times\n10 - Sair\nDigite: '))
    except:
        print('Valor de alteração inválido!')
        return selecao_inicial('retorno')
    
    match indice_altera:
        case 1:
            return alterar_partidas(cod_torneio)
        case 2:
            return altera('nome')
        case 3:
            return altera('DataInicial', get_data(0, input('\nAlterar data inicial\nDigite a data conforme o exemplo (AAAA-MM-DD): ')))
        case 4:
            return altera('DataFinal', get_data(0, input('\nAlterar data final\nDigite a data conforme o exemplo (AAAA-MM-DD): ')))
        case 5:
            return altera('CodOrganizador', get_organizador(0, int(input('\nQual o Novo Organizador?\nDigite apenas o código: '))))
        case 6:
            return altera('codpatrocinador')
        case 7:
            return altera('CodRegiao', get_regiao(0, int(input('Qual a nova região?\nDigite apenas o código: '))))
        case 8:
            return altera('CodTier', get_tier(0, int(input('Qual o novo tier?\nDigite apenas o código: '))))
        case 9:
            print(lista_times())
            return altera('times', get_times(0, input(inputTimes)))
        case 10:
            return selecao_inicial('retorno')
        case _:
            print('Valor de alteração inválido!')
            return selecao_inicial('retorno')

def alterar_partidas(cod_torneio):
    print(lista_partidas(cod_torneio))

    partida = int(input('Digite o código da partida que deseja alterar: '))
        
    times_da_partida = controller.get_all('Times', ['Times.CodTime, Times.Nome'], [('Times_Partidas', 'Times.CodTime', 'Times_Partidas.CodTime', '')] ,f'Times_Partidas.CodPartida = {partida}')
    print(formatacao_dados(['CODIGO','NOME'], times_da_partida))

    vencedor = get_idtime_partida(0, int(input('Digite código o time Vencedor: ')), times_da_partida) 
    perdedor = get_idtime_partida(0, int(input('Digite código o time Perdedor: ')), times_da_partida, vencedor)
    resultado = input('Digite resultado seguindo o exemplo (13x9): ')

    id_resultado = controller.get_all('Partidas', ['idResultado'], condition=f'CodPartida = {partida}')[0]
    if id_resultado[0]:
        controller.update('Resultados', {'Resultado':resultado, 'CodTimeVencedor':vencedor, 'CodTimePerdedor':perdedor}, condition={'id' :id_resultado})
    else:
        controller.insert('Resultados',['Resultado', 'CodTimeVencedor', 'CodTimePerdedor'], [(resultado, vencedor, perdedor)])
        id_resultado = controller.get_all('Resultados',['MAX(id)'])[0][0]
        controller.update('Partidas', {'idResultado':id_resultado}, condition={'CodPartida':partida})

def deleta_torneio(cod_torneio):
    validador = input('\nVocê tem certeza que deseja DELETAR o torneio?\nTodas partidas e informações relacionadas ao torneio também serão deletadas.\nEsta ação é irrevesível\nDigite S para deletar permanentemente: ')
    if  validador.upper() == 'S': 
        controller.delete('Torneio_Patrocinador', {'CodTorneio':cod_torneio})
        controller.delete('Classificacoes', {'CodTorneio':cod_torneio})
        deletar_partidas(cod_torneio)
        controller.delete('Torneio', {'CodTorneio':cod_torneio})
        print('\nTorneio Deletado!')

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

    try:
        nome = input('\nVamos criar um torneio! Para isso precisamos de algumas informações.\nQual o nome do seu torneio?\nDigite: ')
        
        data_inicial = get_data(0, input('\nEm que data ele começa?\nDigite a data conforme o exemplo (AAAA-MM-DD): '))
        data_final = get_data(0, input('\nEm que data ele termina?\nDigite a data conforme o exemplo (AAAA-MM-): '))

        print(lista_organizadores())
        organizador = get_organizador(0, int(input('Qual o organizador?\nDigite apenas o código: ')))
        
        print(lista_patrocinadores())
        patrocinadores = get_patrocinador(0, input('Possui algum patrocinador?\nDigite os seus códigos separados por "/"\nExemplo: 01/02/03\nCaso não possua nenhum patrocinador, apenas deixe em branco\nDigite: '))   
        
        print(lista_regioes())
        regiao = get_regiao(0, int(input('Qual a região?\nDigite apenas o código: ')))
        
        print(lista_tiers())
        tier = get_tier(0, int(input('Qual o tier?\nDigite apenas o código: ')))
        
        print(lista_times())
        times = get_times(0, input(inputTimes))
        
        cod_torneio = int(controller.get_all('torneio',['MAX(codtorneio)'])[0][0]) + 1
      
        controller.insert('torneio', ['codtorneio' ,'nome', 'datainicial', 'datafinal', 'codregiao', 'codtier', 'CodOrganizador'],
                          [(cod_torneio, nome, data_inicial, data_final, regiao, tier, organizador)])
          
        if patrocinadores:
            for patrocinador in patrocinadores:
                controller.insert('torneio_patrocinador', ['codtorneio', 'codpatrocinador'], [(cod_torneio, patrocinador)])

        criar_partidas(cod_torneio, times)
        
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

def get_tier(contador, tier):
    if contador >= 3:
        raise print('Tier inválido! Limite máximo de tentativas excedido')

    if not any(tupla[0] == tier for tupla in tiers):
        return get_regiao(contador+1, int(input('\ntier inválido!\nDigite apenas o código: ')))  
    
    return tier

def get_times(contador, times):
    if contador >= 3:
        raise print('Times inválidos! Limite máximo de tentativas excedido')
    
    timesCod = list(map(int, times.split('/')))

    for e in timesCod:
        if not any(tupla[0] == e for tupla in todos_os_times):
            return get_times(contador + 1, input('\nVocê cometeu um erro ao digitar!\n'+inputTimes))
    
    return timesCod

def get_idtime_partida(contador, idtime, times_da_partida, outro_time = None):
    if contador >= 3:
        raise print('Time inválio! Limite máximo de tentativas excedido')

    if not(any(tupla[0] == idtime for tupla in times_da_partida)) or idtime == outro_time:
        return get_idtime_partida(contador+1, int(input('\Time inválido!\nDigite apenas o código: ')), times_da_partida, outro_time)  
    
    return idtime  


def lista_times():
    global todos_os_times
    todos_os_times = controller.get_all("times", ["codtime", "nome"])
    return formatacao_dados(["CODIGO", "NOME"], todos_os_times)

def atualiza_partida(cod_partida, novos_dados):
    idResultado = controller.get_all("partidas", ["idresultado"], None, f"codpartida = {cod_partida}")
    vencedorAnterior = controller.get_all("resultados", ["codtimevencedor"], None, f"id = {idResultado[0][0]}")
    perdedorAnterior = controller.get_all("resultados", ["codtimeperdedor"], None, f"id = {idResultado[0][0]}")
    codTimePerdedor, codTimeVencedor = None, None
    if novos_dados[0]:
        controller.update("partidas", {"data": novos_dados[0]}, {"codpartida": cod_partida})
    if novos_dados[1]:
        controller.update("resultados",
                          {"resultado": novos_dados[1]},
                          {"id": idResultado[0][0]})
    if novos_dados[2]:
        codTimeVencedor = controller.get_all("times", ["codtime"], None, f"nome = '{novos_dados[2]}'")
        controller.update("resultados",
                          {"CodTimeVencedor": codTimeVencedor[0][0]},
                          {"id": idResultado[0][0]})
    if novos_dados[3]:
        codTimePerdedor = controller.get_all("times", ["codtime"], None, f"nome = '{novos_dados[3]}'")
        controller.update("resultados",
                          {"CodTimePerdedor": codTimePerdedor[0][0]},
                          {"id": idResultado[0][0]})
    if codTimeVencedor:
        controller.update("times_partidas", {"codtime": codTimeVencedor[0][0]}, {"codpartida": cod_partida, "codtime": vencedorAnterior[0][0]})
    if codTimePerdedor:
        controller.update("times_partidas", {"codtime": codTimePerdedor[0][0]}, {"codpartida": cod_partida, "codtime": perdedorAnterior[0][0]})

    print("\nPartida atualizada com sucesso!")
    return selecao_inicial('retorno')

def lista_torneios():
    global torneios
    torneios = controller.get_all("torneio", ["*"])
    return formatacao_dados(["CODIGO", "NOME", "DATA-INICIAL", "DATA-FINAL", "CODIGO-REGIAO", "CODIGO-TIER", "CODIGO-ORGANIZADOR"], torneios)

def lista_partidas(cod_torneio):
    condition = f'torneio.codtorneio = {cod_torneio}'
    columns = ["partidas.codpartida", "partidas.data", "torneio.nome", "resultados.resultado", "tv.nome", "tp.nome", "tier.divisao"]
    join_clause = [("torneio", "partidas.codtorneio", "torneio.codtorneio", ""),
                ("resultados", "partidas.idresultado", "resultados.id", "LEFT"),
                ("times tv", "resultados.CodTimeVencedor", "tv.codtime", "LEFT"),
                ("times tp", "resultados.CodTimePerdedor", "tp.codtime", "LEFT"),
                ("tier", "tier.codtier", "torneio.codtier", "")]
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

def lista_tiers():
    global tiers
    tiers = controller.get_all("Tier", ["*"])
    return formatacao_dados(["CODIGO", "DIVISÃO"], tiers)

def formatacao_dados(cabecalhos, dados):
    larguras = [max(len(str(item))for item in coluna) for coluna in zip(cabecalhos, *dados)]
    tabela = "\n" + "  ".join(header.ljust(larguras[i]) for i, header in enumerate(cabecalhos)) + "\n"
    tabela += "-".join("-" * (largura + 2) for largura in larguras) + "\n"
    for linha in dados:
        tabela += "  ".join(str(item).ljust(larguras[i]) for i, item in enumerate(linha)) + "\n"
    return tabela

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)

def criar_partidas(cod_torneio, times=None):  
    data_inicio, data_fim = controller.get_all('Torneio', ['DataInicial', 'DataFinal'], condition = f'CodTorneio = {cod_torneio}')[0]
    if not times:
        times_participantes = controller.get_all(f'GetTimesByTorneio({cod_torneio})', ['*'])
    else:
        times_participantes = times

    for time in times_participantes:
        times_participantes = times_participantes[1:]
        for e in list(range(len(times_participantes))):
            data_partida = random_date(data_inicio.strftime('%Y-%m-%d'), data_fim.strftime('%Y-%m-%d'), random.random())
            controller.insert('partidas', ['CodTorneio', 'Data'], [(cod_torneio, data_partida)])
            
            codpartida = int(controller.get_all('Partidas',['MAX(CodPartida)'])[0][0])

            controller.insert('Times_Partidas', ['CodPartida', 'CodTime'], [(codpartida, time)])
            controller.insert('Times_Partidas', ['CodPartida', 'CodTime'], [(codpartida, times_participantes[e])])
    
def deletar_partidas(cod_torneio):
    cod_partidas = controller.get_all('partidas',['CodPartida'], condition = f'CodTorneio = {cod_torneio}')

    for cod_partida in cod_partidas:
        controller.delete('Times_Partidas', {'codPartida' : cod_partida})

    controller.delete('partidas', {'CodTorneio' : cod_torneio})


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

