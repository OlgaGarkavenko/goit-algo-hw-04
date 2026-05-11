# Щоб порахувати факторіал потрібно написати цю рекурсію
def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1) 
print(factorial(9)) #9! == 362880


# Знаходження числа Фібоначчі за допомогою рекурсії
def fibonacci(n):
    if n ==1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7)) #7 це порядковий номер числа Фібоначчі
  

# Задача на поліндром
def palindrome(s):
    if len(s) <=1 :
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
print(palindrome("radar")) #True
    
     