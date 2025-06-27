from dataclasses import dataclass

# === DATACLASSES ===
@dataclass
class Livro:
    codigo: str
    titulo: str
    autor: str
    ano: int
    genero: str
    quantidade_total: int
    quantidade_disponivel: int

@dataclass
class Usuario:
    id_usuario: str
    nome: str
    tipo: str  # "aluno" ou "professor"

@dataclass
class Emprestimo:
    id_usuario: str
    codigo_livro: str
    dia_emprestimo: int
    dia_devolucao_prevista: int
    status: str  # "ativo" ou "devolvido"
    dia_devolucao_efetiva: int = None

# === VARIÁVEIS GLOBAIS ===
livros = []
usuarios = []
emprestimos = []
dia_atual_sistema = 1
VALOR_MULTA_POR_DIA = 1.00

# === FUNÇÕES LIVROS ===
def menu_gerenciar_livros():
    while True:
        print("\n--- Gerenciar Livros ---")
        print("1. Cadastrar Novo Livro")
        print("2. Listar Todos os Livros")
        print("3. Buscar Livro")
        print("4. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

def cadastrar_livro():
    codigo = input("Código: ")
    if any(livro.codigo == codigo for livro in livros):
        print("Código já cadastrado.")
        return
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano de publicação: "))
    genero = input("Gênero: ")
    qtd = int(input("Quantidade de exemplares: "))
    livro = Livro(codigo, titulo, autor, ano, genero, qtd, qtd)
    livros.append(livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    for livro in livros:
        print(livro)

def buscar_livro():
    termo = input("Digite código, título ou autor: ").lower()
    for livro in livros:
        if termo in livro.codigo.lower() or termo in livro.titulo.lower() or termo in livro.autor.lower():
            print(livro)

# === FUNÇÕES USUÁRIOS ===
def menu_gerenciar_usuarios():
    while True:
        print("\n--- Gerenciar Usuários ---")
        print("1. Cadastrar Novo Usuário")
        print("2. Listar Todos os Usuários")
        print("3. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

def cadastrar_usuario():
    id_usuario = input("ID do usuário: ")
    if any(usuario.id_usuario == id_usuario for usuario in usuarios):
        print("ID já cadastrado.")
        return
    nome = input("Nome: ")
    tipo = input("Tipo (aluno/professor): ").lower()
    if tipo not in ["aluno", "professor"]:
        print("Tipo inválido.")
        return
    usuario = Usuario(id_usuario, nome, tipo)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    for usuario in usuarios:
        print(usuario)

# === FUNÇÕES EMPRÉSTIMO ===
def realizar_emprestimo():
    global dia_atual_sistema
    id_usuario = input("ID do Usuário: ")
    codigo_livro = input("Código do Livro: ")

    usuario = next((u for u in usuarios if u.id_usuario == id_usuario), None)
    livro = next((l for l in livros if l.codigo == codigo_livro), None)

    if not usuario:
        print("Usuário não encontrado.")
        return
    if not livro:
        print("Livro não encontrado.")
        return
    if livro.quantidade_disponivel <= 0:
        print("Livro indisponível.")
        return

    prazo = 7 if usuario.tipo == "aluno" else 10
    dia_previsto = dia_atual_sistema + prazo

    emprestimo = Emprestimo(id_usuario, codigo_livro, dia_atual_sistema, dia_previsto, "ativo")
    emprestimos.append(emprestimo)
    livro.quantidade_disponivel -= 1
    print("Empréstimo realizado com sucesso!")

# === FUNÇÕES DEVOLUÇÃO ===
def realizar_devolucao():
    global dia_atual_sistema
    id_usuario = input("ID do Usuário: ")
    codigo_livro = input("Código do Livro: ")

    for emprestimo in emprestimos:
        if (emprestimo.id_usuario == id_usuario and
            emprestimo.codigo_livro == codigo_livro and
            emprestimo.status == "ativo"):
            emprestimo.dia_devolucao_efetiva = dia_atual_sistema
            emprestimo.status = "devolvido"
            livro = next((l for l in livros if l.codigo == codigo_livro), None)
            if livro:
                livro.quantidade_disponivel += 1
            atraso = dia_atual_sistema - emprestimo.dia_devolucao_prevista
            if atraso > 0:
                multa = atraso * VALOR_MULTA_POR_DIA
                print(f"Devolvido com {atraso} dias de atraso. Multa: R${multa:.2f}")
            else:
                print("Devolução realizada no prazo.")
            return
    print("Empréstimo não encontrado ou já devolvido.")

# === FUNÇÕES RELATÓRIOS ===
def menu_relatorios():
    print("\n--- Relatórios ---")
    print("1. Livros Emprestados Atualmente")
    print("2. Livros com Devolução em Atraso")
    print("3. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        for emp in emprestimos:
            if emp.status == "ativo":
                livro = next((l for l in livros if l.codigo == emp.codigo_livro), None)
                usuario = next((u for u in usuarios if u.id_usuario == emp.id_usuario), None)
                print(f"{livro.titulo} - {usuario.nome} - Previsto: Dia {emp.dia_devolucao_prevista}")
    elif opcao == '2':
        for emp in emprestimos:
            if emp.status == "ativo" and emp.dia_devolucao_prevista < dia_atual_sistema:
                livro = next((l for l in livros if l.codigo == emp.codigo_livro), None)
                usuario = next((u for u in usuarios if u.id_usuario == emp.id_usuario), None)
                atraso = dia_atual_sistema - emp.dia_devolucao_prevista
                print(f"{livro.titulo} - {usuario.nome} - {atraso} dias de atraso")
    elif opcao == '3':
        return
    else:
        print("Opção inválida.")

# === GERENCIAR TEMPO ===
def menu_gerenciar_tempo(dia_sistema_atual_param):
    while True:
        print("\n--- Gerenciar Tempo ---")
        print(f"Dia Atual do Sistema: {dia_sistema_atual_param}")
        print("1. Avançar 1 dia")
        print("2. Avançar 7 dias")
        print("3. Avançar N dias")
        print("4. Consultar dia atual")
        print("5. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            dia_sistema_atual_param += 1
        elif opcao == '2':
            dia_sistema_atual_param += 7
        elif opcao == '3':
            try:
                n = int(input("Quantos dias deseja avançar? "))
                if n > 0:
                    dia_sistema_atual_param += n
            except:
                print("Entrada inválida.")
        elif opcao == '4':
            print(f"Dia atual: {dia_sistema_atual_param}")
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")
    return dia_sistema_atual_param

# === MENU PRINCIPAL ===
def menu_principal():
    global dia_atual_sistema
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Usuários")
        print("3. Realizar Empréstimo")
        print("4. Realizar Devolução")
        print("5. Relatórios")
        print("6. Gerenciar Tempo")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_gerenciar_livros()
        elif opcao == '2':
            menu_gerenciar_usuarios()
        elif opcao == '3':
            realizar_emprestimo()
        elif opcao == '4':
            realizar_devolucao()
        elif opcao == '5':
            menu_relatorios()
        elif opcao == '6':
            dia_atual_sistema = menu_gerenciar_tempo(dia_atual_sistema)
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

# === EXECUÇÃO ===
if __name__ == '__main__':
    menu_principal()