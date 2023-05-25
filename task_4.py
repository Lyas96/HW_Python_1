# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите количество долек по горизонтали: "))
m = int(input("Введите количество долек по вертикали: "))
k = int(input("Введите число долек которые необходимо отломить: "))
b = n * m
if k != 1:
  if b % k == 0 or b % k == n or b % k == m:
    print("YES")
  else:
    print("NO")
elif n == 1 or m == 1:
  print("YES")
else:
  print("NO")
