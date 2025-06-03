# Sistema de Biblioteca com Interface Tkinter

Este projeto simula o gerenciamento de uma biblioteca com funcionalidades como cadastro de livros e membros, empréstimos, devoluções e busca de livros. Foi desenvolvido em Python utilizando Programação Orientada a Objetos (POO) e interface gráfica com `tkinter`.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: biblioteca nativa para GUI em Python
- **POO (Programação Orientada a Objetos)**: uso de classes para modelar livros, membros e biblioteca
- **Entrada híbrida**: interface gráfica com entradas via terminal (`input()`)

---

## 📋 Funcionalidades

- ✅ Cadastro de livros e membros
- ✅ Empréstimo e devolução de livros
- ✅ Pesquisa por título, autor ou ID
- ✅ Interface gráfica inicial com botões de ação
- ✅ Controle de disponibilidade dos livros
- ✅ Histórico de empréstimos por membro

---

## 🧠 Estrutura do Projeto

### Classes

- `Livro`: representa um livro, com título, autor, ID e status de empréstimo
- `Membro`: representa um usuário da biblioteca com um histórico de empréstimos
- `Biblioteca`: gerencia o catálogo e os membros, e executa operações principais
- `BibliotecaApp`: interface gráfica inicial com botões para chamar as funções principais (inputs ocorrem via terminal)

### Métodos principais

- `adicionar_livro`, `adicionar_membro`
- `emprestar_livro`, `devolver_livro`
- `pesquisar_livro_por_titulo`, `autor`, `ID`

---

## 💡 Exemplo de Fluxo

1. Clique em **Adicionar Livro**
2. Digite os dados no terminal
3. Clique em **Emprestar Livro**
4. Informe o número do membro e título do livro
5. Clique em **Pesquisar Livro** e escolha o critério

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-biblioteca.git
   cd sistema-biblioteca
