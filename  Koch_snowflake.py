import turtle

# рекурсивна функція для лінії Коха
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)


# функція для сніжинки
def draw_snowflake(order, size):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    for _ in range(3):  # 3 сторони трикутника
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


#  запуск програми 
level = int(input("Введіть рівень рекурсії (0-6 рекомендується): "))
draw_snowflake(level, 300)