def u_data(name,age,city, country):
    result = '{}, {} год(а), проживает в городе {}, страна {}'.format(name,age,city, country)
    return result
name = input('Укажите имя ')
age = input ('Укажите возраст ')
city = input ('укажите город ')
country = 'Russia'
result = u_data(name,age,city, country)
print (result)





