#!/usr/bin/env python3
"""
Script: Postar tweets anônimamente no Twitter/X
Uso: python3 twitter-postar.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

# ⚠️ CONFIGURAÇÃO — CUSTOMIZE ANTES DE RODAR

USERNAME_TWITTER = "seu-username-anonimo"  # Ex: babel_libre_2026
EMAIL_TWITTER = "email-temporario@10minutemail.com"
SENHA_TWITTER = "sua-senha-aqui"

TWEETS = [
    """BABEL é uma biblioteca descentralizada permanente que preserva conhecimento para humanidade.

Zero custo. Sem censura. Em qualquer idioma.

Criadores anônimos. Múltiplos países. Um objetivo: libertar informação.

https://github.com/MMMejias39/biblioteca-constantinopla-alexandria

#OpenKnowledge #Descentralizado""",

    """Conhecimento é direito, não propriedade.

BABEL: biblioteca digital que não pode ser censurada, controlada ou deletada.

Funciona offline. Sem proprietário. Para todos.

https://github.com/MMMejias39/biblioteca-constantinopla-alexandria

#LiberdadeDeInformação""",

    """Se o conhecimento é universal, por que está segregado por paywall?

BABEL muda isso: biblioteca permanente, descentralizada, gratuita.

Já traduzido em 5 idiomas. Em crescimento exponencial.

https://github.com/MMMejias39/biblioteca-constantinopla-alexandria""",
]

# ================================

def postar_twitter():
    print("🐦 TWITTER/X AUTOMÁTICO — Poster Anônimo")
    print("=" * 60)

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Descomente para modo silencioso
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Passo 1: Login Twitter
        print("\n🔑 Acessando Twitter...")
        driver.get("https://twitter.com/login")
        time.sleep(3)

        print("🔓 Fazendo login...")

        # Email ou username
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        email_input.send_keys(EMAIL_TWITTER)

        # Próximo
        next_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
        next_btn.click()
        time.sleep(2)

        # Senha
        senha_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        senha_input.send_keys(SENHA_TWITTER)
        time.sleep(1)

        # Login
        login_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
        login_btn.click()
        time.sleep(5)

        # Passo 2: Postar tweets
        print(f"\n🐦 Postando {len(TWEETS)} tweets...\n")

        for i, tweet in enumerate(TWEETS, 1):
            print(f"  {i}. Postando tweet {i}...", end="", flush=True)

            # Campo de tweet
            tweet_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='What is happening!?']"))
            )
            tweet_input.click()
            tweet_input.send_keys(tweet)
            time.sleep(2)

            # Botão "Post"
            post_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]")
            post_btn.click()
            time.sleep(3)

            print(" ✅")

        print("\n" + "=" * 60)
        print("✨ Tweets postados!")
        print("\n⚠️  PRÓXIMO PASSO:")
        print("  1. NÃO interaja com os tweets")
        print("  2. NÃO responda como criador")
        print("  3. Deixe crescer organicamente")
        print("  4. Feche navegador")
        print("  5. DELETE conta (Settings → Deactivate Account)")
        print("  6. Limpe histórico\n")

    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("\nDica: Twitter pode pedir autenticação de 2 fatores.")
        print("Se acontecer, você pode fazer isto manualmente em twitter.com\n")

    finally:
        input("\n[Pressione ENTER para fechar navegador...]")
        driver.quit()

if __name__ == "__main__":
    if USERNAME_TWITTER == "seu-username-anonimo":
        print("❌ ERRO: Configure USERNAME_TWITTER, EMAIL_TWITTER e SENHA_TWITTER!")
        print("\nPASSOS:")
        print("  1. Crie conta em https://twitter.com (anônima)")
        print("  2. Use email temporário: https://10minutemail.com")
        print("  3. Copie username, email e senha neste script")
        print("  4. Rode: python3 twitter-postar.py")
        sys.exit(1)

    print("⚠️  AVISO IMPORTANTE:")
    print("  • EXECUTE COM VPN (Mullvad grátis)")
    print("  • USE EMAIL TEMPORÁRIO (10minutemail.com)")
    print("  • DELETE CONTA DEPOIS")
    print("  • NÃO USE SEUS DADOS PESSOAIS\n")

    input("Pressione ENTER para continuar...")
    postar_twitter()
