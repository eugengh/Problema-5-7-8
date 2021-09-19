Zi = ["L", "Ma", "Mi", 'J', "Vi", "S", "D"]
v = [1500, 2500, 3500, 4000, 4500, 5000, 0]
print("venitul sapatamnal = ", sum(v))
print("media venitului zilnic = ", sum(v)//7)
n= max(v)
y = v.index(n)
print("Ziua in care s-a obtinut cel mai mare venit este", Zi[y])
b = min(v)
a = v.index(b)
print("Ziua cu venitul cel mai mic este ", Zi[a])