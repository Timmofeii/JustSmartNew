from tkinter import *
from random import  choice
# import numpy as np
# import matplotlib.pyplot as plt
# import turtle
# from PIL import Image
# import noise


def simple1():
    x = np.linspace(-2, 2, 400)
    y = x ** 2
    plt.plot(x, y, label="y = x^2")
    plt.legend()
    plt.grid()
    plt.show()


def mandelbrot(c, max_iter=100):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def simple2():
    width, height = 800, 800
    xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            img[j, i] = mandelbrot(complex(x[i], y[j]))
    plt.imshow(img, cmap='inferno', extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.show()


def draw_tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(branch_len - 15, t)
        t.left(40)
        draw_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


def simple3():
    t = turtle.Turtle()
    t.left(90)
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    draw_tree(100, t)
    turtle.done()


def simple4():
    width, height = 512, 512
    scale = 50.0
    image = Image.new("L", (width, height))
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            value = noise.pnoise2(x / scale, y / scale, octaves=6)
            pixels[x, y] = int((value + 1) * 127.5)
    image.show()


# simple4()
def simple5():
        t = np.linspace(0, 2 * np.pi, 1000)
        a, b = 3, 2
        x = np.sin(a * t)
        y = np.sin(b * t)
        plt.plot(x, y)
        plt.axis("equal")
        plt.grid()
        plt.show()


# simple5()

# 1. Вітальне вікно
#
# Створи просту програму на Tkinter, яка запитує твоє ім'я через віджет Entry.
#
# Додай кнопку з текстом "Привітатись".
#
# Коли натиснеш кнопку, програма повинна показувати привітання у Label, наприклад, "Привіт, [ім'я]!".
#
# Вимоги
#
#  Використай основні віджети: Entry, Button, Label.
#
#  Зроби так, щоб привітання змінювалося залежно від того, яке ім'я ти введеш.

def first():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    entry = Entry(frame)
    entry.pack()
    label = Label(frame)
    label.pack()
    button = Button(frame, text="Enter your name: !", command=lambda: label.config(text=f"Hi, {entry.get()}"))
    button.pack()

    root.mainloop()
def first():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    entry = Entry(frame)
    entry.pack()
    label = Label(frame)
    label.pack()
    button = Button(frame, text="Enter your name: !", command=lambda: label.config(text=f"Hi, {entry.get()}"))
    button.pack()

    root.mainloop()
def first():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    entry = Entry(frame)
    entry.pack()
    label = Label(frame)
    label.pack()
    button = Button(frame, text="Enter your name: !", command=lambda: label.config(text=f"Hi, {entry.get()}"))
    button.pack()

    root.mainloop()


# first()
#
# 2. Випадкова зміна кольору
#
# Напиши програму на Tkinter, яка змінює колір фону вікна на випадковий колір, коли натискаєш кнопку.
#
# Створи список кольорів та використай модуль random, щоб обирати випадкові кольори зі списку.
#
# Скористайся методом root.config(bg='колір') для зміни кольору фону вікна.
#
# Вимоги
#
#  Додай кнопку Button з текстом "Магія (змінити колір)".
#
#  Створи Label з інструкцією, наприклад, "Натисни кнопку, щоб змінити колір фону!".
def second():
    colors = ["black",
              "red",
              "blue",
              "gray"
              ]
    root = Tk()
    root.geometry("300x400")  # Задаем размер окна
    frame = Frame(root)
    frame.pack(fill='both',expand=True)
    random_color_button = Button(frame, text="click to change color ",
                                 command=lambda: frame.config(bg=choice(colors)))
    random_color_button.pack()
    root.mainloop()

# second()

def find_smallest_int(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if max < arr[i]:
            max= arr[i]
    return max
arr = [123,24145,214,24,-24242]
print(find_smallest_int(arr))


def get_grade(s1, s2, s3):
    avg = s1+s2+s3 / 3
    
    if avg < 60:
            return'F'
    elif avg < 70:
        return 'D'
    elif avg <80:
        return 'C'
    elif avg < 90:
        return"B"
    return "A"
    