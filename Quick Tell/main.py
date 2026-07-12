import requests               # API calls karne ke liye (weather, news)
import pyttsx3                # text-to-speech ke liye
from dotenv import load_dotenv
import os                     # environment variables (.env) access karne ke liye
import webbrowser             # browser mein URL kholne ke liye
from google import genai      # Gemini AI se baat karne ke liye
from urllib.parse import quote  # search query ko URL-safe banane ke liye

load_dotenv()  # .env file se saari keys load karo

# Sabhi API keys .env file se secure tarike se load ki ja rahi hain
weather_api_key = os.getenv("WEATHER_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")


def speak(text):
    """Text ko console pe print karta hai aur voice mein bhi bolta hai."""
    engine = pyttsx3.init()   # har call pe naya engine banate hain taaki voice atke nahi
    print(text)
    engine.say(text)
    engine.runAndWait()


def get_weather(city):
    """OpenWeatherMap API se diye gaye city ka current weather laata hai."""
    params = {"q": city,
              "appid": weather_api_key,
              "units": "metric"}   # metric = Celsius mein temperature
    r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    print(f"status code: {r.status_code}")

    if r.status_code == 200:   # 200 matlab request successful thi
        data = r.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
    else:
        # agar city galat ho ya API fail ho jaye
        return f"{city} Data not found 404!"

    return (f'It is currently {temp}° in {city}, {description}, humidity {humidity}%')


def get_news():
    """NewsAPI se top 5 headlines laata hai, bolta hai, aur browser mein kholta hai."""
    params = {"country": "us",
              "apiKey": news_api_key}
    r = requests.get("https://newsapi.org/v2/top-headlines", params=params)
    print(f"status code: {r.status_code}")

    if r.status_code == 200:
        data = r.json()
        article = data.get("articles")   # 'articles' list nikal rahe hain response se
        print(f"number of article: {len(article)}")

        speak("Here are your top news articles")
        for articles in article[:5]:      # sirf top 5 headlines
            speak(articles['title'])
            webbrowser.open(articles['url'])   # article ka link browser mein khol do
    else:
        print('Couldn\'t find news sorry!')


def parse_command(command):
    """
    User ke input command ko check karke decide karta hai
    kaunsa function call karna hai (weather / youtube / news / AI).
    """
    command = command.lower().strip()

    if command.startswith("weather"):
        part = command.split(maxsplit=1)   # "weather" aur city ko alag karo
        city = part[1]
        result = get_weather(city)
        speak(result)

    elif command.startswith("youtube"):
        part = command.split(maxsplit=1)   # "youtube" aur channel/naam alag karo
        name = part[1]
        result = open_app(name)

    elif command == "news":
        get_news()

    else:
        # koi bhi aur command match na ho to Gemini AI se jawab lo
        answer = ask_ai(command)
        speak(answer)


def open_app(name):
    """Diye gaye naam ko YouTube pe search karke browser mein khol deta hai."""
    url = "https://www.youtube.com/results?search_query=" + quote(name)
    webbrowser.open(url)


def ask_ai(question):
    """Gemini AI model ko sawaal bhejta hai aur uska jawab return karta hai."""
    client = genai.Client(api_key=gemini_api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    return response.text


def main():
    """Program ka entry point — welcome bolta hai aur commands loop mein leta hai."""
    speak('Assistant ready')
    while True:
        command = input('Enter command: ')
        if command == 'exit':
            break
        parse_command(command)


main()