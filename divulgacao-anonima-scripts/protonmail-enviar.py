#!/usr/bin/env python3
"""
Script: Enviar emails anônimos via ProtonMail
Uso: python3 protonmail-enviar.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

# ⚠️ CONFIGURAÇÃO — CUSTOMIZE ANTES DE RODAR

EMAIL_PROTONMAIL = "seu-email-protonmail@protonmail.com"  # Crie em https://protonmail.com
SENHA_PROTONMAIL = "sua-senha-aqui"  # Senha da conta (delete depois)

DESTINATARIOS = [
    "educador1@escola.br",
    "ong@greenpeace.org.br",
    "contato@comunidade-indigena.org",
    # Adicione mais emails aqui
]

ASSUNTO = "BABEL — Conhecimento Descentralizado para Humanidade"

CORPO = """Criadores anônimos em múltiplos países desenvolveram BABEL.

Uma biblioteca digital que:
  ✓ Preserva conhecimento indefinidamente (zero custo)
  ✓ Não pode ser censurada (descentralizado, P2P, offline)
  ✓ Sem proprietário (CC0, público domínio)
  ✓ Em qualquer idioma (25+)
  ✓ Funciona offline (sem internet necessária)

GitHub: https://github.com/MMMejias39/biblioteca-constantinopla-alexandria

Sem necessidade de responder. Conhecimento é direito, não propriedade.

— Compartilhadores Anônimos"""

# ================================

def enviar_emails():
    print("🌐 PROTONMAIL AUTOMÁTICO — Enviador Anônimo")
    print("=" * 60)

    # Configurar Chrome (modo headless = sem interface)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Comentado: descomente para modo silencioso
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Passo 1: Abrir ProtonMail
        print("\n📧 Abrindo ProtonMail...")
        driver.get("https://mail.protonmail.com/login")
        time.sleep(3)

        # Passo 2: Login
        print("🔑 Fazendo login...")

        # Email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        email_input.send_keys(EMAIL_PROTONMAIL)
        time.sleep(1)

        # Senha
        senha_input = driver.find_element(By.NAME, "password")
        senha_input.send_keys(SENHA_PROTONMAIL)
        time.sleep(1)

        # Botão login
        login_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
        login_btn.click()
        time.sleep(5)  # Aguardar carregar

        # Passo 3: Enviar emails
        print(f"\n📮 Enviando {len(DESTINATARIOS)} emails...\n")

        for i, destinatario in enumerate(DESTINATARIOS, 1):
            print(f"  {i}. Enviando para {destinatario}...", end="", flush=True)

            # Novo email
            novo_email_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Compose')]"))
            )
            novo_email_btn.click()
            time.sleep(2)

            # Campo "Para"
            para_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='To']"))
            )
            para_input.send_keys(destinatario)
            time.sleep(1)

            # Campo "Assunto"
            assunto_input = driver.find_element(By.XPATH, "//input[@placeholder='Subject']")
            assunto_input.send_keys(ASSUNTO)
            time.sleep(1)

            # Campo "Corpo"
            corpo_input = driver.find_element(By.XPATH, "//textarea[@placeholder='Message']")
            corpo_input.send_keys(CORPO)
            time.sleep(1)

            # Enviar
            enviar_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
            enviar_btn.click()
            time.sleep(3)

            print(" ✅")

        print("\n" + "=" * 60)
        print("✨ Todos os emails foram enviados!")
        print("\n⚠️  PRÓXIMO PASSO:")
        print("  1. Feche este navegador")
        print("  2. Limpe histórico do navegador")
        print("  3. Vá em https://protonmail.com → Settings → Delete Account")
        print("  4. Delete a conta ProtonMail")
        print("  5. Continue com vida normal\n")

    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("\nDica: Se tiver problema com login, ProtonMail pode pedir")
        print("autenticação manual. Você também pode fazer isto manualmente")
        print("seguindo as instruções em DIVULGACAO-EXECUTAVEL.md\n")

    finally:
        input("\n[Pressione ENTER para fechar navegador...]")
        driver.quit()

if __name__ == "__main__":
    # Verificações
    if EMAIL_PROTONMAIL == "seu-email-protonmail@protonmail.com":
        print("❌ ERRO: Configure EMAIL_PROTONMAIL e SENHA_PROTONMAIL no script!")
        print("\nPASSOS:")
        print("  1. Crie conta em https://protonmail.com (descartável)")
        print("  2. Copie email e senha neste script")
        print("  3. Rode: python3 protonmail-enviar.py")
        sys.exit(1)

    if not DESTINATARIOS:
        print("❌ ERRO: Liste DESTINATARIOS no script!")
        sys.exit(1)

    print("⚠️  AVISO IMPORTANTE:")
    print("  • EXECUTE COM VPN (Mullvad grátis)")
    print("  • NAVEGADOR PRIVADO/INCÓGNITO")
    print("  • DELETE CONTA DEPOIS")
    print("  • NÃO USE SEUS DADOS PESSOAIS\n")

    input("Pressione ENTER para continuar...")
    enviar_emails()
