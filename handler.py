# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import mariadb
import sys
import smtplib
import main


def login(email, password, signal):
    try:
        connection = mariadb.connect(
            user="root",
            password="lovepy",
            host="localhost",
            port=3306,
            database="contacts")
        print("Подключен к MariaDB")
        cursor = connection.cursor()

        # Проверяем есть ли такой пользователь
        cursor.execute(f'SELECT * FROM contacts WHERE email="{email}";')
        value = cursor.fetchall()
        if value != [] and value[0][1] == password:
            print('Вы вошли в систему')
            main.work()
        else:
            signal.emit('Проверьте правильность ввода данных!')

        cursor.close()
        connection.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


def registration(email, password, signal):
    try:
        connection = mariadb.connect(
            user="root",
            password="lovepy",
            host="localhost",
            port=3306,
            database="contacts")
        print("Подключен к MariaDB")
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM contacts WHERE email="{email}";')
        value = cursor.fetchall()

        # Регистрируем пользователя
        if value != []:
            signal.emit('Такой email уже используется!')

        elif value == []:
            cursor.execute(f"INSERT INTO users (name, password) VALUES ('{email}', '{password}')")
            signal.emit('Вы успешно зарегистрированы!')
            connection.commit()

        cursor.close()
        connection.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


def e_mail():
    from_email = 'hoffman.design@mail.ru'
    e_pas = 'FBFu15kmtEr0EgCfW4pU'
    to_email = login.email
    with smtplib.SMTP_SSL('smtp.mail.ru', 465) as server:
        server.login(from_email, e_pas)
        server.sendmail(from_email, to_email, f"Your password: {login.password}")

def recover(email, password, signal):
    try:
        connection = mariadb.connect(
            user="root",
            password="lovepy",
            host="localhost",
            port=3306,
            database="contacts")
        print("Подключен к MariaDB")
        cursor = connection.cursor()

        # Проверяем есть ли такой пользователь
        cursor.execute(f'SELECT * FROM contacts WHERE email="{email}";')
        value = cursor.fetchall()
        if value != [] and value[0][2] == email:
            e_mail(email, password)
        else:
            signal.emit('Проверьте правильность ввода данных!')

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

