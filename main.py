def adicionaAluno(lista):
  while True: 
    try:
      nome = input("Digite o nome do aluno (ou 'F' para encerrar'): ")
      
      if nome.upper() == 'F':
        break
     
      idade = int(input("Digite a idade do aluno: "))
      peso = float(input("Digite o peso do aluno: "))
      altura = float(input("Digite a altura do aluno: "))
      imc = calculaIMC(peso, altura)
    
      aluno = [nome, idade, peso, altura, imc]
      lista.append(aluno)
      print("Aluno adicionado!")

      # for i, aluno in enumerate(lista):
      #   print(i, aluno)
      
    except ValueError:
      print("Valor Inválido. Digite novamente.")

def listaAlunos(lista):
  total_imc = 0
  if len(lista) == 0:
    print("Não há alunos na lista.")
  else:
    print("------------------------------------")
    print("INFORMAÇÕES DO ALUNO(a) CADASTRADOS:")
    print("------------------------------------")
    
    for aluno in lista:
      nome, idade, peso, altura, imc = aluno
     
      print(f'Nome: {nome}')
      print(f'Idade: {idade}')
      print(f'Peso: {peso}')
      print(f'Altura: {altura}')
      print(f'IMC: {imc:.2f}')
      print("----------------------------")
      total_imc += aluno[4]

    print(f'Média do IMC dos alunos: {total_imc / len(lista):.2f}')

def pesquisaAluno(lista):

  if len(lista) == 0:
    print("Não há alunos na lista.")
  else:
    nome_desejado = input("Digite o nome do aluno desejado: ")
    encontrado = False
    
    for aluno in lista:
      if aluno[0] == nome_desejado:
        encontrado = True
        nome, idade, peso, altura, imc = aluno
        print("-----------------------")
        print("INFORMAÇÕES DO ALUNO(a):")
        print("-----------------------")
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Peso: {peso}')
        print(f'Altura: {altura}')
        print(f'IMC: {imc:.2f}')
        print("------------------")
        break
    if not encontrado:
      print("Aluno não encontrado")
      
def excluiAlunos(lista):
  if len(lista) == 0:
    print("Não há alunos na lista.")
  else:
    nome = input("Digite o nome do aluno para excluir: ")
    for aluno in lista:
      if aluno[0] == nome:
        lista.remove(aluno)
        print("Aluno removido!")
        return
    print("Aluno não encontrado.")

def pesquisaAlunoIdade(lista):
  idade_escolhida = int(input("Digite a idade desejada: "))

  alunos_encontrados = []

  for aluno in lista:
    nome, idade, peso, altura, imc = aluno
    totalIMC = 0
    
    if idade == idade_escolhida:
      alunos_encontrados.append(aluno)

    if len(alunos_encontrados) == 0:
      print("Não encontrei alunos com essa idade. ")
    else:
      print("Alunos encontrados:")
      for aluno in alunos_encontrados:
        nome, idade, peso, altura, imc = aluno
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Peso: {peso}')
        print(f'Altura: {altura}')
        print(f'IMC: {imc:.2f}')
        print("\n")

        totalIMC += aluno[4]

      # Calcula o IMC
      mediaIMC = totalIMC / len(alunos_encontrados)
      print(f'IMC médio do grupo: {mediaIMC:.2f}')

def calculaIMC(peso, altura):
  return peso / (altura * altura)

def exibeMenu():
  print('''
  ----- Menu -----
  1 - Incluir Aluno
  2 - Listar Alunos
  3 - Pesquisar Aluno
  4 - Pesquisar por idade
  5 - Excluir Alunos
  9 - Sair
  ''')

def main():
  lstAlunos = []

  while True:
    exibeMenu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      adicionaAluno(lstAlunos)
    elif opcao == "2":
      listaAlunos(lstAlunos)
    elif opcao == "3":
      pesquisaAluno(lstAlunos)
    elif opcao == "4":
      pesquisaAlunoIdade(lstAlunos)
    elif opcao == "5":
      excluiAlunos(lstAlunos)
    elif opcao == "9":
      print("Encerrando o programa ...")
      break
    else:
      print("Opção inválida. Digite novamente.")

main()