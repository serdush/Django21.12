"""
Управляющие конструкции:
* if else elif ... -- условный оператор
* while / for --- цикл
* def kek() .... --- функция
"""

# Le Question 1
if None:
    print("It works!") 

# Le Question 2
c = 20
for i in range(0, c, 1):
    print(i)
    c += i

# Le Question 3
print("==============================")
a = 1 
def foo():
    a += 1 # Нельзя изменять значения переменных определенных в выше стоящих областях видимости
    print(a) # Поскольку переменная a определена в более высокой области видимости - мы можем из нее прочитать

foo()