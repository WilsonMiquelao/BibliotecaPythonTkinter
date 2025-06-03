class Livro:
    def __init__(self, titulo, autor, ID):
        self.titulo = titulo
        self.autor = autor
        self.ID = ID
        self.status_emprestimo = "disponível"

class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def emprestar_livro(self, livro, membro):
        if livro.status_emprestimo == "disponível":
            livro.status_emprestimo = "emprestado"
            membro.historico_emprestimos.append(livro)
        else:
            print("O livro não está disponível para empréstimo.")

    def devolver_livro(self, livro, membro):
        if livro in membro.historico_emprestimos:
            livro.status_emprestimo = "disponível"
            membro.historico_emprestimos.remove(livro)
        else:
            print("Este livro não foi emprestado por este membro.")

    def pesquisar_livro_por_titulo(self, titulo):
        for livro in self.catalogo:
            if livro.titulo == titulo:
                return livro
        return None

    def pesquisar_livro_por_autor(self, autor):
        resultados = [livro for livro in self.catalogo if livro.autor == autor]
        return resultados

    def pesquisar_livro_por_ID(self, ID):
        for livro in self.catalogo:
            if livro.ID == ID:
                return livro
        return None
    
    import tkinter as tk

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.biblioteca = Biblioteca()
        
        self.label = tk.Label(root, text="Bem-vindo à Biblioteca!")
        self.label.pack()
        
        self.opcoes_frame = tk.Frame(root)
        self.opcoes_frame.pack()
        
        self.adicionar_livro_btn = tk.Button(self.opcoes_frame, text="Adicionar Livro", command=self.adicionar_livro)
        self.adicionar_livro_btn.pack(side=tk.LEFT)
        
        self.adicionar_membro_btn = tk.Button(self.opcoes_frame, text="Adicionar Membro", command=self.adicionar_membro)
        self.adicionar_membro_btn.pack(side=tk.LEFT)
        
        self.emprestar_livro_btn = tk.Button(self.opcoes_frame, text="Emprestar Livro", command=self.emprestar_livro)
        self.emprestar_livro_btn.pack(side=tk.LEFT)
        
        self.devolver_livro_btn = tk.Button(self.opcoes_frame, text="Devolver Livro", command=self.devolver_livro)
        self.devolver_livro_btn.pack(side=tk.LEFT)
        
        self.pesquisar_livro_btn = tk.Button(self.opcoes_frame, text="Pesquisar Livro", command=self.pesquisar_livro)
        self.pesquisar_livro_btn.pack(side=tk.LEFT)
    
    def adicionar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ID = input("Digite o ID do livro: ")
        
        livro = Livro(titulo, autor, ID)
        self.biblioteca.adicionar_livro(livro)
        print("Livro adicionado com sucesso!")
    
    def adicionar_membro(self):
        nome = input("Digite o nome do membro: ")
        numero_membro = input("Digite o número do membro: ")
        
        membro = Membro(nome, numero_membro)
        self.biblioteca.adicionar_membro(membro)
        print("Membro adicionado com sucesso!")
    
    def emprestar_livro(self):
        num_membro = input("Digite o número do membro: ")
        titulo_livro = input("Digite o título do livro a ser emprestado: ")
        
        membro = self.biblioteca.encontrar_membro_por_numero(num_membro)
        livro = self.biblioteca.pesquisar_livro_por_titulo(titulo_livro)
        
        if membro and livro:
            self.biblioteca.emprestar_livro(livro, membro)
            print("Livro emprestado com sucesso!")
        else:
            print("Membro ou livro não encontrado.")
    
    def devolver_livro(self):
        num_membro = input("Digite o número do membro: ")
        titulo_livro = input("Digite o título do livro a ser devolvido: ")
        
        membro = self.biblioteca.encontrar_membro_por_numero(num_membro)
        livro = self.biblioteca.pesquisar_livro_por_titulo(titulo_livro)
        
        if membro and livro:
            self.biblioteca.devolver_livro(livro, membro)
            print("Livro devolvido com sucesso!")
        else:
            print("Membro ou livro não encontrado.")
    
    def pesquisar_livro(self):
        criterio = input("Deseja pesquisar por título, autor ou ID? ")
        
        if criterio == "titulo":
            titulo = input("Digite o título do livro: ")
            livro = self.biblioteca.pesquisar_livro_por_titulo(titulo)
        elif criterio == "autor":
            autor = input("Digite o autor do livro: ")
            livros = self.biblioteca.pesquisar_livro_por_autor(autor)
            for livro in livros:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, ID: {livro.ID}")
        elif criterio == "ID":
            ID = input("Digite o ID do livro: ")
            livro = self.biblioteca.pesquisar_livro_por_ID(ID)