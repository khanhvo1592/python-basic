# Vòng lặp for qua một list
for i in [1, 2, 3, 4, 5]:
    print(i)

# Vòng lặp for qua một range
print("for...in")
for i in range(5):  # sẽ in từ 0 đến 4
    print(i)

# Vòng lặp while
print("while")
j = 5
while j > 0:
    print(j)
    j -= 1

for char in "Python":
    print(char)

my_dict = {"a": 1, "b": 2, "c": 3}
# Lặp qua keys
for k in my_dict:
    print(k)

# Lặp qua values
for v in my_dict.values():
    print(v)

# Lặp qua cả keys và values
for key, value in my_dict.items():
    print(key, value)
