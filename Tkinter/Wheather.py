import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    country = country_entry.get()
    api_key = 'YOUR_API_KEY_HERE'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    weather_label.config(text=f'Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description.capitalize()}')
    
root = tk.Tk()
root.title('Weather App')

city_label = tk.Label(root, text='City')
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

country_label = tk.Label(root, text='Country Code')
country_label.pack()
country_entry = tk.Entry(root)
country_entry.pack()

search_button = tk.Button(root, text='Search', command=get_weather)
search_button.pack()

weather_label = tk.Label(root, text='')
weather_label.pack()

root.mainloop()
