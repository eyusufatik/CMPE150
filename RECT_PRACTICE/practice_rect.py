string = input()
ints = string.split()
w1 = int(ints[0])
h1 = int(ints[1])
w2 = int(ints[2])
h2 = int(ints[3])

if w2*h2 > w1*h1:
    temp = w1
    w1 = w2
    w2 = temp

    temp = h1
    h1 = h2
    h2 = temp

rects = []

for i in range(h1):
    rects.append([])
    for j in range(w1):
        rects[i].append("x")

start_row = int(h1/2 - h2/2)
start_column = int(w1/2 - w2/2)

for i in range(start_row,start_row+h2):
    for j in range(start_column, start_column + w2):
        rects[i][j] = " "


for i in range(h1):
    for j in range(w1):
        print(rects[i][j], end = "")
    print()