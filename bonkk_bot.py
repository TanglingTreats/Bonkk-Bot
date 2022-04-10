import re
import logging
import json
from message_util import (
        form_message_with_options,
        get_message_index,
        get_query_article,
        get_all_articles
        )
from datetime import datetime
from telegram import (
        Update, 
        ReplyKeyboardMarkup, 
        InlineKeyboardMarkup, 
        InlineKeyboardButton
    )
from telegram.ext import (
        Updater,
        CommandHandler,
        ConversationHandler,
        MessageHandler,
        Filters,
        CallbackContext,
        CallbackQueryHandler,
        InlineQueryHandler
    )

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

