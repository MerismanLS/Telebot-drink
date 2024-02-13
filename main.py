import telebot
from telebot import types
import random
import json
import time
time.sleep(5)

bot = telebot.TeleBot('6601149229:AAHlVxHhp8CAtYv30YNK-eP1BEWXd-SZ5LI')
coding = "utf-8"
path = "/data/table.json"
# path = "C:/Users/user/PycharmProjects/tgbot2/table.json"

with open(path, encoding=coding) as t:
    tbl = json.load(t)
def changer(id, value, item):
    with open(path, encoding=coding) as t:
        tbl = json.load(t)
        tbl[id][item] = tbl[id][item] + value
        with open(path, 'w') as f:
            json.dump(tbl, f, ensure_ascii=False, indent=4)


def trezv(id, item):
    with open(path, encoding=coding) as f:
        t = json.load(f)
        t[id][item] = 0
    with open(path, 'w', encoding=coding) as f:
        json.dump(t, f, ensure_ascii=False, indent=4)


counter = 0


@bot.message_handler(commands=['drink'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Водка")
    btn2 = types.KeyboardButton("Сок")
    btn3 = types.KeyboardButton("Пиво")
    btn4 = types.KeyboardButton("Лимонад")
    btn5 = types.KeyboardButton("Кофе")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Чего желаете испить?", reply_markup=markup)

@bot.message_handler(commands=['trezv'])
def start(message):
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Водочка")
    btn2 = types.KeyboardButton("Сочок")
    btn3 = types.KeyboardButton("Пивасик")
    btn4 = types.KeyboardButton("Лимонадик")
    btn5 = types.KeyboardButton("Кофеёк")
    markup2.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Хочешь протрезветь?", reply_markup=markup2)

@bot.message_handler(commands=['stats'])
def start(message):
    markupd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("По водке")
    btn2 = types.KeyboardButton("По соку")
    btn3 = types.KeyboardButton("По пиву")
    btn4 = types.KeyboardButton("По лимонаду")
    btn5 = types.KeyboardButton("По кофе")
    markupd.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "По какому напитку вам нужна статистика?", reply_markup=markupd)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global tbl
    if message.text == "Водка":
        global counter
        if message.from_user.username == "Nastiks_169":
            if counter == 0:
                bot.send_message(message.chat.id, "Хватит пить, пора трезветь!")
                counter += 1
            elif counter == 1:
                bot.send_message(message.chat.id, "Ну ты опять за своё?")
                bot.send_photo(message.chat.id, "https://i.ytimg.com/vi/OO1W8qhn-zw/maxresdefault.jpg")
                counter += 1
            elif counter == 2:
                bot.send_message(message.chat.id, "Ну всё, я обиделся, больше не общаюсь с тобой!")
                bot.send_photo(message.chat.id,
                               "https://avatars.dzeninfra.ru/get-zen_brief/5281279/pub_61c2849a4bfe81623dccd265_61c284cb095ed628a9fa2e30/scale_1200")
                counter += 1
            elif counter < 5 and counter > 2:
                counter += 1
                bot.send_message(message.chat.id, "брбрбрбрбрбрбрбрбрбрбрбр")
            else:
                bot.send_message(message.chat.id, "Ладно, прощаю")
                counter = 0

        with open(path, encoding=coding) as t:
            tbl = json.load(t)
            bot.send_message(message.chat.id, tbl["phrasesvodka"][random.randint(0, 17)])
            drink = random.randint(50, 150)
            bot.send_message(message.chat.id, f"Испито {drink / 10}л")
            id = str(message.from_user.id)
            changer(id, drink, "vodka")
            dr = "vodka"
            bot.send_message(message.chat.id, f"Всего выпито {tbl[id][dr] / 10}Л",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "Сок":
        with open(path, encoding=coding) as t:
            tbl = json.load(t)
            bot.send_message(message.chat.id, tbl["phrasessok"][random.randint(0, 17)])
            drink = random.randint(50, 150)
            bot.send_message(message.chat.id, f"Испито {drink / 10}л")
            id = str(message.from_user.id)
            changer(id, drink, "sok")
            dr = "sok"
            bot.send_message(message.chat.id, f"Всего выпито {tbl[id][dr] / 10}Л",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "Пиво":
        with open(path, encoding=coding) as t:
            tbl = json.load(t)
            bot.send_message(message.chat.id, tbl["phrasespivo"][random.randint(0, 16)])
            drink = random.randint(50, 150)
            bot.send_message(message.chat.id, f"Испито {drink / 10}л")
            id = str(message.from_user.id)
            changer(id, drink, "pivo")
            dr = "pivo"
            bot.send_message(message.chat.id, f"Всего выпито {tbl[id][dr] / 10}Л",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "Лимонад":
        with open(path, encoding=coding) as t:
            tbl = json.load(t)
            bot.send_message(message.chat.id, tbl["phraseslemonade"][random.randint(0, 16)])
            drink = random.randint(50, 150)
            bot.send_message(message.chat.id, f"Испито {drink / 10}л")
            id = str(message.from_user.id)
            changer(id, drink, "lemonade")
            dr = "lemonade"
            bot.send_message(message.chat.id, f"Всего выпито {tbl[id][dr] / 10}Л",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "Кофе":
        with open(path, encoding=coding) as t:
            tbl = json.load(t)
            bot.send_message(message.chat.id, tbl["phrasescoffee"][random.randint(0, 16)])
            drink = random.randint(50, 150)
            bot.send_message(message.chat.id, f"Испито {drink / 10}л")
            id = str(message.from_user.id)
            changer(id, drink, "coffee")
            dr = "coffee"
            bot.send_message(message.chat.id, f"Всего выпито {tbl[id][dr] / 10}Л",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "По водке":
        with open(path, encoding=coding) as tbl:
            h = json.load(tbl)
            alco = dict()
            alco["Настюшик"] = h["5716501004"]["vodka"]
            alco["СерСаныч"] = h["1076372910"]["vodka"]
            alco["Польша"] = h["1125064311"]["vodka"]
            alco["Аняняняня"] = h["5226591737"]["vodka"]
            alco["Аделиииина"] = h["945202594"]["vodka"]
            alco["Михаил"] = h["1390110897"]["vodka"]
            ad = sorted(alco.items(), key=lambda x: x[1])
            bot.send_message(message.chat.id, f"ТОП ВОДКИ \n"
                                              f"\n"
                                              f"Главный алкаш - {ad[5][0]}, выпито целых {ad[5][1] / 10} л,\n"
                                              f"\n"
                                              f"На втором месте - {ad[4][0]}, всего выпито {ad[4][1] / 10} л,\n"
                                              f"\n"
                                              f"Бронзовый призёр бара - {ad[3][0]}, испито {ad[3][1] / 10} л,\n"
                                              f"\n"
                                              f"На почти третьем месте - {ad[2][0]}, употреблено {ad[2][1] / 10} л,\n"
                                              f"\n"
                                              f"Замыкает топ-5 - {ad[1][0]}, поглощено {ad[1][1] / 10} л,\n"
                                              f"\n"
                                              f"Ну и самый трезвый из нас - {ad[0][0]}, выпито всего пару капель {ad[0][1] / 10} л! ",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "По пиву":
        with open(path, encoding=coding) as tbl:
            h = json.load(tbl)
            alco = dict()
            alco["Настюшик"] = h["5716501004"]["pivo"]
            alco["СерСаныч"] = h["1076372910"]["pivo"]
            alco["Польша"] = h["1125064311"]["pivo"]
            alco["Аняняняня"] = h["5226591737"]["pivo"]
            alco["Аделиииина"] = h["945202594"]["pivo"]
            alco["Михаил"] = h["1390110897"]["pivo"]
            ad = sorted(alco.items(), key=lambda x: x[1])
            bot.send_message(message.chat.id, f"ТОП ПИВА \n"
                                              f"\n"
                                              f"Главный бухич - {ad[5][0]}, выпито целых {ad[5][1] / 10} л,\n"
                                              f"\n"
                                              f"На втором месте - {ad[4][0]}, всего выпито {ad[4][1] / 10} л,\n"
                                              f"\n"
                                              f"Бронзовый призёр бара - {ad[3][0]}, испито {ad[3][1] / 10} л,\n"
                                              f"\n"
                                              f"На почти третьем месте - {ad[2][0]}, употреблено {ad[2][1] / 10} л,\n"
                                              f"\n"
                                              f"Замыкает топ-5 - {ad[1][0]}, поглощено {ad[1][1] / 10} л,\n"
                                              f"\n"
                                              f"Ну и самый адекватный из нас - {ad[0][0]}, выпито всего пару капель {ad[0][1] / 10} л! ",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "По соку":
        with open(path, encoding=coding) as tbl:
            h = json.load(tbl)
            alco = dict()
            alco["Настюшик"] = h["5716501004"]["sok"]
            alco["СерСаныч"] = h["1076372910"]["sok"]
            alco["Польша"] = h["1125064311"]["sok"]
            alco["Аняняняня"] = h["5226591737"]["sok"]
            alco["Аделиииина"] = h["945202594"]["sok"]
            alco["Михаил"] = h["1390110897"]["sok"]
            ad = sorted(alco.items(), key=lambda x: x[1])
            bot.send_message(message.chat.id, f"ТОП СОКА \n"
                                              f"\n"
                                              f"Главный ребёнок - {ad[5][0]}, выпито целых {ad[5][1] / 10} л,\n"
                                              f"\n"
                                              f"На втором месте - {ad[4][0]}, всего выпито {ad[4][1] / 10} л,\n"
                                              f"\n"
                                              f"Бронзовый призёр бара - {ad[3][0]}, испито {ad[3][1] / 10} л,\n"
                                              f"\n"
                                              f"На почти третьем месте - {ad[2][0]}, употреблено {ad[2][1] / 10} л,\n"
                                              f"\n"
                                              f"Замыкает топ-5 - {ad[1][0]}, поглощено {ad[1][1] / 10} л,\n"
                                              f"\n"
                                              f"Ну и самый чистый из нас - {ad[0][0]}, выпито всего пару капель {ad[0][1] / 10} л! ",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "По лимонаду":
        with open(path, encoding=coding) as tbl:
            h = json.load(tbl)
            alco = dict()
            alco["Настюшик"] = h["5716501004"]["lemonade"]
            alco["СерСаныч"] = h["1076372910"]["lemonade"]
            alco["Польша"] = h["1125064311"]["lemonade"]
            alco["Аняняняня"] = h["5226591737"]["lemonade"]
            alco["Аделиииина"] = h["945202594"]["lemonade"]
            alco["Михаил"] = h["1390110897"]["lemonade"]
            ad = sorted(alco.items(), key=lambda x: x[1])
            bot.send_message(message.chat.id, f"ТОП ЛИМОНАДА \n"
                                              f"\n"
                                              f"Главный дитятко - {ad[5][0]}, выпито целых {ad[5][1] / 10} л,\n"
                                              f"\n"
                                              f"На втором месте - {ad[4][0]}, всего выпито {ad[4][1] / 10} л,\n"
                                              f"\n"
                                              f"Бронзовый призёр бара - {ad[3][0]}, испито {ad[3][1] / 10} л,\n"
                                              f"\n"
                                              f"На почти третьем месте - {ad[2][0]}, употреблено {ad[2][1] / 10} л,\n"
                                              f"\n"
                                              f"Замыкает топ-5 - {ad[1][0]}, поглощено {ad[1][1] / 10} л,\n"
                                              f"\n"
                                              f"Ну и самый скучный из нас - {ad[0][0]}, выпито всего пару капель {ad[0][1] / 10} л! ",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "По кофе":
        with open(path, encoding=coding) as tbl:
            h = json.load(tbl)
            alco = dict()
            alco["Настюшик"] = h["5716501004"]["coffee"]
            alco["СерСаныч"] = h["1076372910"]["coffee"]
            alco["Польша"] = h["1125064311"]["coffee"]
            alco["Аняняняня"] = h["5226591737"]["coffee"]
            alco["Аделиииина"] = h["945202594"]["coffee"]
            alco["Михаил"] = h["1390110897"]["coffee"]
            ad = sorted(alco.items(), key=lambda x: x[1])
            bot.send_message(message.chat.id, f"ТОП КОФЕ \n"
                                              f"\n"
                                              f"Дольше всех бодрствует - {ad[5][0]}, выпито целых {ad[5][1] / 10} л,\n"
                                              f"\n"
                                              f"На втором месте - {ad[4][0]}, всего выпито {ad[4][1] / 10} л,\n"
                                              f"\n"
                                              f"Бронзовый призёр бара - {ad[3][0]}, испито {ad[3][1] / 10} л,\n"
                                              f"\n"
                                              f"На почти третьем месте - {ad[2][0]}, употреблено {ad[2][1] / 10} л,\n"
                                              f"\n"
                                              f"Замыкает топ-5 - {ad[1][0]}, поглощено {ad[1][1] / 10} л,\n"
                                              f"\n"
                                              f"Ну и самый заспанный из нас - {ad[0][0]}, выпито всего пару капель {ad[0][1] / 10} л! ",
                             reply_markup=types.ReplyKeyboardRemove())

    elif message.text == "Водочка":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, водяра")
        btn2 = types.KeyboardButton("нет.")
        markup3.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы уверены?", reply_markup=markup3)

    elif message.text == "Да, водяра":
        id = str(message.from_user.id)
        trezv(id, "vodka")
        bot.send_message(message.chat.id, "вы стали трезвенником.", reply_markup=types.ReplyKeyboardRemove())
        bot.send_photo(message.chat.id, "https://www.meme-arsenal.com/memes/f8c8cf7d287ea08aa70e37dd86799217.jpg")

    elif message.text == "Сочок":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, сочочек")
        btn2 = types.KeyboardButton("нет.")
        markup3.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы уверены?", reply_markup=markup3)

    elif message.text == "Да, сочочек":
        id = str(message.from_user.id)
        trezv(id, "sok")
        bot.send_message(message.chat.id, "вы стали трезвенником.", reply_markup=types.ReplyKeyboardRemove())
        bot.send_photo(message.chat.id, "https://www.meme-arsenal.com/memes/f8c8cf7d287ea08aa70e37dd86799217.jpg")

    elif message.text == "Пивасик":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, пивко")
        btn2 = types.KeyboardButton("нет.")
        markup3.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы уверены?", reply_markup=markup3)

    elif message.text == "Да, пивко":
        id = str(message.from_user.id)
        trezv(id, "pivo")
        bot.send_message(message.chat.id, "вы стали трезвенником.", reply_markup=types.ReplyKeyboardRemove())
        bot.send_photo(message.chat.id, "https://www.meme-arsenal.com/memes/f8c8cf7d287ea08aa70e37dd86799217.jpg")

    elif message.text == "Лимонадик":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, лимонэйд")
        btn2 = types.KeyboardButton("нет.")
        markup3.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы уверены?", reply_markup=markup3)

    elif message.text == "Да, лимонэйд":
        id = str(message.from_user.id)
        trezv(id, "lemonade")
        bot.send_message(message.chat.id, "вы стали трезвенником.", reply_markup=types.ReplyKeyboardRemove())
        bot.send_photo(message.chat.id, "https://www.meme-arsenal.com/memes/f8c8cf7d287ea08aa70e37dd86799217.jpg")

    elif message.text == "Кофеёк":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, кофэй")
        btn2 = types.KeyboardButton("нет.")
        markup3.add(btn1, btn2)
        bot.send_message(message.chat.id, "Вы уверены?", reply_markup=markup3)

    elif message.text == "Да, кофэй":
        id = str(message.from_user.id)
        trezv(id, "coffee")
        bot.send_message(message.chat.id, "вы стали трезвенником.", reply_markup=types.ReplyKeyboardRemove())
        bot.send_photo(message.chat.id, "https://www.meme-arsenal.com/memes/f8c8cf7d287ea08aa70e37dd86799217.jpg")

    elif message.text == "нет.":
        bot.send_message(message.chat.id, "Правильное решение", reply_markup=types.ReplyKeyboardRemove())


bot.polling(none_stop=True, interval=0)
