from typing import Final
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler

Token: Final = "7917487474:AAFMUWgbyDuL2USRRWO5remNJaWEmOB0Jf4"
Bot_username: Final = "@instrumentalhop_bot"

input_await = {}
user_input = ""
async def start_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = (
        "Привет! Я твой ассистент. Вот, что я могу делать:\n\n"
        "1️⃣ Скачать видео.\n"
        "2️⃣ Скачать аудио.\n"
        "3️⃣(Добавьте другие функции)\n\n"
        "Используйте команды или просто напишите мне!"
    )
    keyboard = [
        ["Скачать видео", "Скачать аудио"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(message_text, reply_markup=reply_markup)

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global input_await
    user_id = update.effective_user.id
    input_await[user_id] = "video"

    await update.message.reply_text("Введите ссылку на видео, которое нужно скачать:")


async def handle_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global input_await
    user_id = update.effective_user.id

    if user_id in input_await and input_await[user_id] == "video":
        user_input = update.message.text 
        del input_await[user_id] 
        await update.message.reply_text(f"Ссылка на видео получена: {user_input}")
    else:
        await update.message.reply_text("Пожалуйста, выберите команду через /start.")

async def audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите ссылку на аудио, которое нужно скачать:")


def main():
    application = Application.builder().token(Token).build()

    application.add_handler(CommandHandler("start", start_massage))
    application.add_handler(MessageHandler(filters.Regex("Скачать видео"), video))
    application.add_handler(MessageHandler(filters.Regex("Скачать аудио"), audio))
    application.add_handler(MessageHandler(filters.TEXT, handle_input)) 

    application.run_polling()

if __name__ == "__main__":
    main()
