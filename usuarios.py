lista_usuarios = []
while True:
        print("===================================")
        print("         MENU DE USUÁRIOS             ")
        print("===================================")
        print("1. Cadastrar novo usuario")
        print("2. Listar usuarios")
        print("3. Ativar/Inativar usuario")
        print("4. Voltar ao menu principal")
        print("===================================")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_novo_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
           ativar_inativar_usuario()
        elif opcao == "4":
            return voltar
        else:
            print("Opção inválida. Tente novamente.")



        def cadastrar_novo_usuario():
    
           while True:
            print("\n----------------------- CADASTRAR NOVO USUÁRIO ----------------------------")

        nome = input("Nome Completo:").strip()
        login = input("login: ").strip()
        
        # Verifica se o login já existe
        if any(usuario[ "Login"] == login for usuario in lista_usuarios):
            print("Esse Login já está cadrastado. Tente outro.")
            continue
        
        status = input("Ativo/Inativo: ").strip().capitalize()
        if status not in ["Ativo", "Inativo"]:
            print("Status inválido. Por favor, digite 'Ativo' ou 'Inativo'.")
            continue
        
       
        
        usuario = {
            "Nome": nome,
            "Login": login,
            "Status": status
            
        }

        # Adicionar na lista de alunos
        lista_usuarios.append(usuario)
        print("Usuário cadrastado com sucesso!!")

        continuar = input("Deseja cadastrar um novo usuário? (s/n): ").lower()
        if continuar !=  "s":
            break
           
# =================== LISTAR USUÁRIOS ===================

def listar_usuarios():
    print("\n----------------------- LISTAR USUÁRIOS ----------------------------")
   
   
    print("----------------------- LISTA DE USUÁRIOS ----------------------------")
    for i, usuario in enumerate(lista_usuarios, start=1):
        print(f"{i}. Nome. {usuario['Nome']} | login: {usuario['Login']} | status: {usuario['status']}")
        print("------------------------------------------------------------------")



    print("----------------------- ATIVAR/INATIVAR USUÁRIO ----------------------------")
    def ativar_inativar_usuario():
     listar_usuarios = ():

    if not lista_usuarios:
        return
    
    login = input("\n Digite o login do usuário para alterar o status (ou digite 'voltar' para cancelar): ").strip()
    if login.lower() == 'voltar':
        return
    
    for usuario in lista_usuarios:
        if usuario['Login'] == login:
            status_atual = usuario['Status']
            print(f"Status atual do usuário {usuario['Nome']}: {status_atual}")

            novo_status = input("Digite o novo status (Ativo/Inativo) ou deixe em branco para manter o status atual: ").strip().capitalize()
            if novo_status not in ['Ativo', 'Inativo']:
                print("Status inválido. Por favor, use 'Ativo' ou 'Inativo'.")
                return

            usuario['status'] = novo_status 
            print(f"Status de {usuario['Nome']} alterado para {novo_status}.")
            return
        print("Usuário não encontrado.")
        
