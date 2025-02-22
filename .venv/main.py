from telebot import TeleBot
from telebot import types
from telebot.types import InputMediaPhoto
import random
import keyboardInline
#import keyboardMini
import keyboards
from datetime import datetime
import json
from myToken import token, my_admin


bot = TeleBot(token)
today = str(datetime.now().strftime("%Y %B %d %a %H:%M"))

text_redial: str = "Please try again."

text_choice: str = "Choose again"

@bot.message_handler(commands=["start"])
def start_bot(message):
    print("bot")
    #picture_ava = open('picture/ava.png', 'rb')
    #bot.send_photo(message.chat.id, picture_ava)
    #bot.send_message(message.chat.id,str("Hello\U0001F600 " + message.from_user.first_name))

    if message.from_user.first_name is not None:
        returned_info = str(str(message.from_user.id) + ' - ' + message.from_user.first_name)
        bot.send_message(my_admin, returned_info)
    else:
        bot.send_message(my_admin, str(message.from_user.id))


    number_send = random.randint(0, 2)

    set_phrases = ("Nice to meet you \\.", "Pleased to meet you \\.", "How are you \\?")
    picture_ava = open('picture/poetsCove.jpg', 'rb')
    bot.send_photo(message.chat.id, picture_ava)
    bot.send_message(message.chat.id,
                     " Hello, *{0}*\\. {1} Want to visit one of the South Bay Islands? Poets Cove Resort, Spa \\& Marina "
                     " looks forward to welcoming you".format(message.from_user.first_name, set_phrases[number_send]),
                     reply_markup=keyboards.keyboard_start(),
                     parse_mode="MarkdownV2")


@bot.message_handler(content_types=['text'])
def catalog_bot(message):
    picture_address = open('picture/address.png', 'rb')
    if message.text == "About us \U0001F5C2":
        bot.send_message(message.chat.id, "Select a section", reply_markup=keyboards.keyboard_catalog())
        bot.register_next_step_handler(message, about_bot)
    elif message.text == "Address \U0001F5C2":
        bot.send_location(message.chat.id, 48.74681469552466, -123.22714700126132)
        bot.reply_to(message, "9801 Spalding Road, Pender Island, BC, Canada, British Columbia")
        bot.send_photo(message.chat.id,picture_address, "You can get to the island by ferry. If you don't have your "
                                                        " own transport, you can order a transfer from Otter Bay pier",
                       reply_markup=keyboardInline.keyboard_address())
        #bot.send_message(message.chat.id, "9801 Spalding Road, Pender Island, BC, Canada, British Columbia", reply_markup=keyboards.keyboard_catalog())
        bot.register_next_step_handler(message, catalog_bot)
    elif message.text == "Announcements \u270B":
        bot.reply_to(message, "see the ads here",
                     reply_markup=keyboardInline.keyboard_letter())
    elif message.text == "Review \u270D":
        bot.reply_to(message, "if you want to post a review - write them in the text box",
                     reply_markup=keyboards.keyboard_start())
        bot.register_next_step_handler(message, send_notification)
    else:
        bot.reply_to(message, "Hello, {0.first_name}. Choose the section you need".format(message.from_user),
                     reply_markup=keyboards.keyboard_start())


@bot.message_handler(content_types=['text'])
def send_notification(message):
    if message.text == "About us \U0001F5C2" or message.text == "Address \U0001F5C2" \
            or message.text == "Announcements \u270B":
        bot.reply_to(message, "I didn't receive your suggestion. So please select the section you need again.",
                     reply_markup=keyboards.keyboard_start())
        return
    else:
        open('problem.txt', 'w').write(str(message.chat.id) + ' | ' + message.text + '||')
        bot.send_message(message.chat.id, 'Thank you for your feedback', reply_markup=keyboards.keyboard_start())
        bot.send_message(my_admin, str(message.from_user.id) + ' | ' + message.text + " | "+ today)


def about_bot(message):
    picture_group = [InputMediaPhoto(open("picture/cottage.png", "rb"), caption=" "),
                     InputMediaPhoto(open('picture/villa.png', 'rb')),
                     InputMediaPhoto(open('picture/room_king.png', 'rb')),
                     InputMediaPhoto(open('picture/room_twin.png', 'rb')),
                     ]
    picture_restaurant = open('picture/restaurant.png', 'rb')
    picture_spa = open('picture/spa.png', 'rb')

    if message.text == "Stay \U0001F3E8 \U0001F3E1":
        bot.send_media_group(message.chat.id, picture_group)
        bot.send_message(message.chat.id, "Book your stay on Pender Island. Choose a lodge room, villa or a private "
                                          "cottage.", reply_markup=keyboardInline.keyboard_book())
        bot.register_next_step_handler(message, about_bot)
    elif message.text == "SPA \U0001F486":
        bot.send_photo(message.chat.id, picture_spa,
                       "The Healing Spa offers a range of seasonal packages, body care and massage treatments.",
                       reply_markup=keyboardInline.keyboard_spa())
        bot.register_next_step_handler(message, about_bot)
    elif message.text == "Restaurant \U0001F37D":
        bot.send_photo(message.chat.id, picture_restaurant, "Boasting excellent food and the best ocean views on Pender Island.",
                         reply_markup=keyboardInline.keyboard_restaurant())
        bot.register_next_step_handler(message, about_bot)
    elif message.text == "Other \U0001F4BC":
        bot.send_message(message.chat.id,
                       "What's your favourite thing about PoetsCove?",
                       reply_markup=keyboardInline.keyboard_activities())
        bot.register_next_step_handler(message, about_bot)
    else:
        bot.send_message(message.chat.id, text_redial, reply_markup=keyboards.keyboard_start())
        return


@bot.callback_query_handler(func=lambda call: "address" in call.data)
def how_get(call):
    if call.data == 'address transfer':
        bot.reply_to(call.message, "+18888708889 or +12506292100")
    elif call.data == 'address back':
        bot.send_message(call.message.chat.id, text_choice,
                         reply_markup=keyboards.keyboard_start())


@bot.callback_query_handler(func=lambda call: "book" in call.data)
def how_book(call):
    if call.data == 'book back':
        bot.send_message(call.message.chat.id, text_choice,
                         reply_markup=keyboards.keyboard_catalog())


@bot.callback_query_handler(func=lambda call: "restaurant" in call.data)
def how_order(call):
    if call.data == 'restaurant back':
        bot.send_message(call.message.chat.id, text_choice,
                         reply_markup=keyboards.keyboard_catalog())
    elif call.data == 'restaurant order':
        bot.send_message(call.message.chat.id, "+12506292100")


@bot.callback_query_handler(func=lambda call: "spa" in call.data)
def how_rest(call):
    if call.data == 'spa back':
        bot.send_message(call.message.chat.id, text_choice,
                         reply_markup=keyboards.keyboard_catalog())
    elif call.data == 'spa order':
        bot.send_message(call.message.chat.id, "\uE009+12506292100, \U0001F4E7spa@poetscove.com")


@bot.callback_query_handler(func=lambda call: "activities" in call.data)
def other_activities(call):
    picture_group_walking = [InputMediaPhoto(open("picture/beach.png", "rb"), caption="Breathe in the fresh air while "
                                                   "hiking and enjoy being in touch with nature."),
                     InputMediaPhoto(open('picture/forest.png', 'rb')),
                     InputMediaPhoto(open('picture/deers.png', 'rb')),
                     ]
#,
    picture_group_activities = [InputMediaPhoto(open("picture/jacuzzis.png", "rb"), caption="Enjoy outdoor pools with "
                                                                                    "ocean views and relax in hot "
                                                                                    "tubs. Also at your service tennis "
                                                                                    "court, gym,ping pong table"),
                     InputMediaPhoto(open('picture/pool.png', 'rb')),
                     ]

    if call.data == 'activities back':
        bot.send_message(call.message.chat.id, text_choice,
                         reply_markup=keyboards.keyboard_catalog())
    elif call.data == 'activities walking':
        bot.send_media_group(call.message.chat.id, picture_group_walking)
    elif call.data == 'activities pool':
        bot.send_media_group(call.message.chat.id, picture_group_activities)

if __name__ == "__main__":
    bot.polling()
