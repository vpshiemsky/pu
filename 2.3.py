#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def info(*args):
    return f'Ваше имя-{args[0]},фамилия-{args[1]},год рождения-{args[2]},город проживания-{args[3]},email-{args[4]},телефон-{args[5]}'
print(info(input('Ваше имя '),input('Фамилия ' ),input('Год рождения '),input('Город проживания '),input('email '),input('Телефон ')))