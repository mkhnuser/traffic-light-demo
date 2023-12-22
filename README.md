# Traffic Light Weather Service Demo

## Основные положения

В этом репозитории пытливый читатель сможет найти реализацию простого сервиса погоды. Техническое задание может быть найдено [тут](https://docs.google.com/document/d/1rsAkjz65c0081AGYkyIpPi_IOhAfTYIRMDHBUlQU-8g/edit#heading=h.3axn2igz47kq). Я выполнил два обязательных пункта, а третий необязательный оставил в качестве дополнительного упражнения на следующий раз.

## Инструкция по установке

Для установки проекта, введи команды ниже. Я буду полагать, что ты используешь bash.

<pre>
git clone https://github.com/mkhnuser/traffic-light-demo.git
cd traffic-light-demo
pip install -r requirements.txt
</pre>

## Инструкция по запуску

Давай установим переменные окружения. Более того, так как это тестовое задание, давай я дам свои.

Я буду опять полагать, что ты используешь bash.

<pre>
export YANDEX_WEATHER_API_KEY=10e10fba-a07f-41e8-8460-a0f1b906d384
export TEMP_DJANGO_SECRET_KEY="django-insecure-!%p$w768e-my)))erzmz*osb^2kpvqie0zj00ev$9klfnp2bxz"
export TELEGRAM_BOT_TOKEN=6436194606:AAHoyO4CZNf5P_H-A6ZC4y-Xl_WcQ5fT84g
</pre>

Теперь запустим наш backend, который обрабатывает запросы на полечение погоды.

Положим, что ты в директории traffic-light-demo. Сделаем это так:

<pre>
cd simple_weather_service
python manage.py makemigrations && python manage.py migrate
python manage.py runserver
</pre>

Теперь ты можешь прямо в своём браузере обратиться по следующему пути: *http://127.0.0.1:8000/api/v1/weather?city=Москва*. В ответ ты получишь JSON response, который содержит текущую температуру воздуха в Москве, давление и скорость ветра.

---

Давай запустим телеграм-бота, который будет служить интерфейсом к нашему backend.

Положим, что ты в директории traffic-light-demo. Сделаем это так:

<pre>
cd telegram_bot
python bot.py
</pre>

Запуск приложения завершён!

## Инструкция по использованию

Открой, пожалуйста, телеграм-клиент. В нём ты сможешь найти телеграм бота, которого ты запустил. Вот его id: _@TrafficLightAwesomeTestBot\_._ Бот также может быть найден по URL: https://t.me/TrafficLightAwesomeTestBot.

Теперь напиши что-нибудь боту и следуй его инструкциям.
