BOT_API_TOKEN = '5958854543:AAFh4AKuPU1I6Nq3oUIqALhDdr9eHpJAvu0'
WEATHER_API_KEY = '20ebde480d3b3c663f7b4b617c5ab97c'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)
