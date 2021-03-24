import requests
from decimal import Decimal
import datetime


def get_parc(resp, argv, text):
    """
    Получает значение любого поля в HTML тегах вида <text>return</text>


    :param resp: ответ от сата, из которого будем получать данные
    :param argv: код валюты , для которой получаемс данные
    :param text: поле, которое хотим получать
    :return:
    """
    return resp.text.split(argv)[1].split(text)[1][1:-2]


def currency_rates(arg):
    """

    :param arg: Код валюты для получения курса
    :return: возвращает список из даты, наименования валюты и собственно курса
    """
    arg = arg.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    if response.text.find(arg) != -1:
        nominal = int(get_parc(response, arg, "Nominal"))
        my_date = datetime.datetime.strptime(response.text.split("Date")[1].split('"')[1], "%d.%m.%Y").date()
        name = get_parc(response, arg, "Name")

        new_value = Decimal(".".join(get_parc(response, arg, "Value").split(','))).quantize(Decimal("1.00"))

        return [my_date, name, new_value / nominal]


if __name__ == '__main__':
    lst = currency_rates("usd")
    print(f"на  {lst[0]} Курс 1 {lst[1]} равен {lst[2]} рублей")
    lst = currency_rates("Eur")
    print(f"на  {lst[0]} Курс 1 {lst[1]} равен {lst[2]} рублей")
