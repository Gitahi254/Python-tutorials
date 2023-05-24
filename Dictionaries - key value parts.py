drinks = {'Konyagi': 350, 'Best Gin': 300, 'Heiniken': 250} #drink is the key, price is the value.
employees = {'Finance':['Allan', 'Kimani','Gitahi'], 'IT':['Mark', 'Lorainne', 'Luigi', 'Chrispin'], 'HR':['Lucy', 'Jane', 'Grace']}
print(employees)

employees['Legal'] = ['Mr.Koskei'] #adds new value pair
print(employees)

employees.update({'Sales': ['Andie', 'Adamu']}) #adds new key value pair
print(employees)

drinks['Konyagi'] = 500
print(drinks)

print(drinks.get('Konyagi'))