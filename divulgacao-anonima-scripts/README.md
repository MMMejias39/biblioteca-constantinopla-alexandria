# 🕵️ Scripts de Divulgação Anônima — BABEL

**Objetivo:** Espalhar BABEL de forma anônima e rastreável via scripts Python.

**Filosofia:** Você desaparece. BABEL permanece.

---

## ⚠️ AVISO IMPORTANTE

Estes scripts usam **Selenium** para automação de navegador. Execute SEMPRE com:

1. **VPN ativa** (Mullvad grátis: https://mullvad.net)
2. **Navegador privado/incógnito** (ou criar perfil novo)
3. **Contas descartáveis** (não use dados pessoais)
4. **Delete contas depois** (nenhum rastro)

---

## 📋 Scripts Disponíveis

### 1️⃣ `protonmail-enviar.py`
Envia emails anônimos via ProtonMail descartável.

**O que faz:**
- Login em ProtonMail (sua conta descartável)
- Envia emails pré-configurados para lista de contatos
- Personaliza destinatários

**Tempo:** ~5-10 minutos

**Como usar:**
```bash
# 1. Crie conta em https://protonmail.com (descartável)
# 2. Edite o script:
nano protonmail-enviar.py

# Configure:
EMAIL_PROTONMAIL = "seu-email@protonmail.com"
SENHA_PROTONMAIL = "sua-senha"
DESTINATARIOS = ["email1@exemplo.com", "email2@exemplo.com", ...]

# 3. Rode:
python3 protonmail-enviar.py

# 4. Execute com VPN ativa
# 5. Delete conta ProtonMail depois
```

---

### 2️⃣ `reddit-postar.py`
Posta em subreddits anônimamente.

**O que faz:**
- Login em Reddit (sua conta anônima)
- Posta em múltiplos subreddits
- Customiza lista de subreddits

**Tempo:** ~5-10 minutos

**Como usar:**
```bash
# 1. Crie conta em https://reddit.com (anônima)
#    Email: https://10minutemail.com (temporário)
# 2. Edite o script:
nano reddit-postar.py

# Configure:
USERNAME_REDDIT = "seu-username"
SENHA_REDDIT = "sua-senha"
EMAIL_REDDIT = "seu-email-temporario@10minutemail.com"
SUBREDDITS = ["opensource", "activism", ...]

# 3. Rode:
python3 reddit-postar.py

# 4. Execute com VPN ativa
# 5. Delete conta Reddit depois
```

---

### 3️⃣ `twitter-postar.py`
Posta tweets anônimamente.

**O que faz:**
- Login no Twitter/X (sua conta anônima)
- Posta múltiplos tweets
- Customiza tweets

**Tempo:** ~3-5 minutos

**Como usar:**
```bash
# 1. Crie conta em https://twitter.com (anônima)
#    Email: https://10minutemail.com (temporário)
# 2. Edite o script:
nano twitter-postar.py

# Configure:
USERNAME_TWITTER = "seu-username"
EMAIL_TWITTER = "seu-email-temporario@10minutemail.com"
SENHA_TWITTER = "sua-senha"

# 3. Rode:
python3 twitter-postar.py

# 4. Execute com VPN ativa
# 5. Delete conta Twitter depois
```

---

## 🛠️ Dependências

Instale antes de rodar:

```bash
# Chrome/Chromium (necessário para Selenium)
# Ubuntu/Debian:
sudo apt-get install chromium-browser

# macOS:
brew install chromium

# Depois: Python dependencies
pip3 install selenium

# Você também precisa do chromedriver
# Download: https://chromedriver.chromium.org/
# Ou instale via pip:
pip3 install webdriver-manager
```

---

## 📝 Passo-a-Passo Completo (30 min)

### 1. Prepare o Ambiente

```bash
# VPN (Mullvad)
# https://mullvad.net/download → Instale e conecte

# Terminal:
cd /home/mejias/biblioteca-constantinopla-alexandria/divulgacao-anonima-scripts

# Instale dependências:
pip3 install selenium webdriver-manager
```

### 2. Escolha 1-2 Scripts

**Opção A: ProtonMail (Educadores + ONGs)**
```bash
# Edite emails para enviar
nano protonmail-enviar.py

# Configure:
# - EMAIL_PROTONMAIL
# - SENHA_PROTONMAIL
# - DESTINATARIOS
```

**Opção B: Reddit (Comunidade Tech + Activism)**
```bash
# Edite conta e subreddits
nano reddit-postar.py

# Configure:
# - USERNAME_REDDIT
# - SENHA_REDDIT
# - EMAIL_REDDIT
# - SUBREDDITS
```

**Opção C: Twitter (Visibilidade Rápida)**
```bash
# Edite tweets
nano twitter-postar.py

# Configure:
# - USERNAME_TWITTER
# - EMAIL_TWITTER
# - SENHA_TWITTER
```

### 3. Execute

```bash
# Com VPN ativa, navegador PRIVADO aberto:
python3 protonmail-enviar.py
# ou
python3 reddit-postar.py
# ou
python3 twitter-postar.py
```

### 4. Cleanup (Importante!)

```bash
# 1. Feche navegador
# 2. Delete contas (Settings em cada plataforma)
# 3. Limpe histórico do navegador
# 4. Desconecte VPN
# 5. Desligue PC
# 6. Continue vida normal
```

---

## 🔐 Segurança — Não Deixe Rastros

### DURANTE execução:

- ✅ VPN **ativa**
- ✅ Navegador em **modo incógnito** ou novo perfil
- ✅ Contas **descartáveis** (não seus dados)
- ✅ Emails **temporários** (10minutemail.com)
- ✅ Senhas **aleatórias** (não salve)

### DEPOIS:

- ✅ Delete contas em cada plataforma
- ✅ Limpe histórico do navegador (Ctrl+Shift+Delete)
- ✅ Desconecte VPN
- ✅ Reinicie computador
- ✅ Nenhum rastro de você

**Resultado:** IP anônimo (VPN) + contas descartáveis + nenhum rastro pessoal = **Você desaparece completamente** ✨

---

## 📊 Resultado Esperado

**Após executar todos os scripts:**

| Métrica | Semana 1 | Mês 1 |
|---------|----------|-------|
| Pessoas que sabem | 100+ | 1000+ |
| GitHub stars | 20+ | 100+ |
| Menções em redes | 10+ | 100+ |
| Você rastreado? | ❌ Não | ❌ Não |

---

## 🐛 Troubleshooting

### "Chrome não encontrado"
```bash
pip3 install webdriver-manager
# Script vai baixar automaticamente
```

### "CAPTCHA apareceu"
- Pause o script (Ctrl+C)
- Resolva manualmente no navegador
- Retome execução

### "Conta bloqueada"
- Delete a conta
- Crie nova conta (diferente email temporário)
- Tente novamente com VPN diferente

### "Login falhou"
- Verifique email/senha (copy/paste, sem espaços)
- Verifique se conta existe
- Twitter/Reddit podem pedir autenticação 2FA (resolva manualmente)

---

## 📝 Customizações

### Mudar destinatários de email:
```python
DESTINATARIOS = [
    "seu-contato-1@exemplo.com",
    "seu-contato-2@exemplo.com",
    # Adicione quantos quiser
]
```

### Mudar subreddits:
```python
SUBREDDITS = [
    "opensource",
    "activism",
    "privacy",
    # Adicione outros subreddits
]
```

### Mudar tweets:
```python
TWEETS = [
    "Seu tweet 1 aqui",
    "Seu tweet 2 aqui",
    # Adicione quantos quiser (cada um é um tweet separado)
]
```

---

## ⚡ Quick Start (5 minutos)

```bash
# 1. VPN: Instale Mullvad, conecte
# 2. Terminal:
cd divulgacao-anonima-scripts
pip3 install selenium webdriver-manager

# 3. Escolha UM script, edite emails/username
nano protonmail-enviar.py

# 4. Execute:
python3 protonmail-enviar.py

# 5. Siga instruções
# 6. Delete contas depois
# 7. Fim!
```

---

## 🎯 Filosofia

```
Você executa scripts
  ↓
BABEL se espalha
  ↓
Comunidade descobre
  ↓
Você desaparece
  ↓
BABEL permanece para sempre
```

---

**Versão:** 1.0  
**Data:** 2026-10-09  
**Status:** Pronto para Execução

**Lembrete:** Você é apenas o catalisador. Depois desaparece.  
BABEL é de humanidade, não de você.

🚀 Comece agora. Depois volte para vida normal.
