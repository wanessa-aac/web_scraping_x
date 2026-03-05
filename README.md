# Web Scraping do X (Antigo Twitter) com Python
Esse projeto foi desenvolvido para a disciplina de **Modelagem de Dados**, com o objetivo de coletar publicações de algum perfil de usuário do X (antigo Twitter). O perfil que escolhi foi o da @AnthropicAI, utilizei Python, Selenium e BeautifulSoup.

> ⚠️ **Nota:** Este script foi desenvolvido para **macOS** pois utiliza o SafariDriver. Para outros sistemas operacionais, será necessário adaptar o navegador.

---

## 📋 O que o script faz?

- Autentica no **X** via cookies de sessão (sem login automatizado)
- Acessa o perfil público @AnthropicAI
- Extrai os 10 tweets mais recentes com: **autor**, **descrição**, e **data**
- Salva os dados em um arquivo `.csv` estruturado

---

## 🛠️ Bibliotecas utilizadas

  | Biblioteca | Função |
  |---|---|
  | `selenium` | Responsável por controlar o Safari automaticamente |
  | `beautifulsoup4` | Utilizada para extração de dados do HTML renderizado |
  | `lxml` | Parser rápido usado pelo BeautifulSoup4; podemos descrever o `lxml` como um tradutor de {'chave': 'valor'} para objeto no código |
  | `python-dotenv`| Lê as credenciais do arquivo `.env`, permitindo a segurança e o gerenciamento eficiente de dados sensíveis|

  ---

## ⚙️ Como instalar?

**1. Clone o repositório:**
```bash
git clone https://github.com/wanessa-aac/web_scraping_x.git
cd web_scraping_x
```

**2. Crie e ative o ambiente virtual:**
```bash
python3 -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install selenium beautifulsoup4 lxml python-dotenv
```

## 🧭 Configuração do Safari
Antes de rodar o script, é necessário habilitar a automação no Safari:
1. Abra o **Safari**
2. Vá em **Safari → Ajustes → Avançado**
3. Ative **"Mostrar recursos para desenvolvedores da web"**
4. No menu **Desenvolvimento** → clique em **"Permitir Automação Remota"**

---

## 🍪 Como configurar os cookies?

O X bloqueia login automatizado, por isso a autenticação é feita via cookies de sessão exportados manualmente do navegador, por isso é de suma importância habilitar **Mostrar recursos para desenvolvedor da web**.

**Passo a passo para obter os cookies:**

1. Acesse [x.com](https://x.com) e faça login normalmente no **Safari**
2. Abra o Inspecionar Elemento (no macOS Tahoe): ou simplesmente use `Cmd + Option + I`
3. Vá em **Armazenamento → Cookies → x.com**
4. Copie os valores de `auth_token` e `ct0`

**Crie o arquivo `.env` na raiz do projeto:**
```
AUTH_TOKEN=seu_auth_token_aqui
CT0=seu_ct0_aqui
```

> ⚠️ **Atenção:** Os cookies são pessoais e expiram periodicamente. Cada usuário deve usar seus próprios cookies. O arquivo `.env` nunca em hipótese alguma deve ser enviado ao Github.

___

## ▶️ Como faço para rodar o script?

Com o ambiente virtual ativo e o `.env` configurado:
```bash
python3 scraping_x.py
```

O Safari abrirá automaticamente, carregando o perfil escolhido e os dados serão salvos em `tweets_anthropic.csv`.

___

## 📄 Exemplo de saída
```
autor, descricao, data
Anthropic @AnthropicAI,A statement on the comments from Secretary of War Pete Hegseth.,2026-02-28T01:24:31.000Z
Anthropic @AnthropicAI,Introducing Claude Opus 4.6. Our smartest model got an upgrade.,2026-02-05T17:45:16.000Z
```

___

## 🔒 Segurança

Neste projeto, foi usado variáveis de ambiente para proteger credenciais sensíveis. O arquivo `.gitignore`  garante que os seguintes arquivos **nunca sejam enviados ao Github**:
```

.env
venv/
__pycache__/
tweets_anthropic.csv
```

___

## 💡 Observações técnicas

- O X é um site **dinâmico** — o conteúdo é carregado via JavaScript, por isso o Selenium é necessário para renderizar a página antes da extração
- O login automatizado é bloqueado pelo X e pelo Cloudflare, por isso foi adotada a abordagem de cookies
- O `time.sleep()` é necessário para aguardar o carregamento completo da página antes da extração

---

*Projeto acadêmico — Disciplina de Modelagem de Dados*
