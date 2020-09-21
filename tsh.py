#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def call(command):
    print(os.popen(command).read())

known_commands = []
def read_line(expected, error_message="что-то не то"):
    while True:
        val = raw_input("$")
        if val == expected:
            known_commands.append(expected)
            break
        elif val in known_commands:
            call(val)
        else:
            print(error_message)


print("Тут какой-то текст про man")
read_line("man")
print("Молодец, теперь ты всегда можешь посмотреть справку. выполни man man :D")
read_line("man man")
print("Молодец, в награду ты получаешь новую команду в свой арсенал заклинаний: ls, "
      "чтобы получить ее, напиши man ls")
read_line("man ls")
read_line("ls")
print("Отлично, теперь ты можешь смотреть по сторонам")
print("Но чтобы перемещаться, тебе нужен cd, возьми же его [man cd]")
read_line("man cd")
print("Отлично, теперь ты можешь ходить куда тебе вздумается")
print("Иди же отсюда")


