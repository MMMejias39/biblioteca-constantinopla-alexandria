#!/usr/bin/env python3
"""
Script: Postar em subreddits anônimamente
Uso: python3 reddit-postar.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

# ⚠️ CONFIGURAÇÃO — CUSTOMIZE ANTES DE RODAR

USERNAME_REDDIT = "seu-username-anonimo"  # Ex: babel_library_2026
SENHA_REDDIT = "sua-senha-aqui"
EMAIL_REDDIT = "email-temporario@10minutemail.com"  # Use 10minutemail.com

SUBREDDITS = [
    "opensource",
    "DecentralizedInternet",
    "openkowledge",
    "activism",
    "privacy",
]

TITULO = "BABEL — Biblioteca Digital Descentralizada Permanente"

CORPO = """Alguém aqui conhece BABEL? Descobri no GitHub e achei bem interessante.

É uma biblioteca digital criada por criadores anônimos que:
  ✓ Preserva conhecimento para sempre (descentralizado, P2P)
  ✓ Zero custo
  ✓ Funciona offline
  ✓ Impossível de censurar (múltiplas jurisdições, IPFS)
  ✓ Em 25+ idiomas
  ✓ CC0 (público domínio, sem proprietário)

**GitHub:** https://github.com/MMMejias39/biblioteca-constantinopla-alexandria

Achei bem legal o conceito de conhecimento como bem público permanente. Alguém mais conhece ou já usa?

#OpenKnowledge #Descentralizado #LiberdadeDeInformação"""

# ================================

def postar_reddit():
    print("🔴 REDDIT AUTOMÁTICO — Poster Anônimo")
    print("=" * 60)

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Descomente para modo silencioso
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Passo 1: Login Reddit
        print("\n🔑 Acessando Reddit...")
        driver.get("https://www.reddit.com/login")
        time.sleep(3)

        print("🔓 Fazendo login...")

        # Username
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_input.send_keys(USERNAME_REDDIT)
        time.sleep(1)

        # Senha
        senha_input = driver.find_element(By.NAME, "password")
        senha_input.send_keys(SENHA_REDDIT)
        time.sleep(1)

        # Login
        login_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
        login_btn.click()
        time.sleep(5)

        # Passo 2: Postar em subreddits
        print(f"\n📝 Postando em {len(SUBREDDITS)} subreddits...\n")

        for i, subreddit in enumerate(SUBREDDITS, 1):
            print(f"  {i}. r/{subreddit}...", end="", flush=True)

            # Ir para subreddit
            driver.get(f"https://www.reddit.com/r/{subreddit}/submit")
            time.sleep(3)

            # Título
            try:
                titulo_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Title']"))
                )
                titulo_input.send_keys(TITULO)
                time.sleep(1)
            except:
                print("\n  ⚠️  Problema ao encontrar campo de título")
                continue

            # Corpo
            try:
                corpo_input = driver.find_element(By.XPATH, "//textarea[@placeholder='Text']")
                corpo_input.send_keys(CORPO)
                time.sleep(1)
            except:
                pass  # Alguns subreddits não têm campo de corpo

            # Postar
            try:
                postar_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]")
                postar_btn.click()
                time.sleep(3)
                print(" ✅")
            except:
                print(" ⚠️  (não conseguiu postar)")

        print("\n" + "=" * 60)
        print("✨ Posts enviados!")
        print("\n⚠️  PRÓXIMO PASSO:")
        print("  1. NÃO responda nos posts como criador")
        print("  2. Deixe comunidade gerenciar")
        print("  3. Feche navegador")
        print("  4. DELETE conta Reddit (Settings → Delete Account)")
        print("  5. Limpe histórico\n")

    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("\nDica: Reddit pode pedir CAPTCHA. Se acontecer,")
        print("você pode fazer isto manualmente em reddit.com\n")

    finally:
        input("\n[Pressione ENTER para fechar navegador...]")
        driver.quit()

if __name__ == "__main__":
    if USERNAME_REDDIT == "seu-username-anonimo":
        print("❌ ERRO: Configure USERNAME_REDDIT e SENHA_REDDIT!")
        print("\nPASSOS:")
        print("  1. Crie conta em https://www.reddit.com (anônima)")
        print("  2. Use email temporário: https://10minutemail.com")
        print("  3. Copie username e senha neste script")
        print("  4. Rode: python3 reddit-postar.py")
        sys.exit(1)

    print("⚠️  AVISO IMPORTANTE:")
    print("  • EXECUTE COM VPN (Mullvad grátis)")
    print("  • USE EMAIL TEMPORÁRIO (10minutemail.com)")
    print("  • DELETE CONTA DEPOIS")
    print("  • NÃO USE SEUS DADOS PESSOAIS\n")

    input("Pressione ENTER para continuar...")
    postar_reddit()
