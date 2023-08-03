from botwork.functions import conversation as chat

def mapping(data):

    if "day" in data:
        chat.day()
    
    elif "exit" in data:
        chat.Exit()
    
    elif "time" in data:
        chat.time()
    
    elif "news" in data:
        chat.news()

    elif "temperature" in data:
        chat.weather()
