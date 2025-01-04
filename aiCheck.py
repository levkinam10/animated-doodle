import asyncio
import nest_asyncio
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import openai

nest_asyncio.apply()  # Применяем nest_asyncio
openai.base_url = "https://models.inference.ai.azure.com"
openai.api_key = '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'

async def start(update, context):
    await update.message.reply_text('Привет! Задайте мне вопрос.')

async def handle_message(update, context):
    user_message = update.message.text
    response = get_gpt_response(user_message)
    print(response)
    await update.message.reply_text(response, parse_mode=ParseMode.HTML)

def get_gpt_response(message):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system", "content": "Ты помощник кодера, ты должен писать код по запросу пользователя, блоки кода выделяй через <code></code>, перед < или > кроме начала и конца блока кода используй символ обхода"},{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

async def main():
    application = ApplicationBuilder().token('6905882326:AAGgTMNQimaQf_vkpVEr-rczUPw9uQsGh_A').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())  # Теперь используем asyncio.run()