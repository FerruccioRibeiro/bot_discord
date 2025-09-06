import hikari
import lightbulb
import random
import requests

bot = hikari.GatewayBot(open('tokens/discord_tk.txt').read())
client = lightbulb.client_from_app(bot)

bot.subscribe(hikari.StartingEvent, client.start)

@client.register()
class hello_bot(lightbulb.SlashCommand, name="hello_bot", description="Inicia o bot"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond("*Ola Ferruccio!*")


# Piadas
p1 = 'O que o pato disse para a pata? \nR: Vem Qua!'
p2 = 'Por que o menino estava falando no telefone deitado? \nR: Para nao cair a ligacao.'
p3 = 'Qual cidade brasileira que nao tem taxi? \nR: Uberlandia.'
p4 = 'Qual a fruta que anda de trem? \nR: O kiwiiiii.'
p5 = 'O que e um pontinho preto no aviao? \nR: Uma aeromosca.'

piadas = [p1,p2,p3,p4,p5]

@client.register()
class piada(lightbulb.SlashCommand, name="piada", description="Receba uma piada"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        n = random.randint(0,4)
        await ctx.respond(f'*{piadas[n]}*')

# Calculadora
group = lightbulb.Group("calculadora", "Inicia a calculadora")
@group.register()
class soma(lightbulb.SlashCommand, name="soma", description="Soma dois valores"):
    n2 = lightbulb.number("n2", "Numero 2")
    n1 = lightbulb.number("n1", "Numero 1")
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        r = self.n1 + self.n2
        await ctx.respond(f'*{r}*')

@group.register()
class subtracao(lightbulb.SlashCommand, name="subtracao", description="Soma dois valores"):
    n2 = lightbulb.number("n2", "Numero 2")
    n1 = lightbulb.number("n1", "Numero 1")
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        r = self.n1 - self.n2
        await ctx.respond(f'*{r}*')

@group.register()
class divisao(lightbulb.SlashCommand, name="divisao", description="Soma dois valores"):
    n2 = lightbulb.number("n2", "Numero 2")
    n1 = lightbulb.number("n1", "Numero 1")
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        r = self.n1 / self.n2
        await ctx.respond(f'*{r}*')

@group.register()
class multiplicacao(lightbulb.SlashCommand, name="multiplicacao", description="Soma dois valores"):
    n2 = lightbulb.number("n2", "Numero 2")
    n1 = lightbulb.number("n1", "Numero 1")
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        r = self.n1 * self.n2
        await ctx.respond(f'*{r}*')

client.register(group)

#Temperatura
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('tokens/api_weather_key.txt').read()

@client.register()
class temperatura(lightbulb.SlashCommand, name="temperatura", description="Saiba das condicoes climaticas de determinada cidade"):
    pais = lightbulb.string("pais", "Digite o pais")
    cidade = lightbulb.string("cidade", "Digite a cidade")

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        pais = str(self.pais)[0:2].lower()
        cidade = str(self.cidade).capitalize()
        local = cidade + ',' + pais
        url = BASE_URL + 'q=' + local + '&appid=' + API_KEY
        api_response = requests.get(url).json()

        temp_kelvin = api_response['main']['temp']
        temp_celsius = round(temp_kelvin - 273.15)
        umid = api_response['main']['humidity']
        vento = api_response['wind']['speed']
        await ctx.respond(f'```A temperatura e de {temp_celsius}C\nUmidade de {umid}%\nCom ventos de {vento}m/s```')

bot.run()
