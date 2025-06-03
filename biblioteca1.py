import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Frame, Label, Entry, Button, Listbox, Scrollbar

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
            return True
        else:
            return False

    def devolver_livro(self, livro, membro):
        if livro in membro.historico_emprestimos:
            livro.status_emprestimo = "disponível"
            membro.historico_emprestimos.remove(livro)
            return True
        else:
            return False

    def pesquisar_livro_por_titulo(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def pesquisar_livro_por_autor(self, autor):
        resultados = [livro for livro in self.catalogo if livro.autor.lower() == autor.lower()]
        return resultados
    
    def encontrar_membro_por_numero(self, numero):
        for membro in self.membros:
            if membro.numero_membro == numero:
                return membro
        return None

    def pesquisar_livro_por_ID(self, ID):
        for livro in self.catalogo:
            if livro.ID.lower() == ID.lower():
                return livro
        return None


class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.biblioteca = Biblioteca()
        
        self.label = tk.Label(root, text="Bem-vindo à Biblioteca!", font=('Arial', 14))
        self.label.pack(pady=10)
        
        self.opcoes_frame = tk.Frame(root)
        self.opcoes_frame.pack(pady=20)
        
        # Botões com estilo melhorado
        button_style = {'width': 20, 'height': 2, 'font': ('Arial', 10)}
        
        self.adicionar_livro_btn = tk.Button(self.opcoes_frame, text="Adicionar Livro", 
                                            command=self.adicionar_livro, **button_style)
        self.adicionar_livro_btn.grid(row=0, column=0, padx=10, pady=5)
        
        self.adicionar_membro_btn = tk.Button(self.opcoes_frame, text="Adicionar Membro", 
                                            command=self.adicionar_membro, **button_style)
        self.adicionar_membro_btn.grid(row=0, column=1, padx=10, pady=5)
        
        self.emprestar_livro_btn = tk.Button(self.opcoes_frame, text="Emprestar Livro", 
                                           command=self.emprestar_livro, **button_style)
        self.emprestar_livro_btn.grid(row=1, column=0, padx=10, pady=5)
        
        self.devolver_livro_btn = tk.Button(self.opcoes_frame, text="Devolver Livro", 
                                          command=self.devolver_livro, **button_style)
        self.devolver_livro_btn.grid(row=1, column=1, padx=10, pady=5)
        
        self.pesquisar_livro_btn = tk.Button(self.opcoes_frame, text="Pesquisar Livro", 
                                           command=self.pesquisar_livro, **button_style)
        self.pesquisar_livro_btn.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Área de status
        self.status_frame = tk.Frame(root, borderwidth=2, relief="groove")
        self.status_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.status_label = tk.Label(self.status_frame, text="Status:", font=('Arial', 12))
        self.status_label.pack(anchor="w")
        
        self.status_text = tk.Text(self.status_frame, height=10, wrap="word", state="disabled")
        self.status_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(self.status_text)
        scrollbar.pack(side="right", fill="y")
        scrollbar.config(command=self.status_text.yview)
        self.status_text.config(yscrollcommand=scrollbar.set)
    
    def atualizar_status(self, mensagem):
        self.status_text.config(state="normal")
        self.status_text.insert("end", mensagem + "\n")
        self.status_text.see("end")
        self.status_text.config(state="disabled")
    
    def criar_janela_entrada(self, titulo, campos):
        janela = Toplevel(self.root)
        janela.title(titulo)
        janela.transient(self.root)
        janela.grab_set()
        
        entries = {}
        for i, (label_text, default) in enumerate(campos.items()):
            frame = Frame(janela)
            frame.pack(fill="x", padx=5, pady=5)
            
            label = Label(frame, text=label_text, width=15)
            label.pack(side="left")
            
            entry = Entry(frame)
            entry.insert(0, default)
            entry.pack(side="left", fill="x", expand=True)
            entries[label_text] = entry
        
        return janela, entries
    
    def adicionar_livro(self):
        janela, entries = self.criar_janela_entrada(
            "Adicionar Livro",
            {"Título": "", "Autor": "", "ID": ""}
        )
        
        def confirmar():
            titulo = entries["Título"].get()
            autor = entries["Autor"].get()
            ID = entries["ID"].get()
            
            if not titulo or not autor or not ID:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
                return
            
            livro = Livro(titulo, autor, ID)
            self.biblioteca.adicionar_livro(livro)
            self.atualizar_status(f"Livro adicionado: {titulo} por {autor} (ID: {ID})")
            janela.destroy()
        
        Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
    
    def adicionar_membro(self):
        janela, entries = self.criar_janela_entrada(
            "Adicionar Membro",
            {"Nome": "", "Número de Membro": ""}
        )
        
        def confirmar():
            nome = entries["Nome"].get()
            numero_membro = entries["Número de Membro"].get()
            
            if not nome or not numero_membro:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
                return
            
            # Verificar se número de membro já existe
            if self.biblioteca.encontrar_membro_por_numero(numero_membro):
                messagebox.showerror("Erro", "Número de membro já existe!")
                return
            
            membro = Membro(nome, numero_membro)
            self.biblioteca.adicionar_membro(membro)
            self.atualizar_status(f"Membro adicionado: {nome} (Número: {numero_membro})")
            janela.destroy()
        
        Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
    
    def emprestar_livro(self):
        janela, entries = self.criar_janela_entrada(
            "Emprestar Livro",
            {"Número do Membro": "", "Título do Livro": ""}
        )
        
        def confirmar():
            num_membro = entries["Número do Membro"].get()
            titulo_livro = entries["Título do Livro"].get()
            
            if not num_membro or not titulo_livro:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
                return
            
            membro = self.biblioteca.encontrar_membro_por_numero(num_membro)
            livro = self.biblioteca.pesquisar_livro_por_titulo(titulo_livro)
            
            if not membro:
                messagebox.showerror("Erro", "Membro não encontrado!")
                return
            if not livro:
                messagebox.showerror("Erro", "Livro não encontrado!")
                return
            
            if self.biblioteca.emprestar_livro(livro, membro):
                self.atualizar_status(f"Livro '{livro.titulo}' emprestado para {membro.nome}")
            else:
                messagebox.showerror("Erro", "Livro não está disponível para empréstimo!")
            
            janela.destroy()
        
        Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
    
    def devolver_livro(self):
        janela, entries = self.criar_janela_entrada(
            "Devolver Livro",
            {"Número do Membro": "", "Título do Livro": ""}
        )
        
        def confirmar():
            num_membro = entries["Número do Membro"].get()
            titulo_livro = entries["Título do Livro"].get()
            
            if not num_membro or not titulo_livro:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
                return
            
            membro = self.biblioteca.encontrar_membro_por_numero(num_membro)
            livro = self.biblioteca.pesquisar_livro_por_titulo(titulo_livro)
            
            if not membro:
                messagebox.showerror("Erro", "Membro não encontrado!")
                return
            if not livro:
                messagebox.showerror("Erro", "Livro não encontrado!")
                return
            
            if self.biblioteca.devolver_livro(livro, membro):
                self.atualizar_status(f"Livro '{livro.titulo}' devolvido por {membro.nome}")
            else:
                messagebox.showerror("Erro", "Este livro não foi emprestado por este membro!")
            
            janela.destroy()
        
        Button(janela, text="Confirmar", command=confirmar).pack(pady=10)
    
    def pesquisar_livro(self):
        janela = Toplevel(self.root)
        janela.title("Pesquisar Livro")
        
        Label(janela, text="Pesquisar por:").pack(pady=5)
        
        var = tk.StringVar(value="titulo")
        
        Radiobutton(janela, text="Título", variable=var, value="titulo").pack(anchor="w")
        Radiobutton(janela, text="Autor", variable=var, value="autor").pack(anchor="w")
        Radiobutton(janela, text="ID", variable=var, value="ID").pack(anchor="w")
        
        Label(janela, text="Termo de pesquisa:").pack(pady=5)
        entry = Entry(janela)
        entry.pack(fill="x", padx=5)
        
        def pesquisar():
            criterio = var.get()
            termo = entry.get()
            
            if not termo:
                messagebox.showerror("Erro", "Digite um termo de pesquisa!")
                return
            
            if criterio == "titulo":
                livro = self.biblioteca.pesquisar_livro_por_titulo(termo)
                if livro:
                    self.mostrar_resultado(livro)
                else:
                    messagebox.showinfo("Resultado", "Nenhum livro encontrado com este título.")
            elif criterio == "autor":
                livros = self.biblioteca.pesquisar_livro_por_autor(termo)
                if livros:
                    self.mostrar_resultado(livros)
                else:
                    messagebox.showinfo("Resultado", "Nenhum livro encontrado deste autor.")
            elif criterio == "ID":
                livro = self.biblioteca.pesquisar_livro_por_ID(termo)
                if livro:
                    self.mostrar_resultado(livro)
                else:
                    messagebox.showinfo("Resultado", "Nenhum livro encontrado com este ID.")
            
            janela.destroy()
        
        Button(janela, text="Pesquisar", command=pesquisar).pack(pady=10)
    
    def mostrar_resultado(self, resultado):
        if isinstance(resultado, list):  # Lista de livros (pesquisa por autor)
            janela = Toplevel(self.root)
            janela.title("Resultados da Pesquisa")
            
            listbox = Listbox(janela, width=80, height=15)
            scrollbar = Scrollbar(janela, orient="vertical", command=listbox.yview)
            listbox.config(yscrollcommand=scrollbar.set)
            
            for livro in resultado:
                status = "Disponível" if livro.status_emprestimo == "disponível" else "Emprestado"
                listbox.insert("end", 
                             f"Título: {livro.titulo} | Autor: {livro.autor} | ID: {livro.ID} | Status: {status}")
            
            listbox.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
        else:  # Livro único
            livro = resultado
            status = "Disponível" if livro.status_emprestimo == "disponível" else "Emprestado"
            messagebox.showinfo("Resultado da Pesquisa", 
                               f"Título: {livro.titulo}\nAutor: {livro.autor}\nID: {livro.ID}\nStatus: {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()