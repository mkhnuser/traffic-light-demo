import os
from json import JSONDecodeError

import requests
import telebot
from telebot import types


bot = telebot.TeleBot(os.environ["TELEGRAM_BOT_TOKEN"])


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    current_weather_button = types.InlineKeyboardButton(
        text="Узнать погоду",
        callback_data="foobarbaz"
    )
    keyboard.add(current_weather_button)
    bot.send_message(
        message.from_user.id,
        text="Здравствуйте! Чтобы получить прогноз погоды, нажмите на кнопку ниже.",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    message = bot.send_message(
        call.message.chat.id,
        "Отлично! Давайте выберем город, прогноз для которого вам интересен. Например, введите Новосибирск."
    )
    bot.register_next_step_handler(message, get_weather_forecast)


def get_weather_forecast(message):
    bot.send_message(
        message.chat.id,
        "Пожалуйста, ожидайте..."
    )
    response = requests.get(
        f"http://localhost:8000/api/v1/weather?city={message.text}"
    )
    if not response.ok:
        return bot.send_message(
            message.chat.id,
            "Увы, что-то пошло не так. Вы точно верно ввели город?"
        )
    try:
        _ = response.json()
    except JSONDecodeError:
        return bot.send_message(
            message.chat.id,
            "Увы, что-то пошло не так на нашей стороне."
        )

    bot.send_message(
        message.chat.id,
        f"Великолепно! Прогноз погоды для {message.text}:"
        f"""\n\nТемпература: {_["temperature"]};"""
        f"""\nДавление (миллиметров рт. столба): {_["pressure"]};"""
        f"""\nСкорость ветра (м/с): {_["wind_speed"]}."""
    )


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0.25)
