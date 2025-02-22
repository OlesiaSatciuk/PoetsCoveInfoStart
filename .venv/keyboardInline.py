from telebot import types

def keyboard_start():
    start_keyboard = types.InlineKeyboardMarkup(keyboard=None, row_width=1)
    catalog = types.KeyboardButton(text="/start")
    question = types.KeyboardButton(text="/help")
    start_keyboard.add(catalog, question)
    return start_keyboard


def keyboard_address():
    get_keyboard = types.InlineKeyboardMarkup(keyboard=None, row_width=1)
    ferries = types.InlineKeyboardButton("Book sailings by ferry", callback_data="address ferries",
                                         url="https://www.bcferries.com/")
    transfer = types.InlineKeyboardButton("Order transfer", callback_data="address transfer")
    back = types.InlineKeyboardButton("Back", callback_data="address back")
    get_keyboard.add(ferries, transfer, back)
    return get_keyboard


def keyboard_letter():
    writing_keyboard = types.InlineKeyboardMarkup(keyboard=None)
    letter_field = types.InlineKeyboardButton("ОГОЛОШЕННЯ", url="https://t.me/PoetsCove")
    writing_keyboard.add(letter_field)
    return writing_keyboard


def keyboard_book():
    book_keyboard = types.InlineKeyboardMarkup(keyboard=None)
    book_field = types.InlineKeyboardButton("Book now", url="https://www.poetscove.com/rooms")
    back = types.InlineKeyboardButton(text="Back", callback_data="book back")
    book_keyboard.add(book_field, back)
    return book_keyboard


def keyboard_restaurant():
    restaurant_keyboard = types.InlineKeyboardMarkup(keyboard=None)
    menu = types.InlineKeyboardButton("View menu", url="https://www.poetscove.com/dining/aurora")
    order = types.InlineKeyboardButton("Order food", callback_data="restaurant order")
    back = types.InlineKeyboardButton(text="Back", callback_data="restaurant back")
    restaurant_keyboard.add(menu, order, back)
    return restaurant_keyboard


def keyboard_spa():
    restaurant_keyboard = types.InlineKeyboardMarkup(keyboard=None)
    book = types.InlineKeyboardButton("Book an Appointment", url="https://poetscove.janeapp.com/#staff_member/1")
    order = types.InlineKeyboardButton("For more information", callback_data="spa order")
    back = types.InlineKeyboardButton(text="Back", callback_data="spa back")
    restaurant_keyboard.add(book, order, back)
    return restaurant_keyboard


def keyboard_activities():
    activities_keyboard = types.InlineKeyboardMarkup(keyboard=None)
    wedding = types.InlineKeyboardButton("Celebrations&Weddings", url="https://www.poetscove.com/weddings")
    walk = types.InlineKeyboardButton("Walking", callback_data="activities walking")
    pool = types.InlineKeyboardButton("Activities", callback_data="activities pool")
    boat = types.InlineKeyboardButton("Dock Your Boat", url="https://www.poetscove.com/the-marina")
    back = types.InlineKeyboardButton(text="Back", callback_data="activities back")
    activities_keyboard.add(walk, pool, boat, wedding, back)
    return activities_keyboard