# 🚀 API CRUD Assíncrona com FastAPI e UUIDs

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Ativo-success)

Uma API **CRUD** simples e **assíncrona** desenvolvida com **FastAPI**, utilizando **UUIDs** para identificar cada item de forma única.  
O projeto demonstra como integrar **asyncio** aos endpoints, simulando operações de I/O assíncronas para um comportamento não bloqueante.

---

## 📖 Visão Geral

Esta API permite:

- ➕ Criar novos itens com **UUID** gerado automaticamente  
- 📋 Listar todos os itens ou buscar por ID  
- ✏️ Atualizar um item pelo seu UUID  
- 🗑️ Remover itens  
- ⚡ Todas as operações são **assíncronas** (`async def`)

Ideal para praticar programação assíncrona e entender a estrutura de um CRUD moderno com Python + FastAPI.

---

## ✨ Funcionalidades

- ⚡ **Endpoints Assíncronos**: todos usam `async def` para execução não bloqueante.  
- 🆔 **UUIDs Automáticos**: gerados via `uuid.uuid4()` com `default_factory`.  
- 💤 **Operações Assíncronas Simuladas**: uso de `await asyncio.sleep()` para simular acesso a banco de dados ou APIs externas.  
- 🔄 **CRUD Completo**: criação, leitura, atualização e exclusão de registros.

---

## 📦 Como Usar

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
````

### 2️⃣ Instalar Dependências

```bash
# Usando pip
pip install fastapi uvicorn pydantic

# Ou com Poetry
poetry install
```

### 3️⃣ Executar o Servidor

```bash
uvicorn app:app --reload
```

A API ficará disponível em:
🔗 `http://127.0.0.1:8000`
📄 Documentação interativa: `http://127.0.0.1:8000/docs`

---

## 📌 Endpoints

| Método   | Rota            | Descrição                      | Corpo da Requisição          |
| -------- | --------------- | ------------------------------ | ---------------------------- |
| `GET`    | `/`             | Mensagem de boas-vindas        | Nenhum                       |
| `POST`   | `/items`        | Criar novo item                | `{ "item": "nome do item" }` |
| `GET`    | `/items`        | Listar todos os itens          | Nenhum                       |
| `GET`    | `/items/{uuid}` | Obter item específico por UUID | Nenhum                       |
| `PUT`    | `/items/{uuid}` | Atualizar item pelo UUID       | `{ "item": "novo nome" }`    |
| `DELETE` | `/items/{uuid}` | Deletar item pelo UUID         | Nenhum                       |

---

## 📋 Exemplos de Requisições

**Criar um novo item**

```http
POST /items
Content-Type: application/json

{
  "item": "banana"
}
```

**Listar todos os itens**

```http
GET /items
```

**Obter um item específico**

```http
GET /items/<uuid>
```

**Atualizar um item**

```http
PUT /items/<uuid>
Content-Type: application/json

{
  "item": "maçã"
}
```

**Excluir um item**

```http
DELETE /items/<uuid>
```

---

## 🛠 Tecnologias Utilizadas

* 🐍 **Python 3.8+**
* ⚡ **FastAPI**
* ✅ **Pydantic**
* 🔄 **asyncio**

---

## 🤝 Contribuindo

Contribuições são muito bem-vindas!

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas alterações (`git commit -m 'feat: nova feature'`)
4. Envie para o repositório (`git push origin feature/nova-feature`)
5. Abra um Pull Request 🚀

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito por Thiago Alves Soares