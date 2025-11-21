prompt = "Hola, que tal"
prompt += "\nQue ciudad te gustaría ir?: "


while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Me encanta ir {city.title()}!")