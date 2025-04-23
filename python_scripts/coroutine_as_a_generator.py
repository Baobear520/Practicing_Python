
def message_handler():
    response = None
    while True: # Endless iteration
        message = yield response # the value of "response" becomes equal to what is being sent into the generator
        if message == "ping":
            response = "pong"
        else:
            response = "unknown"


handler = message_handler()

next(handler)  # Инициализация
print(handler.send("ping"))  # pong
print(handler.send("test"))  # unknown

handler.close()
