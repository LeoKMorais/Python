'''
O intuito deste projeto é criar um sistema de Rede Social, que conte com sistema de login, cadastro de usuarios, interesses, informações, etc, utilizando python com Programação orientada a Objetos.

Serão criados também métodos para realizar as ações necessárias em uma rede social, como adicionar outros usuários como amigos, postar algo, ver número de amigos, ver posts de amigos, bloquear outros usuários e afins.
'''

#Classe Usuário, para os usuários da rede social
class Usuario:
    def __init__(self,nome,data_nascimento,email,apelido=None):
        '''
        Cria um usuário da rede social
        
        Parâmetros
        ----------
        nome : str
            O nome do usuário
        data_nascimento : str
            A data de nascimento do usuário
        email : str
            O email de cadastro do usuário
        apelido: str (opcional)
            O apelido do usuário
        '''
        self.nome=nome
        self.data_nascimento=data_nascimento
        self.email=email
        self.apelido=apelido
        self.lista_amigos=[]
        self.lista_posts=[]
        self.lista_interesses=[]
        self.lista_melhores_amigos=[]
        self.lista_bloqueados=[]
    #Método para postar
    def postar(self,post):
        '''
        Captura uma postagem e a salva na lista de posts

        Parâmetros
        ----------
        post: str
            O texto a ser postado, digitado pelo usuário
        '''
        self.lista_posts.append(post)
        print ("POSTADO!")

    #Método para mostrar o número de amigos
    def mostra_numero_amigos(self):
            print(f"O usuario {self.nome} possui {len(self.lista_amigos)} amigo(s) e {len(self.lista_melhores_amigos)} melhor(es) amigo(s)")

    #Método para mostrar o número de posts
    def mostra_numero_posts(self):
            print(f"O usuario {self.nome} fez {len(self.lista_posts)} post(s)")

    #Método para adicionar amigo
    def adiciona_amigo(self,amigo):
        '''
        Recebe um usuário indicado pelo usuário vigente e o adiciona como amigo

        Parâmetros
        ----------
        amigo: Usuario
            O usuario (objeto da classe Usuario) a ser adicionado como amigo
        '''
        if (amigo not in self.lista_amigos) and (amigo not in self.lista_melhores_amigos) and (self not in amigo.lista_amigos):
            self.lista_amigos.append(amigo)
            amigo.lista_amigos.append(self)
            print("AMIGO ADICIONADO")
        else:
            print("AMIGO JÁ ESTÁ NA LISTA")

    #Método para adicionar melhor amigo
    def adiciona_melhor_amigo(self,melhor_amigo):
        '''
        Recebe um usuário da lista de amigos e o adiciona como melhor amigo, o removendo da lista de amigos

        Parâmetros
        ----------
        melhor_amigo: Usuario
            O usuario (objeto da classe Usuario) a ser adicionado como amigo
        '''
        if (melhor_amigo not in self.lista_melhores_amigos):
            self.lista_melhores_amigos.append(melhor_amigo)
            self.lista_amigos.remove(melhor_amigo) #Adiciona o amigo aos melhores amigos e remove da lista de amigo. Esta operação não é mútua!
            print("AMIGO ADICIONADO AOS MELHORES AMIGOS")
        else:
            print("AMIGO JÁ ESTÁ NA LISTA DE MELHORES AMIGOS")

    #Método para adicionar interesse
    def adiciona_interesse(self,interesse):
        '''
        Recebe um interesse e o adiciona na lista de interesses

        Parâmetros
        ----------
        interesse: str
            O interesse adicionado pelo usuário
        '''
        if (interesse not in self.lista_interesses):
            self.lista_interesses.append(interesse)
            print("INTERESSE ADICIONADO")
        else:
            print("INTERESSE JÁ ESTÁ NA LISTA")

    #Método para desfazer amizade
    def desfazer_amizade(self,amigo):
        '''
        Recebe um amigo indicado pelo usuário vigente e o remove das listas de amigo

        Parâmetros
        ----------
        amigo: Usuario
            O usuario (objeto da classe Usuario) a ser removido das listas de amigo
        '''
        if amigo in self.lista_amigos:
            self.lista_amigos.remove(amigo) #Remove o amigo de todas as listas do usuario, bem como o usuario de todas as listas do amigo
        if amigo in self.lista_melhores_amigos:
            self.lista_melhores_amigos.remove(amigo)
        if self in amigo.lista_amigos:
            amigo.lista_amigos.remove(self)
        if self in amigo.lista_melhores_amigos:
            amigo.lista_melhores_amigos.remove(self)
        print("AMIZADE DESFEITA")

    #Método para buscar algo na lista de amigos
    def buscar_amigo(self,busca):
        '''
        Busca partes de um texto nas listas de amigo e melhores amigos do usuário vigente

        Parâmetros
        ----------
        busca: str
            O texto digitado pelo usuário a ser pesquisado entre os amigos

        Retorno:
        --------
        out: list
            Retorna lista com os nomes de amigos encontrados pela pesquisa
        '''
        lista_amigos_encontrados=[] #Lista vazia, vai armazenar os resultados de nomes de amigos encontrados nas iterações, e depois vai ser retornada pela função
        for amigo in self.lista_amigos: 
            if busca.lower() in amigo.nome.lower():
                lista_amigos_encontrados.append(amigo.nome)
        for melhor_amigo in self.lista_melhores_amigos:
            if busca.lower() in melhor_amigo.nome.lower():
                lista_amigos_encontrados.append(melhor_amigo.nome)
        return lista_amigos_encontrados

    #Método para buscar algo entre todos os posts cadastrados
    def buscar_post(self,busca):
        '''
        Busca partes de um texto nas listas de posts

        Parâmetros
        ----------
        busca: str
            O texto digitado pelo usuário a ser pesquisado entre os posts

        Retorno:
        --------
        out: list
            Retorna lista com os posts encontrados pela pesquisa
        '''
        lista_posts_encontrados=[] #Lista vazia, vai armazenar os posts encontrados ao longo das iterações, e depois vai ser retornada na função.
        for posts in self.lista_posts:
            if busca.lower() in posts.lower():
                lista_posts_encontrados.append(posts)
        return lista_posts_encontrados

    #Método para mostrar todos os posts de algum amigo
    def mostra_posts_amigo(self,amigo):
        for post in amigo.lista_posts:
            print(f"{amigo.nome}: {post}")

    #Método para bloquear
    def bloquear(self, inimigo):
        '''
        Recebe um 'inimigo' indicado pelo usuário vigente e o bloqueia,
        removendo das listas de amizade e impedindo novos pedidos de amizade

        Parâmetros
        ----------
        inimigo: Usuario
            O usuario (objeto da classe Usuario) a ser bloqueado
        '''
        if (inimigo not in self.lista_bloqueados) and (self not in inimigo.lista_bloqueados):
            self.lista_bloqueados.append(inimigo) 
            inimigo.lista_bloqueados.append(self)
            print("USUÁRIO BLOQUEADO")
            if inimigo in self.lista_amigos:
                self.lista_amigos.remove(inimigo) #Após adicionar o inimigo na lista de bloqueio, desfaz as amizades entre ele e o usuario (caso existam)
            if inimigo in self.lista_melhores_amigos:
                self.lista_melhores_amigos.remove(inimigo)
            if self in inimigo.lista_amigos:
                inimigo.lista_amigos.remove(self)
            if self in inimigo.lista_melhores_amigos:
                inimigo.lista_melhores_amigos.remove(self)
        else:
            print("Opa, ja existe um bloqueio entre vocês...")


#Inicio do código geral do programa
print("BEM VINDO AO PYTHONBOOK")
opcao_geral='' #Variável inicia vazia, para depois receber 1, 2 ou 3 (str)
cadastro_usuarios={} #dicionário inicia vazio, para depois receber os dados os usuarios conforme os mesmos são digitados(email:senha,nome,nascimento,email,apelido)
cadastro_usuarios_classe={} #dicionario inicia vazio, para depois receber o email e a referencia do objeto dos usuarios cadastrados na classe Usuario (email:objeto)
while opcao_geral!='3': #programa permanece no loop até ser selecionada a opção 3 para encerrar (str)
    opcao_geral=input("O QUE TEMOS PARA HOJE? \n1-NOVO CADASTRO \n2-LOGIN \n3-ENCERRAR \n")
    if opcao_geral=='1': #Opção para cadastrar novo usuario.
        print("NOVO CADASTRO")
        email_cadastro=input("Digite seu email: ") 
        senha_cadastro=input("Cadastre uma senha: ")
        nome_cadastro=input("Digite seu nome: ")
        nascimento_cadastro=input("Digite sua data de nascimento: ")
        apelido_cadastro=input("Digite seu apelido (opcional): ")
        if apelido_cadastro==None:
            apelido_cadastro==' ' #Define um espaço vazio para o apelido caso o mesmo não seja declarado, para não dar erro nos indices do dicionario cadastro_usuarios
        if email_cadastro not in cadastro_usuarios: #Verifica se o email digitado ainda não existe no dicionario de usuarios digitados
            cadastro_usuarios.update({email_cadastro:[senha_cadastro,nome_cadastro,nascimento_cadastro,email_cadastro,apelido_cadastro]}) #salva os dados digitados no dicionario
            for objeto in cadastro_usuarios: #percorre os usuarios salvos no dicionario de cadastro. 
                if cadastro_usuarios[objeto][3] not in cadastro_usuarios_classe: #Se a chave salva não estiver instanciada na classe Usuario, declara os dados do dicionario na classe
                    objeto=Usuario(cadastro_usuarios[objeto][1],cadastro_usuarios[objeto][2],cadastro_usuarios[objeto][3],cadastro_usuarios[objeto][4])
                    cadastro_usuarios_classe.update({email_cadastro:objeto}) #Salva a referencia da classe no segundo dicionário com o email como chave, para facilitar encontrar os objetos.
            print("USUÁRIO CADASTRADO")
        else:
            print("USUÁRIO JÁ EXISTENTE")
    elif opcao_geral=='2': #Opção para fazer login em algum usuario cadastrado
    
        print("LOGIN") 
        email_login=input("Digite seu email: ")
        if email_login in cadastro_usuarios: #Verificar se o usuário existe (se o email digitado foi salvo no dicionario na opção 1)
            senha_login=input("Digite sua senha: ")
            if senha_login==cadastro_usuarios[email_login][0]: #Checa se a senha digitada corresponde à senha salva para aquele email
                usuario_logado=cadastro_usuarios_classe[email_login] #A variável usuario_logado recebe a referência ao objeto no valor que corresponde ao email de login (para facilitar).
                opcao_login='' #Variável inicia vazia e vai receber numeros de 1 a 12, para as opções ao longo do programa (str)
                while opcao_login!='12': #Loop até digitar a opção 12 (logoff)
                    lista_objetos_usuarios=[] #Lista inicia vazia, posteriormente vai receber a referencia aos objetos dos usuarios diferentes do usuario logado, para as opções 2 e 11
                    print(f"Bem Vindo(a), {usuario_logado.nome}. O que deseja fazer?")
                    opcao_login=input("1-Postar \n2-Adicionar Amigo \n3-Adicionar Melhor Amigo \n4-Buscar Amigo \n5-Buscar Post \n6-Ver Número de Amigos \n7-Ver Número de Posts \n8-Ver Posts dos Amigos \n9-Adicionar Interesses \n10-Desfazer Amizade \n11-Bloquear Usuário \n12-LOGOFF")
                    
                    if opcao_login=='1': #Opção para postar
                        print("NOVO POST")
                        novo_post=input("Digite o que deseja postar: ")
                        usuario_logado.postar(novo_post)
                    
                    elif opcao_login=='2': #Opção de adicionar amigo
                        if len(cadastro_usuarios)>1: #Verifica se há algum usuário cadastrado além do usuário que fez login
                            print("ADICIONAR AMIGO \n LISTA DE USUARIOS CADASTRADOS:")
                            for usuario in cadastro_usuarios_classe: #Percorre o dicionario dos usuarios salvos na classe (email:objeto)
                                if (cadastro_usuarios_classe[usuario])!=(usuario_logado): #Para os usuários diferente do usuário logado, busca o objeto e salva na lista de objetos
                                    lista_objetos_usuarios.append(cadastro_usuarios_classe[usuario])
                            opcao_confirmar_amizade='' #Opção para confirmar a solicitação de amizade. Inicia vazia, e vai receber S ou N (str)       
                            while opcao_confirmar_amizade!='S' and opcao_confirmar_amizade!='N': #Fica em loop até o usuário digitar S ou N
                                for i in range(len(lista_objetos_usuarios)):
                                    print(f"{i} - {lista_objetos_usuarios[i].nome}") #printa o nome dos usuários disponíveis, junto com o indice na lista de referencias                                
                                opcao_amigo=input("Qual usuário deseja adicionar como amigo?: ") #variável vai receber o número do amigo que o usuario quer adicionar como amigo (int)
                                while True: #Procedimento de verificação necessário por utilizar a entrada como índice da lista de amigos. Entradas diferentes de 'int' irão travar o programa.
                                    try:
                                        opcao_amigo=int(opcao_amigo)
                                        break
                                    except:
                                        opcao_amigo=input("ERRO: DIGITE APENAS O NÚMERO DO USUÁRIO QUE DESEJA ADICIONAR")
                                if 0<=opcao_amigo<len(lista_objetos_usuarios): #Verifica se o numero digitado corresponde a algum usuário
                                    opcao_confirmar_amizade = input(f"Usuário Selecionado: {lista_objetos_usuarios[opcao_amigo].nome}. Confirma Amizade? \nS - CONFIRMA \nN - SAIR")
                                    opcao_confirmar_amizade = opcao_confirmar_amizade.upper()
                                    if opcao_confirmar_amizade == "S":
                                        if lista_objetos_usuarios[opcao_amigo] not in usuario_logado.lista_bloqueados:
                                            usuario_logado.adiciona_amigo(lista_objetos_usuarios[opcao_amigo]) #se o usuário selecionado não estiver na lista de bloqueados, adiciona aos amigos.
                                        else:
                                            print("Não foi possível adicionar este usuário")
                                    elif opcao_confirmar_amizade == "N":
                                        print("OPERAÇÃO CANCELADA")
                                    else:
                                        print("ENTRADA INCORRETA: FAVOR DIGITAR APENAS S OU N")
                                else:
                                    print("NÚMERO INEXISTENTE: POR FAVOR, DIGITE O NÚMERO DO USUÁRIO QUE DESEJA ADICIONAR COMO AMIGO")   
                        else:
                            print("NENHUM OUTRO USUÁRIO CADASTRADO")
                    
                    elif opcao_login=='3': #opção de adicionar melhor amigo
                        if len(usuario_logado.lista_amigos)>0: #Verifica se o usuário atual possui amigos adicionados antes de entrar na opção
                            print("ADICIONAR MELHOR AMIGO")
                            for amigo in usuario_logado.lista_amigos: #percorre a lista de amigos do usuario 
                                print(f"{usuario_logado.lista_amigos.index(amigo)} - {amigo.nome}") #printa o nome dos amigos e o indice dos mesmos para seleção
                            opcao_melhor_amigo=input("Qual amigo deseja transformar em melhor amigo?: ") #variável vai receber o numero correspondente ao usuario para adicionar como melhor amigo (int)
                            while True: #Procedimento de verificação necessário por utilizar a entrada como índice da lista de amigos. Entradas diferentes de 'int' irão travar o programa
                                try:
                                    opcao_melhor_amigo=int(opcao_melhor_amigo)
                                    break
                                except:
                                    opcao_melhor_amigo=input("ERRO: DIGITE APENAS O NÚMERO CORRESPONDENTE AO AMIGO")
                            if 0<=opcao_melhor_amigo<len(usuario_logado.lista_amigos): #verifica se o numero digitado corresponde a algum dos amigos
                                usuario_logado.adiciona_melhor_amigo(usuario_logado.lista_amigos[opcao_melhor_amigo]) #salva o amigo escolhido na lista de melhores amigos do usuario
                            else:
                                print("NÚMERO INEXISTENTE. POR FAVOR DIGITE O NUMERO CORRESPONDENTE AO AMIGO")
                        else:
                            print("Sua lista de amigos está vazia :(")
                    
                    elif opcao_login=='4': #Opção de buscar amigo
                        if (len(usuario_logado.lista_melhores_amigos)>0) or (len(usuario_logado.lista_amigos)>0): #verifica se o usuário atual possui algum amigo ou melhor amigo
                            print("BUSCAR AMIGO")
                            busca_amigo=input("Digite o que deseja buscar: ") #variável recebe o que vai ser buscado (str)
                            if len(usuario_logado.buscar_amigo(busca_amigo))>0: #verifica se o método de buscar amigos retornou algum resultado
                                print("Amigos Encontrados:")
                                for i in range (len(usuario_logado.buscar_amigo(busca_amigo))):
                                    print(usuario_logado.buscar_amigo(busca_amigo)[i]) #Printa os resultados encontrados entre os nomes de amigos
                            else:
                                print("Não há resultados")
                        else:
                            print("Não há amigos adicionados")
                    
                    elif opcao_login=='5': #Opção de buscar postagem
                        resultados_posts=0 #Contador genérico, inicia em 0, vai verificar se houve algum resultado nas buscas por posts
                        print("BUSCAR POST")
                        busca_posts=input("Digite o que deseja buscar: ") 
                        for usuario in cadastro_usuarios_classe: #Varre o dicionario de objetos cadastrados na classe, para executar a busca de posts em todos os usuarios
                            if len(cadastro_usuarios_classe[usuario].buscar_post(busca_posts))>0: #Verifica se a lista de resultados da busca de posts não está vazia
                                for i in range (len(cadastro_usuarios_classe[usuario].buscar_post(busca_posts))): #Varre a lista de resultados da busca de posts
                                    print(f"{cadastro_usuarios_classe[usuario].nome} : {cadastro_usuarios_classe[usuario].buscar_post(busca_posts)[i]}")
                                    resultados_posts+=1 #printa o nome do usuario e a postagem encontrada, e soma um ao contador genérico de resultados
                        if resultados_posts==0:
                            print("Nenhum resultado encontrado")
                    
                    elif opcao_login=='6': #Opção de mostrar número de amigos
                        if (len(usuario_logado.lista_melhores_amigos)>0) or (len(usuario_logado.lista_amigos)>0): #verifica se o usuario logado possui algum amigo ou melhor amigo
                            print("NÚMERO DE AMIGOS ADICIONADOS")
                            usuario_logado.mostra_numero_amigos()
                        else:
                            print('Não há amigos adicionados')
                    
                    elif opcao_login=='7': #Opção de mostrar o número de posts feitos
                        if len(usuario_logado.lista_posts)>0: #verifica se o usuario logado tem alguma postagem
                            print("NÚMERO DE POSTAGENS")
                            usuario_logado.mostra_numero_posts()
                        else:
                            print("Não há postagens")
                    
                    elif opcao_login=='8': #Opção para mostrar todos os posts (Melhores amigos antes)
                        quantidade_postagens=0 #contador genérico para as postagens feitas pelos amigos 
                        if (len(usuario_logado.lista_melhores_amigos)>0) or (len(usuario_logado.lista_amigos)>0): #verifica se o usuario logado possui algum amigo ou melhor amigo
                            for melhor_amigo in usuario_logado.lista_melhores_amigos: #Varre a lista de melhores amigos do usuario
                                if len(melhor_amigo.lista_posts)>0: #caso o melhor amigo do usuario tenha alguma postagem, executa o comando de mostrar postagem
                                    usuario_logado.mostra_posts_amigo(melhor_amigo)
                                    quantidade_postagens+=1
                            for amigo in usuario_logado.lista_amigos:#Varre depois a lista de amigos do usuario
                                if len(amigo.lista_posts)>0:#caso o amigo tenha alguma postagem, executa o mesmo comando de mostrar postagem
                                    usuario_logado.mostra_posts_amigo(amigo)
                                    quantidade_postagens+=1
                            if quantidade_postagens==0:
                                print("Nenhum amigo fez postagens")
                        else:
                            print('Não há amigos adicionados')
                    
                    elif opcao_login=='9': #Opção de adicionar interesse
                        print("ADICIONAR INTERESSE")
                        novo_interesse=input("Digite o interesse que deseja adicionar: ")
                        usuario_logado.adiciona_interesse(novo_interesse)
                    
                    elif opcao_login=='10': #Opção de Desfazer Amizade
                        if len(cadastro_usuarios)>1:
                            lista_todos_amigos=[] #lista inicia vazia, vai receber os objetos de todos os usuarios adicionados como amigo ou melhor amigo
                            if (len(usuario_logado.lista_melhores_amigos)>0) or (len(usuario_logado.lista_amigos)>0):
                                print('DESFAZER AMIZADE')
                                for amigo in usuario_logado.lista_amigos: #percorre a lista de amigos do usuario e salva na lista acima
                                    lista_todos_amigos.append(amigo)
                                for melhor_amigo in usuario_logado.lista_melhores_amigos: #percorre a lista de melhores amigos e salva na lista acima
                                    lista_todos_amigos.append(melhor_amigo)
                                print("Lista de amigos: ")
                                for amigo in lista_todos_amigos: #printa a lista do nome de todos os amigos e melhores amigos, com seus indices para seleção
                                    print(f"{lista_todos_amigos.index(amigo)} - {amigo.nome}")
                                opcao_desfazer_amizade=input("Qual amigo deseja excluir?: ") #recebe o indice do amigo que se deseja excluir (int)
                                while True: #Procedimento de verificação necessário por utilizar a entrada como índice da lista de amigos. Entradas diferentes de 'int' irão travar o programa.
                                    try:
                                        opcao_desfazer_amizade=int(opcao_desfazer_amizade)
                                        break
                                    except:
                                        opcao_desfazer_amizade=input("ERRO: DIGITE APENAS O NÚMERO CORRESPONDENTE AO AMIGO")
                                if 0<=opcao_desfazer_amizade<len(lista_todos_amigos):
                                    usuario_logado.desfazer_amizade(lista_todos_amigos[opcao_desfazer_amizade]) #desfaz a amizade com o usuario do indice selecionado
                                else:
                                    print("NÚMERO INEXISTENTE. POR FAVOR DIGITE O NUMERO CORRESPONDENTE AO AMIGO")    
                            else:
                                print('Não há amigos adicionados')
                        else:
                            print("NENHUM OUTRO USUÁRIO CADASTRADO")

                    elif opcao_login=='11': #Opção de bloquear
                        if len(cadastro_usuarios)>1:
                            print("BLOQUEAR USUARIO \n LISTA DE USUARIOS CADASTRADOS:")
                            for usuario in cadastro_usuarios_classe: #percorre todos os usuarios cadastrados (objetos) e salva os mesmos, utiliza a mesma lista da opção 2
                                if (cadastro_usuarios_classe[usuario])!=(usuario_logado):
                                    lista_objetos_usuarios.append(cadastro_usuarios_classe[usuario])
                            opcao_confirmar_bloqueio=''        
                            while opcao_confirmar_bloqueio!='S' and opcao_confirmar_bloqueio!='N':
                                for i in range(len(lista_objetos_usuarios)):
                                    print(f"{i} - {lista_objetos_usuarios[i].nome}")    #Mesmo procedimento do passo de adicionar amigo                            
                                opcao_bloqueio=input("Qual usuário deseja bloquear?: ") #variável vai receber o indice do usuario que se deseja bloquear
                                while True: #Procedimento de verificação necessário por utilizar a entrada como índice da lista de amigos. Entradas diferentes de 'int' irão travar o programa.
                                    try:
                                        opcao_bloqueio=int(opcao_bloqueio)
                                        break
                                    except:
                                        opcao_bloqueio=input("ERRO: DIGITE APENAS O NÚMERO DO USUÁRIO QUE DESEJA BLOQUEAR")
                                if 0<=opcao_bloqueio<len(lista_objetos_usuarios):
                                    opcao_confirmar_bloqueio = input(f"Usuário Selecionado: {lista_objetos_usuarios[opcao_bloqueio].nome}. Confirma Bloqueio? \nS - CONFIRMA \nN - SAIR")
                                    opcao_confirmar_bloqueio = opcao_confirmar_bloqueio.upper()
                                    if opcao_confirmar_bloqueio == "S":
                                        usuario_logado.bloquear(lista_objetos_usuarios[opcao_bloqueio])
                                    elif opcao_confirmar_amizade == "N":
                                        print("OPERAÇÃO CANCELADA")
                                    else:
                                        print("ENTRADA INCORRETA: FAVOR DIGITAR APENAS S OU N")
                                else:
                                    print("NÚMERO INEXISTENTE: POR FAVOR, DIGITE O NÚMERO DO USUÁRIO QUE DESEJA BLOQUEAR")   
                        else:
                            print("NENHUM OUTRO USUÁRIO CADASTRADO")
                    
                    elif opcao_login=='12': #Opção de Sair
                        print("SAINDO...")
                    else:
                        print("ENTRADA INVÁLIDA")                    
            else:
                print("SENHA INCORRETA")
        else:
            print("USUÁRIO NÃO CADASTRADO")
    elif opcao_geral=='3':
        print("ENCERRANDO...")
    else:
        print("OPÇÃO NÃO RECONHECIDA. POR FAVOR, SELECIONE 1,2 OU 3")
print("OBRIGADO POR USAR O PYTHONBOOK. ZUCKERBERG QUE SE CUIDE!")