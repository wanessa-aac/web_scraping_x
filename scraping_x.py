from selenium import webdriver
from selenium.webdriver.safari.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import csv
import time
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurando o Safari para ser controlado pelo Selenium
options = Options()
driver = webdriver.Safari(options=options)

# Abre o X para poder adicionar os cookies de autenticação
driver.get("https://x.com")
time.sleep(3)

# Adiciona os cookies da sessão para autenticar sem precisar de login manual
driver.add_cookie({
    "name": "auth_token",
    "value": os.getenv("AUTH_TOKEN"),
    "domain": ".x.com"
})

driver.add_cookie({
    "name": "ct0",
    "value": os.getenv("CT0"),
    "domain": ".x.com"
})

# Acessa o perfil da Anthropic com a sessão autenticada
print("Carregando sessão com cookies...")
driver.get("https://x.com/AnthropicAI")

# Aguarda a página carregar completamente
time.sleep(8)

# Volta para o topo primeiro
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)

# Rola devagar para carregar os tweets mais recentes
for i in range(3):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

# Usa o BeautifulSoup para extrair os dados do HTML carregado pelo Selenium
soup = BeautifulSoup(driver.page_source, "lxml")

# Lista para armazenar os tweets coletados
tweets_coletados = []

# Localiza todos os elementos de tweet pelo atributo data-testid
tweets = soup.find_all("div", {"data-testid": "tweetText"})

# Percorre cada tweet e extrai autor, descrição e data
for tweet in tweets[:10]:
    # Extrai o nome do autor corretamente
    try:
        bloco = tweet.find_previous("div", {"data-testid": "User-Name"})
        spans = bloco.find_all("span")
        autor = spans[0].get_text(strip=True)
        username = spans[3].get_text(strip=True)
    except:
        autor = "Anthropic"
        username = "@AnthropicAI"

    # Extrai a data do tweet
    try:
        data = tweet.find_previous("time")["datetime"]
    except:
        data = "data não encontrada"

    # Adiciona os dados na lista
    tweets_coletados.append({
        "autor": f"{autor} {username}",
        "descricao": tweet.get_text(strip=True),
        "data": data
    })

# Salva os tweets coletados em um arquivo CSV estruturado
with open("tweets_anthropic.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["autor", "descricao", "data"])
    writer.writeheader()
    writer.writerows(tweets_coletados)

print(f"\n√ {len(tweets_coletados)} tweets salvos em tweets_anthropic.csv!")

driver.quit()