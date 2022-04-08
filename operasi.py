from operation import *

a = 10
b = 7
print(a, ' + ', b, ' = ', tambah(a,b))
print(a, ' - ', b, ' = ', kurang(a,b))
print(a, ' * ', b, ' = ', kali(a,b))
print(a, ' / ', b, ' = ', bagi(a,b))

print("2 + 4 * 6 - 4 = ", kurang(tambah(2,(kali(4,6))),4))
print("(4 + 7) * (6 - 9) = ", kali(tambah(4,7),kurang(6,9)))
print("(10 + 2) / (7 + 5) / (12-34) = ", bagi(bagi(tambah(10, 2), tambah(7, 5)), kurang(12, 34)))
