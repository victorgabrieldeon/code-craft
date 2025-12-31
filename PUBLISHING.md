# 🚀 Publishing code-craft to PyPI

## ✅ Build Status

**Package built successfully!**

- Distribution: `code_craft-0.1.0.tar.gz`
- Wheel: `code_craft-0.1.0-py3-none-any.whl`

## 🔐 PyPI Authentication Required

PyPI no longer accepts username/password authentication. You need an **API Token**.

### Step 1: Create PyPI API Token

1. Go to: https://pypi.org/manage/account/token/
2. Click **"Add API token"**
3. Name: `code-craft-upload`
4. Scope: **Entire account** (or specific to `code-craft` after first upload)
5. Copy the token (starts with `pypi-...`)

### Step 2: Configure PDM

```bash
# Set username as __token__
pdm config pypi.username __token__

# Set your API token as password
pdm config pypi.password pypi-YOUR_TOKEN_HERE
```

### Step 3: Publish

```bash
# Option 1: Publish to PyPI (production)
pdm publish

# Option 2: Test on TestPyPI first (recommended)
pdm publish -r testpypi
```

## 📝 Alternative: Use Environment Variables

Instead of storing in config:

```bash
export PDM_PUBLISH_USERNAME=__token__
export PDM_PUBLISH_PASSWORD=pypi-YOUR_TOKEN_HERE
pdm publish
```

## 🔍 Verify Publication

After publishing:

```bash
pip install code-craft
```

Or on TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ code-craft
```

## ✨ Package URL

Once published, your package will be available at:
https://pypi.org/project/code-craft/

## 📦 Installation Command for Users

```bash
pip install code-craft
```

Or with code import:

```python
from codecraft import CodeBuilder
```
