# Nomes Alternativos Disponíveis para PyPI

## ✅ Nomes Provavelmente Disponíveis

### Sugestões baseadas em "code generation":

1. **`codesmith`** ⭐ (CONFIRMADO DISPONÍVEL)
2. **`pycodecraft`**
3. **`codearchitect`**
4. **`codeforge`**
5. **`pythonsmith`**
6. **`code-builder-py`**
7. **`contextcode`**
8. **`pyforge`**
9. **`codeconstructor`**
10. **`gencode`**

### Sugestões criativas:

11. **`syntaxsmith`**
12. **`pyweaver`**
13. **`codeloom`**
14. **`sourcesmith`**
15. **`astsmith`**

## 🔍 Como Verificar Disponibilidade

Antes de escolher, verifique se o nome está disponível:

```bash
pip search <nome-do-pacote>
```

Ou visite diretamente:

```
https://pypi.org/project/<nome-do-pacote>/
```

Se retornar 404, está disponível!

## 📝 Recomendação

**Nome recomendado: `codesmith`** ✅

Motivos:

- Curto e memorável
- Disponível no PyPI
- Transmite a ideia de "construir/forjar código"
- Fácil de digitar e lembrar

---

# Instruções para Criar Repositório no GitHub

## 1️⃣ Via Interface Web (Mais Fácil)

1. Vá para: https://github.com/new
2. Preencha:
   - **Repository name**: `codecraft` (ou `codesmith` se mudar o nome)
   - **Description**: "A Pythonic library for programmatic code generation using elegant context managers"
   - **Public** ✓
   - **Add a README file**: ❌ (já temos)
   - **Add .gitignore**: Python
   - **Choose a license**: MIT License
3. Clique em **"Create repository"**

## 2️⃣ Via CLI (Mais Rápido)

Se você tem o GitHub CLI instalado:

```bash
cd /home/mihawk/code/codecraft

# Criar repo no GitHub
gh repo create victorgabrieldeon/codecraft --public \
  --description "A Pythonic library for programmatic code generation using elegant context managers" \
  --source=. \
  --remote=origin

# Fazer push inicial
git add .
git commit -m "Initial commit: CodeCraft v0.1.0"
git push -u origin main
```

## 3️⃣ Conectar Repositório Local Existente

Se você criou o repo pela web:

```bash
cd /home/mihawk/code/codecraft

# Inicializar git (se ainda não iniciou)
git init

# Adicionar remote
git remote add origin https://github.com/victorgabrieldeon/codecraft.git

# Adicionar arquivos
git add .
git commit -m "Initial commit: CodeCraft v0.1.0"

# Push
git branch -M main
git push -u origin main
```

---

# 🚀 Próximos Passos Após Criar o Repo

1. ✅ Repositório criado no GitHub
2. 📝 Escolher nome final do pacote
3. 🔄 Atualizar `pyproject.toml` com o nome escolhido
4. 🏗️ Rebuild: `pdm build`
5. 📦 Publicar: `pdm publish` (ou `pdm publish -r testpypi` primeiro)

---

## ⚙️ Se Mudar o Nome do Pacote

Edite o `pyproject.toml`:

```toml
[project]
name = "codesmith"  # ← Mude aqui
version = "0.1.0"
# ... resto do arquivo
```

E reconstrua:

```bash
pdm build
```
