weather_input = input('How is the weather?').capitalize().strip()
weather = ['Sunny', 'Raing','Snowy']
activity = ['Go for a walk', 'Read a book', 'Build a snowman']
if weather_input in weather:
    idx = weather.index(weather_input)
    print(activity[idx])
else:
    print('Information not available')