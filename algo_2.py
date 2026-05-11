from queue import Queue
import random
from collections import deque

# Завдання 1
queue = Queue() #Cтворення черги


def generate_request():
    queue.put(random.randint(1, 100)) #генерує випадковий запит і додає його до черги
    
def process_request():
    if not queue.empty(): #перевіряє, чи черга не порожня
        request = queue.get() #отримує запит з черги
        print(f"Обробка запиту: {request}") #виводить оброблений запит
    else:
        print("Черга порожня. Немає запитів для обробки.") #повідомляє, що черга порожня
    
while True:
    action = input("Введіть 'g' для генерації запиту, 'p' для обробки запиту або 'q' для виходу: ")
    if action == 'g':
        generate_request()
    elif action == 'p':
        process_request()
    elif action == 'q':
        break
    else:
        print("Невірна команда. Спробуйте ще раз.")
 
 
        
# Завдання 2

def is_palindrome(s):
    # Підготовка рядка: малі літери і без пробілів
    s = s.lower().replace(" ", "")
    
    # Заповнення deque символами
    d = deque()
    for char in s:
        d.append(char)
    
    # Порівняння символів з обох кінців
    while len(d) > 1:
        left = d.popleft()  # забираємо зліва
        right = d.pop()     # забираємо справа
        if left != right:
            return False
    
    return True


# Тестування
test_words = [
    "radar",
    "hello",
    "А роза впала на лапу Азора",
    "Рacecar",
    "Python"
]

for word in test_words:
    result = is_palindrome(word)
    print(f"'{word}' — {'паліндром ✅' if result else 'не паліндром ❌'}")