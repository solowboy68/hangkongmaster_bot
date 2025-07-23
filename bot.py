from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# ইউজার ডেটা সেভ করার জন্য মেমরি (বেসিক ডেমো)
users_data = {}

# Start Command
def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in users_data:
        users_data[user_id] = {"coins": 0}
    
    keyboard = [
        [InlineKeyboardButton("💰 Tap to Earn", callback_data='tap')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        f"Welcome {update.effective_user.first_name}! \nYour Coins: {users_data[user_id]['coins']}",
        reply_markup=reply_markup
    )

# Tap Button Handler
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    query.answer()
    
    if query.data == 'tap':
        users_data[user_id]['coins'] += 1  # প্রতি ট্যাপে ১ কয়েন
        keyboard = [
            [InlineKeyboardButton("💰 Tap to Earn", callback_data='tap')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        query.edit_message_text(
            text=f"💰 Coins: {users_data[user_id]['coins']}",
            reply_markup=reply_markup
        )

def main():
    TOKEN = "8079388438:AAEa4UMDLmW8yrd2WyE7NLvosT_Lv-64YkY"  # এখানে BotFather থেকে পাওয়া টোকেন বসাও
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()