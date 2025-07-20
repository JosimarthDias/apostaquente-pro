import asyncio
from telegram import Bot

BOT_TOKEN = "7872406811:AAH5Hu8NRmI5TMGKtIm4AXzDSIPDo0A_HIU"
CHAT_ID = -1001958273610

mensagem = """
🔥 MÚLTIPLA VIP - ENTRADA R$100

1. Flamengo x Grêmio – Over 1.5 gols  
2. Real Madrid x Getafe – Vitória do Real Madrid  
3. PSG x Lille – Over 7.5 escanteios  
4. River Plate x Boca Juniors – Over 3.5 cartões  
5. Milan x Napoli – Ambas marcam SIM

💵 Lucro possível: R$1.320,00  
📊 Odds totais: 14.20  
🏠 Casa recomendada: Betano
"""

async def enviar_mensagem():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=mensagem)
    print("✅ Mensagem enviada com sucesso!")

if __name__ == "__main__":
    asyncio.run(enviar_mensagem())

