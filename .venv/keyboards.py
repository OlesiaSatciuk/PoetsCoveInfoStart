from telebot import types


def keyboard_start():
    start_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    catalog = types.KeyboardButton(text="About us \U0001F5C2")
    address = types.KeyboardButton(text="Address \U0001F5C2")
    my_loc = types.KeyboardButton(text="Send location", request_location=True)
    my_phone = types.KeyboardButton(text="Order a call \u260E", request_contact=True)
    announcements = types.KeyboardButton(text="Announcements \u270B")
    review = types.KeyboardButton(text="Review \u270D")
    start_keyboard.add(catalog, address, announcements, review, my_phone, my_loc )
    return start_keyboard


def keyboard_phone():
    phone_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    my_phone = types.KeyboardButton(text="Phone ", request_contact=True)
    phone_keyboard.add(my_phone)
    return phone_keyboard


def keyboard_catalog():
    catalog_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    #repair = types.KeyboardButton(text="Ремонт\n \U0001F6E0 \U0001F6B2 \U0001F477 \U0001F4BB  ...")
    accommodation = types.KeyboardButton(text='Stay \U0001F3E8 \U0001F3E1')
    restaurant = types.KeyboardButton(text="Restaurant \U0001F37D") #\U0001F3C3 \U0001F45F
    spa = types.KeyboardButton(text="SPA \U0001F486")
    #edukation = types.KeyboardButton(text="Навчання \U0001F4D6")
    #bus = types.KeyboardButton(text="Розклад автобусів \U0001F68C")
    other = types.KeyboardButton(text="Other \U0001F4BC")
    back = types.KeyboardButton(text="Back \U0001F519")
    catalog_keyboard.add(accommodation, restaurant, spa, other, back)
    return catalog_keyboard


def keyboard_home():
    catalog_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    villas = types.KeyboardButton(text="Villa \U0001F3E0")
    #repair = types.KeyboardButton(text="Ремонт\n \U0001F6E0 \U0001F6B2 \U0001F477 \U0001F4BB  ...")
    cottages = types.KeyboardButton(text='Cottage \U0001F3E1')
    rooms = types.KeyboardButton(text="Room \U0001F3E8")
    #edukation = types.KeyboardButton(text="Навчання \U0001F4D6")
    #bus = types.KeyboardButton(text="Розклад автобусів \U0001F68C")
    other = types.KeyboardButton(text="Other \U0001F4BC")
    back = types.KeyboardButton(text="Back \U0001F519")
    catalog_keyboard.add(villas, cottages,  rooms, other, back)
    return catalog_keyboard

def keyboard_service():
    service_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    service_keyboard.add(*[types.KeyboardButton(name) for name in ["Фото", "Авто"]])
    service_keyboard.add(*[types.KeyboardButton(name) for name in ["Ритуальні", "Квіти"]])
    service_keyboard.add(*[types.KeyboardButton(name) for name in ["Чищення", "Шиття"]])
    service_keyboard.add(*[types.KeyboardButton(name) for name in ["Меблі", "Повернутись"]])
    return service_keyboard


def keyboard_service_remove():
    service_keyboard = types.ReplyKeyboardRemove(selective=False)
    return service_keyboard


def keyboard_medicine():
    medicine_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    tmo = types.KeyboardButton(text="Лікарня")
    pmd = types.KeyboardButton(text="Сімейна медицина")
    dent = types.KeyboardButton(text="Стоматологія")
    veterinary = types.KeyboardButton(text="Ветмедицина")
    kovel_tmo = types.KeyboardButton(text="Ковель МТМО")
    go_back = types.KeyboardButton(text="Повернутись")
    medicine_keyboard.add(tmo, pmd, dent, veterinary, kovel_tmo, go_back)
    return medicine_keyboard


def keyboard_medicine_remove():
    medicine_keyboard = types.ReplyKeyboardRemove(selective=False)
    return medicine_keyboard


def keyboard_other():
    other_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    jurist = types.KeyboardButton(text="Юридичні")
    communal = types.KeyboardButton(text="Комунальні")
    different = types.KeyboardButton(text="Різне")
    go_back = types.KeyboardButton(text="Повернутись")
    other_keyboard.add(jurist, communal, different, go_back)
    return other_keyboard


def keyboard_other_remove():
    other_keyboard = types.ReplyKeyboardRemove(selective=False)
    return other_keyboard


def keyboard_education():
    other_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    education = types.KeyboardButton(text="Репетитор")
    speech = types.KeyboardButton(text="Логопед")
    go_back = types.KeyboardButton(text="Повернутись")
    other_keyboard.add(speech, education, go_back)
    return other_keyboard


def keyboard_food():
    food_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    restaurant = types.KeyboardButton(text="Ресторани")
    catering = types.KeyboardButton(text="Кейтеринг")
    takeout = types.KeyboardButton(text="Їжа на винос")
    halls = types.KeyboardButton(text="Банкетні зали")
    products = types.KeyboardButton(text="Продукти(харч)")
    go_back = types.KeyboardButton(text="Повернутись")
    food_keyboard.add(restaurant, catering, takeout, halls, products, go_back)
    return food_keyboard


def keyboard_food_remove():
    food_keyboard = types.ReplyKeyboardRemove(selective=False)
    return food_keyboard
