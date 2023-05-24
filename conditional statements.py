def drink(money):
    if money >= 2:
        return 'You got yourself a drink!'
    else:
        return 'No drink for you!'
print(drink(3))
print(drink(1))

def alchohol(age,money):
    if(age >= 21) and (money >= 5):
        return 'Drinks na mayengs!!'
    elif (age >= 21) and (money > 5 ):
        return 'Tafta pesa nanii!'
    elif(age <21) and (money >= 5):
        return 'Kumbe ni under 18'
    else:
        return 'Oya gathee!'
print(alchohol(21,50)) #place your variable ages and monies
