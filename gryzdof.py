import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

messages = [
    "# *Hudba je jazyk, který nepotřebuje překlad. A když najdeš tu správnou melodii, dokáže tě vytáhnout z nejhlubší tmy a připomenout ti, že má smysl pokračovat.*",
    "# *Každý tón, který hraješ nebo posloucháš, je krokem na cestě. Není důležité, jestli ladíš dokonale – důležité je, že se učíš a rosteš.*",
    "# *Hudba není útěk od reality, ale klíč, jak ji přežít a proměnit bolest v něco krásného.*",
    "# *Když máš pocit, že svět tě neposlouchá, zahraj svou píseň. Ať slyší aspoň tvé srdce, že stále bije do rytmu.*",
    "# *Hudba je jako dech – nemůžeš ji zastavit. Pokud ji v sobě cítíš, nech ji proudit, protože právě ona tě může dovést tam, kam se bojíš jít sám.*",
    "# *Každý beat je připomínkou, že čas běží. Můžeš ho promarnit tichem, nebo využít k vytvoření vlastního příběhu.*",
    "# *Hudba tě naučí, že i disonance má smysl – stejně jako těžké dny v životě, které nakonec vytvoří harmonii s těmi dobrými.*",
    "# *Největší síla hudby není v tom, že zaplní sál, ale v tom, že dokáže naplnit prázdnotu uvnitř tebe.*",
    "# *Hudebníci vědí, že chyba není konec – je to nový směr. Stejně tak se dívej na svůj život: špatný krok může být začátkem nové cesty.*",
    "# *Hudba ti ukáže, že není nutné rozumět všemu, aby tě to dokázalo změnit.*",
    "# *Každá píseň je důkazem, že i ticho se dá překonat. A ty máš sílu překonat své vlastní ticho, když se rozhodneš ozvat.*",
    "# *Hudba není o tom, kolik lidí tě poslouchá, ale jak moc se ty sám slyšíš, když hraješ nebo zpíváš.*",
    "# *Pokud tě hudba dokáže rozplakat nebo rozesmát, znamená to, že žiješ. To samo o sobě je důvod jít dál.*",
    "# *Hudba je jako most přes chaos. I když se ti svět rozpadá pod nohama, melodie ti ukáže, že můžeš přejít dál.*",
    "# *Když máš pocit, že jsi na dně, poslouchej rytmus. I srdce hraje pořád stejný beat – a to je signál, že ještě není konec.*",
    "# *Hudba je připomínkou, že dokonalost není cílem. Krása vzniká právě z nedokonalých tónů, stejně jako ty rosteš ze svých nedostatků.*",
    "# *Každá skladba je jako život – začíná tichem, prochází bouřemi i klidem, a nakonec mizí. Ale záleží, jaký pocit zanechá.*",
    "# *Hudba ti ukáže, že i v nejhlubším smutku existuje krása. Někdy musíš slyšet temné tóny, abys vážil ty jasné.*",
    "# *Hudba ti nemusí dát odpovědi. Ale vždycky ti dá otázky, které tě přinutí hledat svou vlastní cestu.*",
    "# *Když hraješ hudbu, hraješ i sám sebe. A každý nový den je šance zahrát lepší verzi.*",
    "# *Hudba je připomínka, že nikdy nejsi sám – vždy existuje rytmus, který bije spolu s tebou.*",
    "# *Hudba nezná hranice. Pokud tě něco drží zpátky, nauč se slyšet melodii, která tě vede vpřed.*",
    "# *Každá píseň začíná prázdným papírem. A tvůj život je stejný – na to, abys napsal nový verš, nepotřebuješ nic jiného než odvahu.*",
    "# *Hudba tě učí trpělivosti – velká symfonie nevznikne přes noc. Ani tvůj příběh ne.*",
    "# *Hudba tě dokáže naučit, že i v nejtěžších chvílích můžeš najít rytmus, který tě udrží na nohou.*"
]

last_message = None

@bot.event
async def on_ready():
    print(f"Přihlášen jako {bot.user}")
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_daily_message, "cron", hour=6, minute=0)
    scheduler.start()
    print("Scheduler spuštěn - denní zprávy budou odesílány v 6:00")
    
async def send_daily_message():
    global last_message
    channel = bot.get_channel(1419121174935244933)
    
    if channel is None:
        print("Kanál nebyl nalezen!")
        return
    
    available = [msg for msg in messages if msg != last_message]
    chosen = random.choice(available)
    
    try:
        await channel.send(chosen)
        print(f"Zpráva odeslána: {chosen[:50]}...")
        last_message = chosen
    except Exception as e:
        print(f"Chyba při odesílání zprávy: {e}")
@bot.command(name='test')
async def test_message(ctx, action=None):
    """Odešle testovací motivační zprávu - použijte !test motivator"""
    if action != "motivator":
        await ctx.send("❌ Použijte: `!test motivator` pro odeslání testovací zprávy")
        return
    
    global last_message
    channel = bot.get_channel(1419121174935244933)
    
    if channel is None:
        await ctx.send("Kanál nebyl nalezen!")
        return
    
    available = [msg for msg in messages if msg != last_message]
    chosen = random.choice(available)
    
    try:
        await channel.send(f"🎵 **Testovací zpráva:** {chosen}")
        last_message = chosen
    except Exception as e:
        await ctx.send(f"❌ Chyba při odesílání zprávy: {e}")
        print(f"Chyba při odesílání testovací zprávy: {e}")
if __name__ == "__main__":
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print("CHYBA: DISCORD_BOT_TOKEN nebyl nalezen v proměnných prostředí!")
        print("Přidejte svůj Discord bot token jako proměnnou prostředí 'DISCORD_BOT_TOKEN'")
        exit(1)
    
    bot.run(token)
