# API Rest em Python com Flask e SQLite

Este projeto é uma API Restful desenvolvida em Python utilizando o framework Flask para a construção do servidor e SQLite para o banco de dados.

## Instalação

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução

Para iniciar o servidor, execute o seguinte comando:
```bash
python app.py
```

A API será iniciada e estará acessível em `http://localhost:3000`.

## Endpoints

### Listar todos os livros

- Método: `GET`
- Rota: `/books`
- Descrição: Retorna uma lista com todos os livros cadastrados.

### Listar um único livro

- Método: `GET`
- Rota: `/books/:id`
- Descrição: Retorna os detalhes de um único livro com base no ID fornecido.

### Salvar um livro

- Método: `POST`
- Rota: `/books`
- Descrição: Salva um novo livro no banco de dados.
- Parâmetros do corpo da requisição:
  - `title` (string): Título do livro.
  - `author` (string): Autor do livro.
  - `description` (string): Descrição do livro.

### Deletar um livro

- Método: `DELETE`
- Rota: `/books/:id`
- Descrição: Deleta um livro do banco de dados com base no ID fornecido.

### Atualizar um livro

- Método: `PUT`
- Rota: `/books/:id`
- Descrição: Atualiza os detalhes de um único livro com base no ID fornecido.
- Parâmetros do corpo da requisição:
  - `title` (string): Título do livro.
  - `author` (string): Autor do livro.
  - `description` (string): Descrição do livro.

## Estrutura de Pastas

```
├── .vscode/
│   └── settings.json
├── .gitignore
├── app.py
├── database.db
├── database.py
├── models.py
├── README.md
├── requirements.txt
└── routes.py
```

**Desenvolvido por [Luis Paiva](https://github.com/luispaiva)**
