from telegram import *
from telegram.ext import *
import requests
import json
from types import SimpleNamespace
import math
import random
import time
from datetime import datetime
import pytz
from dateutil import tz

domain = "https://api.chootc.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Tham giá @chootcvn để mua, bán USDT số lượng lớn.", parse_mode=constants.ParseMode.HTML)

async def messageHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.effective_user.username
    chat_id = update.effective_chat.id
    
    info_user = requests.get(f"{domain}/api/user-info/{username}")

    if not info_user.content or info_user.json()["kyc"] != "success":
        await context.bot.deleteMessage(chat_id=chat_id, message_id=update.message.message_id)   

app = ApplicationBuilder().token(
    "6527191878:AAHU-YonBSxVjG3hA6EomsK0-p5msquiR_k").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, messageHandler))

app.run_polling()
