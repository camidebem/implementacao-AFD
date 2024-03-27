# Implementação de um Autômato Finito Determinístico Genérico 
# GCC108 - Teoria da Computação 
# Aluna: Camily Gonçalves de Bem

# Declarando as Estruturas 

estados = [] # o conjunto de estados será armazenado em uma lista 
alfabeto = [] # o alfabeto da linguagem será armazenado em uma lista 
funcao_transicao = {} # as funções de transição ficarão armazenadas em um dict, devido a característica chave-valor δ(q0,a) -> q1
estado_inicial = "" # estado inicial é uma String 
estados_finais = [] # o conjunto de estados finais fica em uma lista

# Leitura de dados 

print("Digite os Estados que compõem o autômato: ", end="")
estados = input().strip().split() # é necessário o uso do .split porque o python trataria os estados como uma única string na lista. Com o split o espaço serve de separador.
print("Digite o alfabeto da linguagem: ", end="")
alfabeto = input().split()
print("Digite o estado inicial: ", end="") 
estado_inicial = input().strip() # usando o strip para remover o espaço antes de apertar enter.
print("Digite o conjunto de estados de aceitação (finais): ", end="") 
estados_finais = input().split()
# Definindo as funções de transição 
print ("Digite as funções de transição conforme solicitadas na saída: ")
for estado in estados:
    for caractere in alfabeto: 
        print(f"  - δ({estado}, {caractere}) = ", end='')
        proximo_estado = input()

        if proximo_estado == "y": 
            funcao_transicao[(estado, caractere)] = None
        else: 
            funcao_transicao[(estado, caractere)] = proximo_estado

# Reconhecendo 
while True: # loop para entrar com mais de uma palavra a ser testada no autômato
    print("\nInforme a palavra: ", end="")
    entrada = input()

    # verificando se todos os caracteres da entrada pertencem ao alfabeto
    if any(caractere not in alfabeto for caractere in entrada):
        print("Palavra contém caracteres inválidos. Por favor, use apenas caracteres do alfabeto definido.")
        continue

    estado_atual = estado_inicial 
    rejeitou = False  # variável para controlar se a palavra foi rejeitada ou não

    for caractere in entrada: 
        print(f"  - δ({estado_atual}, {caractere}) = {funcao_transicao.get((estado_atual, caractere), None)}\n", end='')
        
        estado_atual = funcao_transicao.get((estado_atual, caractere), None)
        if estado_atual is None: 
            rejeitou = True  # se a palavra for rejeitada, atualize a variável para True
            break # não há necessidade de continuar testando após ela ser rejeitada

    if not rejeitou:  
        if estado_atual in estados_finais: 
            print("Aceita")
        else:
            print("Rejeita")
    else: 
        print("Rejeita")

    opcao = input("Deseja testar outra palavra? (s para sim, qualquer outra coisa para sair): ")
    if opcao.lower() != 's':
        break