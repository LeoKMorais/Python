#PROJETO 2 - CADASTRO DE FORNECEDORES
"""""
Na empresa em que você trabalha foi solicitada a implementação de um sistema de cadastro dos fornecedores. As informações que devem ser cadastradas são:

- Código do fornecedor;
- Nome do fornecedor;
- Telefone do fornecedor;
- Email do fornecedor.

Para isso, você deverá criar um script para armazenar essas informações em alguma estrutura de dados.

Também como parte do sistema de cadastro, é necessário criar uma "interface de navegação" pelo sistema, que tenha as seguintes funcionalidades:

- Permite a exibição (usando o `print`) de todas as informaçoes de contatos específicos, a partir da busca pelo código do fornecedor;
- Permite a remoção e adição de fornecedores à estrutura de cadastro.

Requisitos:

- Requisito #1 - Não existe um limite para fornecedores cadastrados, portanto você deverá permitir que o usuário cadastre a quantidade que desejar.
- Requisito #2 - Crie pelo menos uma função em seu script. Você deverá escolher pelo menos uma tarefa do seu script e implementar em uma função para chamá-la dentro da sua lógica de cadastro.
- Requisito #3 - Crie pelo menos uma verificação em seu código, por exemplo: Se o dicionário estiver vazio, não permita a opção remover.

Tópicos avaliados:

- Variáveis;
- Tipos de dados;
- Operadores aritméticos;
- I/O de dados;
- Expressões lógicas e condicionais;
- Laços de repetição;
- Listas e dicionários;
- Funções.
"""""

#Função para verificar se a opção de cadastro foi digitada corretamente
def testaentrada(n):
    while True:
        try:
            n=int(n)
            if 0<=n<=6: #Fica em loop até que seja digitada uma opção de 1 a 6
                break
            else:
                n=input("ERRO: DIGITE UMA OPÇÃO DE 1 A 6 ")
        except:
            n=input("ERRO: DIGITE UM NÚMERO, DE 1 A 6 ")
    return n
#Iniciamos com listas vazias onde serão armazenados os dados
cod=[]
nome=[]
tel=[]
email=[]
print("CADASTRO DE FORNECEDORES")
while True: #Programa permanece no loop de cadastro até que o usuário selecione a opção para sair
    opc=input("Digite a opção desejada: \n1-Novo Cadastro \n2-Mostrar Dados Cadastrados \n3-Apagar Dados \n4-Corrigir Dados \n5-Consultar Fornecedor \n6-Sair ")
    n=testaentrada(opc)
    if n==1: #Caso selecionada a opção 1, entra o script para criação de novo cadastro
        sel="" #Variável de seleção de opção para confirmação dos dados, inicia vazia e depois recebe S ou N
        while sel!="S": #Caso seja selecionado N, os dados não são gravados e o loop retorna ao começo
            print("NOVO CADASTRO")
            codprov=""
            nomeprov=""
            telprov=""
            emailprov=""
            while codprov=="":# Os laços abaixo não permitem que o programa prossiga se alguma das entradas não for digitada.
                codprov=input("Digite o Código do fornecedor: ")
            while nomeprov=="":
                nomeprov=input("Digite o Nome do Fornecedor: ")
            while telprov=="":
                telprov=input("Digite o Telefone do Fornecedor: ")
            while emailprov=="":
                emailprov=input("Digite o Email do Fornecedor: ")
            print("Dados digitados: \nCódigo:",codprov,"\nNome:",nomeprov,"\nTelefone:",telprov,"\nEmail:",emailprov)
            n1=input("Confirma? S/N ") #Caso seja selecionado S, o programa segue em frente e grava os dados no cadastro.
            n1=n1.upper()
            while True: #Loop para verificar se foi escolhido só S ou N, ou se há erro na entrada.
                if (n1=="S") or (n1=="N"):
                    sel=n1
                    break
                else:
                    n1=input("ERRO: CONFIRME APENAS COM S OU N ") 
                    n1=n1.upper
        if codprov in cod: #Verifica se o código digitado já existe na lista, caso positivo retorna erro
            print("ERRO: CÓDIGO JÁ CADASTRADO")
        else:
            cod.append(codprov)#Salva os dados se o código for novo na lista
            nome.append(nomeprov)
            tel.append(telprov)
            email.append(emailprov)
            print("CONFIRMADO, DADOS SALVOS")
    elif n==2: #Caso selecionada a opção 2, retorna uma lista com os dados gravados
        if len(cod)==0:
            print ("ERRO: CADASTRO VAZIO") #Retorna erro caso não existam registros
        else:
            for i in range (len(cod)):
                print(cod[i],nome[i],tel[i],email[i])
    elif n==3: #Caso selecionada a opção 3, entra o script de remoção de dados
        if len(cod)!=0:
            coddelete=input("Digite o código do fornecedor que deseja apagar: ")
            try:
                idx=cod.index(coddelete) #Tenta encontrar o código digitado na tabela e seu respectivo índice
                cod.pop(idx)     #Apaga os registros em todas as tabelas no indice do código digitado
                nome.pop(idx)
                tel.pop(idx)
                email.pop(idx)
                print("Fornecedor de código",coddelete,"apagado")
            except:
                print("ERRO: CÓDIGO NÃO ENCONTRADO") #Retorna erro caso o código não seja encontrado
        else:
            print("ERRO: O CADASTRO JÁ ESTÁ VAZIO")
    elif n==4: #Caso seja selecionada a opção 4, entra o script de alteração de dados
        if len(cod)!=0:
            codaltera=input("Digite o código do fornecedor que deseja alterar: ")
            try:
                idx=cod.index(codaltera) #Tenta encontrar o código digitado na tabela e seu respectivo índice
                print("Qual atributo você deseja alterar? (1, 2 ou 3)")
                atributo=input("1 - NOME \n2 - TELEFONE \n3 - EMAIL ")
                if (atributo=="1") or (atributo=="2") or (atributo=="3"):
                    if atributo=="1":
                        novonome=input("Digite o novo nome: ")
                        nome[idx]=novonome #Altera o registros no indice do código digitado para a tabela selecionada
                        print("NOME ALTERADO")
                    elif atributo=="2":
                        novotel=input("Digite o novo telefone: ")
                        tel[idx]=novotel
                        print("TELEFONE ALTERADO")
                    elif atributo=="3":
                        novoemail=input("Digite o novo email: ")
                        email[idx]=novoemail
                        print("EMAIL ALTERADO")
                else:
                    print("ERRO: SELECIONE OS ATRIBUTOS 1, 2 OU 3") #Retorna erro caso seja digitado algo diferente de 1, 2 ou 3
            except:
                print("ERRO: CODIGO NÃO ENCONTRADO")
        else:
            print("ERRO: CADASTRO VAZIO")
    elif n==5: #Caso selecionada a opção 5, entra o script de consulta de dados individuais
        if len(cod)!=0:
            codconsulta=input("Digite o código do fornecedor que deseja consultar: ")
            try:
                idx=cod.index(codconsulta)
                print("Codigo:",cod[idx],"\nNome:",nome[idx],"\nTelefone:",tel[idx],"\nEmail:",email[idx])
            except:
                print("ERRO: CÓDIGO NÃO ENCONTRADO")
        else:
            print("ERRO: CADASTRO VAZIO")
    else: #Caso selecionada opção 6, encerra o loop
        break
print("PROGRAMA ENCERRADO")

            

