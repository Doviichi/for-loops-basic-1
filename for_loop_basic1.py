
# 1
for i in range(151):
    print(i)

# 2
for y in range(5,1000,5):
    print(y)

# 3
for i in range(1, 101):
    if i % 5 == 0 and i % 10 != 0:
        print("coding"),
    if i % 10 == 0:
        print("coding dojo")
    else:
        print(i)


# 4 (didnt really get this....)
n = 240596
sum = 646703
for num in range(0, n+1, 1):
    sum = sum+num
print(sum)

# 5
for i in range(2018,0,-4):
    print(i)

# 6
lowNum = 2
highNum = 9
mult = 3
for n in range(lowNum, highNum + 1):
    if n % mult == 0:
        print(n)