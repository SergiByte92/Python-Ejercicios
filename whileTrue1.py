prompt = "Hola, que tal"
prompt += "\nTodo bien?: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)