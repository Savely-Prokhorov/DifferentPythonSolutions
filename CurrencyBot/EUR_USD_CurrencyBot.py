from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Update, Bot
from lxml import etree
from urllib.request import urlopen
import json
import time

bot_name = "EUR_USD_CurrencyRate"
token = '441787376:AAFuVAMCI3Ou8wHZigk4jTQ-FQp7MT4jMqY'
chat_id = 405392565

EurUsdCurUrl = 'https://query.yahooapis.com/v1/public/yql?q=select+*+from+yahoo.finance.xchange+where+pair' \
               '+=+"EURUSD"&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
CbCurUrl = 'http://informer.kovalut.ru/webmaster/getxml.php?kod=7701'

USD_cur, EUR_cur, EUR_USD_cur, old_Eur_Usd = 0, 0, 0, 1.1894
count, currency = 0, 0
new_currency_arr, difference_arr = [], []


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Start")


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def send_currency(bot, update, new_currency_list, difference_list, date):
    usd_change, eur_change, eur_usd_change = "", "", ""

    usd_currency, usd_difference = new_currency_list[0], round(difference_list[0], 2)
    eur_currency, eur_difference = new_currency_list[1], round(difference_list[1], 2)
    eur_usd_currency, eur_usd_difference = new_currency_list[2], round(difference_list[2], 2)
    upd_date = date

    if usd_difference > 0:
        usd_change = "↑"
    else:
        usd_change = "↓"

    if eur_difference > 0:
        eur_change = "↑"
    else:
        eur_change = "↓"

    if eur_usd_difference > 0:
        eur_usd_change = "↑"
    else:
        eur_usd_change = "↓"

    message = """Курсы валют на <i>{date}:</i>
    1 USD = <b>{usd_currency}</b> RUB {usd_change} ({usd_difference:+})
    1 EUR = <b>{eur_currency}</b> RUB {eur_change} ({eur_difference:+})
    1 EUR =   <b>{eur_usd_currency}</b> USD {eur_usd_change} ({eur_usd_difference:+})"""\
        .format(date=upd_date, usd_currency=usd_currency, usd_change=usd_change, eur_currency=eur_currency,
                eur_change=eur_change, eur_usd_currency=eur_usd_currency, eur_usd_change=eur_usd_change,
                usd_difference=usd_difference, eur_difference=eur_difference, eur_usd_difference=eur_usd_difference)

    bot.sendMessage(chat_id, text=message, parse_mode="HTML")

    new_currency_list, difference_list = [], []


updater = Updater(token)

bot_obj = Bot(token)

updater = Updater(token)
upd = Update(update_id=867755814, message=currency)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))


def timer():
    t = time.localtime()

    if t[3] >= 14 and t[4] >= 5:
        hours_till_upd = 24 - t[3] + 14
    elif t[3] <= 14 and t[4] < 5:
        hours_till_upd = 14 - t[3]
    elif t[3] < 14 and t[4] > 5:
        hours_till_upd = 14 - t[3] - 1

    if t[4] < 5:
        minutes_till_upd = 5 - t[4]
    elif t[4] > 5:
        minutes_till_upd = 60 - t[4] + 5
    else:
        minutes_till_upd = 0

    print(hours_till_upd)
    seconds_till_upd = minutes_till_upd * 60 + hours_till_upd * 3600 + t[5]
    print(seconds_till_upd)
    time.sleep(seconds_till_upd)


def get_currency():
    global old_Eur_Usd
    current_USD_Rate = USD_cur
    current_EUR_Rate = EUR_cur
    current_EUR_USD_Rate = EUR_USD_cur
    if old_Eur_Usd == 0:
        old_Eur_Usd_cur = old_Eur_Usd
    counter = count

    EurUsdInfo = urlopen(EurUsdCurUrl)
    EurUsd = EurUsdInfo.read()

    data = json.loads(EurUsd)
    dict = data["query"]["results"]["rate"]

    if current_EUR_USD_Rate != dict["Rate"]:
        new_Eur_Usd_cur = dict["Rate"]
    else:
        counter += 1
        time.sleep(300)
        get_currency()

    tree = etree.parse(CbCurUrl)

    date = tree.xpath("/Exchange_Rates/Central_Bank_RF/USD/New/Digital_Date/text()")[0]

    if current_USD_Rate != tree.xpath("/Exchange_Rates/Central_Bank_RF/USD/New/Exch_Rate/text()")[0]:
        new_USD_cur = tree.xpath("/Exchange_Rates/Central_Bank_RF/USD/New/Exch_Rate/text()")[0]
    else:
        counter += 1
        time.sleep(300)
        get_currency()

    old_USD_cur = tree.xpath("/Exchange_Rates/Central_Bank_RF/USD/Old/Exch_Rate/text()")[0]

    if current_EUR_Rate != tree.xpath("/Exchange_Rates/Central_Bank_RF/EUR/New/Exch_Rate/text()")[0]:
        new_EUR_cur = tree.xpath("/Exchange_Rates/Central_Bank_RF/EUR/New/Exch_Rate/text()")[0]
    else:
        counter += 1
        time.sleep(300)
        get_currency()

    old_EUR_cur = tree.xpath("/Exchange_Rates/Central_Bank_RF/EUR/Old/Exch_Rate/text()")[0]

    print(date, new_USD_cur, old_USD_cur)
    print(new_EUR_cur, old_EUR_cur)
    print(new_Eur_Usd_cur)

    print()

    USD_cur_difference = float(new_USD_cur) - float(old_USD_cur)
    EUR_cur_difference = float(new_EUR_cur) - float(old_EUR_cur)
    EUR_USD_cur_difference = float(new_Eur_Usd_cur) - float(old_Eur_Usd_cur)

    new_currency_arr.append(new_USD_cur)
    new_currency_arr.append(new_EUR_cur)
    new_currency_arr.append(new_Eur_Usd_cur)
    difference_arr.append(USD_cur_difference)
    difference_arr.append(EUR_cur_difference)
    difference_arr.append(EUR_USD_cur_difference)

    try:
        updater.dispatcher.add_handler(MessageHandler(callback=send_currency(
            bot_obj, upd, new_currency_list=new_currency_arr, difference_list=difference_arr, date=date)))
    except TypeError:
        pass

    # sleeping till 00:05 then update old currency
    sleeping_time = 36000 - counter * 300
    if sleeping_time > 0:
        time.sleep(36000 - counter * 300)
    else:
        time.sleep(36000)
    old_Eur_Usd_cur, old_Eur_Usd = new_Eur_Usd_cur

    # sleeping till 14:05 and all by new
    t = time.localtime()
    hours = t[3]
    minutes = t[4]
    seconds = t[5]
    day_of_week = t[6]

    if hours >= 0:
        hours_till_upd = 14 - hours
    else:
        hours_till_upd = 24 - hours + 14

    if minutes < 5:
        minutes_till_upd = 5 - t[4]
    elif minutes > 5:
        minutes_till_upd = 60 - t[4] + 5
    else:
        minutes_till_upd = 0

    if day_of_week == 5:
        seconds_till_upd = 2 * 24 * 3600 + hours_till_upd * 3600 + minutes_till_upd * 60 + seconds

    seconds_till_upd = hours_till_upd * 3600 + minutes_till_upd * 60 + seconds

    time.sleep(seconds_till_upd)
    print("Буду спать ", seconds_till_upd, "секунд")
    get_currency()


timer()
get_currency()

updater = Updater(token)

bot = updater.bot(token)
bot_obj = Bot(token)

updater = Updater(token)
upd = Update(update_id=867755814, message=currency)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
