def u_data(name,age,city):
    result = '{}, {} год(а), проживает в городе {}'.format(name,age,city)
    return result
name = input('Укажите имя ')
age = input ('Укажите возраст ')
city = input ('укажите город ')
result = u_data(name,age,city)
print (result)




