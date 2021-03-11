user_input = int(input('How many people are coming to your wedding?\n'))
price = print



if user_input > 200:
    print(20000)
elif user_input < 200 and user_input >= 101:
    print(15000)
elif user_input <= 100 and user_input >= 51:
    print(10000)
elif user_input <=50:
    print(4000)
else:
    print("Price not available")

print('Your wedding will cost '+str(price)+' dollars')