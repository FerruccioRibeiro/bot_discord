# 🤖 Discord Bot — Calculadora • Piadas • Clima

Um bot de Discord escrito em **Python** usando **Hikari** + **Lightbulb** com três comandos principais:

* **Calculadora** (`/soma`, `/subtrai`, `/multiplica`, `/divide`)
* **Piada** (`/piada`)
* **Clima** (`/temperatura pais:<nome> cidade:<nome>`)

---

## ✨ Destaques

* Slash commands (nativos do Discord)
* Código simples e organizado em plugins
* Integração com API de clima (OpenWeather)
* Pronto para rodar localmente ou em Docker

---

## 📦 Stack

* Python 3.10+
* [hikari](https://www.hikari-py.dev/) (cliente Discord)
* [hikari-lightbulb](https://hikari-lightbulb.readthedocs.io/) (framework de comandos)
* `aiohttp` (requisições assíncronas para a API de clima)

---

## 📁 Estrutura sugerida

```
bot_discord/
├─ bot.py
├─ .venv                          # DISCORD_TOKEN, OPENWEATHER_API_KEY
└─ tokens/
   ├─ api_weather_key.txt
   ├─ discord_tk.txt
```

---

## 🔑 Pré‑requisitos

1. **Criar o bot no Discord Developer Portal**

   * Anote o **Token** do bot.
   * Gere um link de convite com escopos **`bot`** e **`applications.commands`**.
2. **(Opcional)** Ativar *Privileged Gateway Intents* apenas se você realmente precisar (para estes comandos não é necessário o `MESSAGE CONTENT`).
3. **OpenWeather**

   * Crie uma conta em [https://openweathermap.org/](https://openweathermap.org/)
   * Pegue sua **API Key**.

---

## ⚙️ Ambiente

Crie um arquivo `.venv` na raiz

---

## 📥 Dependências

`requirements.txt` sugerido:

```
aiohappyeyeballs==2.6.1
aiohttp==3.12.15
aiosignal==1.4.0
asttokens==3.0.0
async-timeout==5.0.1
attrs==25.3.0
certifi==2025.8.3
charset-normalizer==3.4.3
colorlog==6.9.0
comm==0.2.3
confspec==0.0.3
debugpy==1.8.16
decorator==5.2.1
executing==2.2.1
frozenlist==1.7.0
hikari==2.3.5
hikari-lightbulb==3.2.0
idna==3.10
ipykernel==6.30.1
ipython==9.5.0
ipython_pygments_lexers==1.1.1
jedi==0.19.2
jupyter_client==8.6.3
jupyter_core==5.8.1
linkd==0.1.0
matplotlib-inline==0.1.7
multidict==6.6.4
nest-asyncio==1.6.0
packaging==25.0
parso==0.8.5
pexpect==4.9.0
platformdirs==4.4.0
prompt_toolkit==3.0.52
propcache==0.3.2
psutil==7.0.0
ptyprocess==0.7.0
pure_eval==0.2.3
Pygments==2.19.2
python-dateutil==2.9.0.post0
pyzmq==27.0.2
requests==2.32.5
six==1.17.0
stack-data==0.6.3
tornado==6.5.2
traitlets==5.14.3
typing_extensions==4.15.0
urllib3==2.5.0
wcwidth==0.2.13
yarl==1.20.1
```

Instale:

```bash
pip install -r requirements.txt
```


