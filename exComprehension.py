#Lista SEM Comprehension
x = [1,2,3,4,5,6]
y = []

for i in x :
  y.append(i**2)

print(x)
print(y)

#Lista COM Comprehension
z = [i**2 for i in x]
print(x)
print(z)

#Lista COM Comprehension
w = [i for i in x if i%2 == 1]
print(w)