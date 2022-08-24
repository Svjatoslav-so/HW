var1 = var2 = 5
print(var1)
print(var2)
print(id(var1), id(var2))
var1 += 1
print(var1)
print(var2)
print(id(var1), id(var2))

var500 = 500
var501 = 500
print(id(var500), id(var501))
a = -200 - 300
b = -500
print(id(a), id(b))

g = 500
print(id(g))
f = 6
print(id(f))
ia = 1
da = 1.1
db = 1.1
print(id(ia), id(da), id(db))
