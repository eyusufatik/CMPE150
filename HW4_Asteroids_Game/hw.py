
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
row_num = x + g + 1
col_num = y

asteroid_num = x*y
asteroids_destroyed = 0

frame = []

time = 0

ship_row = 0
ship_col = 0

fire_row = -1 #-1 means there is no laser in the frame
fire_col = -1
fire_mode = False

command = ""
exit_with_command = False

win_condition = False
game_over_condition = False

#creating the first frame
for i in range(row_num):
    frame.append([])
    for j in range(col_num):
        if i < x:
            frame[i].append("*")
        elif i < x + g:
            frame[i].append(" ")
        else:
            if j == (y - 1) // 2:
                frame[i].append("@")
                ship_row = i
                ship_col = j
            else:
                frame[i].append(" ")



while command != "exit":
    if game_over_condition:
        print("GAME OVER")
        command = "exit"
    if asteroids_destroyed == asteroid_num:
        print("YOU WON!")
        win_condition = True
        command = "exit"

    for row in frame:
        for col in row:
            print(col, end="")
        print()

    for i in range(72):
        print("-", end="")
    print()

    if not fire_mode and not win_condition and not game_over_condition:
        try:
            command = input("Choose your action!\n")
            command = command.lower()
            if command == "exit":
                exit_with_command = True
        except EOFError:
            command = "exit"


    if command == "left" and not fire_mode:
        if ship_col!=0:
            frame[ship_row][ship_col] = " "
            frame[ship_row][ship_col-1] = "@"
            ship_col-=1
    elif command == "right" and not fire_mode:
        if ship_col!= col_num-1:
            frame[ship_row][ship_col] = " "
            frame[ship_row][ship_col+1] = "@"
            ship_col += 1
    elif command == "fire":
        if fire_row == -1 and fire_col == -1:
            fire_mode = True
            if frame[ship_row-1][ship_col] == " ":
                frame[ship_row-1][ship_col] = "|"
                fire_row = ship_row-1
                fire_col = ship_col
            elif frame[ship_row-1][ship_col] == "*":
                frame[ship_row - 1][ship_col] = " "
                asteroids_destroyed += 1
                fire_mode = False
                fire_row = -1
                fire_col = -1
        else:
            if fire_row != 0:
                frame[fire_row][fire_col] = " "
                if frame[fire_row - 1][fire_col] == " ":
                    frame[fire_row-1][fire_col] = "|"
                    fire_row -= 1
                elif frame[fire_row-1][fire_col] == "*":
                    frame[fire_row - 1][fire_col] = " "
                    asteroids_destroyed += 1
                    fire_mode = False
                    fire_row = -1
                    fire_col = -1
            else:
                frame[0][fire_col] = " "
                fire_row = -1
                fire_col = -1
                fire_mode = False
                command ="sad"

    if not fire_mode and not win_condition and not game_over_condition and not exit_with_command:
        time += 1
        #print(time)
        if time % 5 ==0:
            if "*" in frame[ship_row-1]:
                game_over_condition = True
            else:
                frame[ship_row][ship_col] = " "
                frame[ship_row-1][ship_col] = "@"
                frame.pop()
                frame.insert(0,[" "]*col_num)


if exit_with_command:
    for row in frame:
        for col in row:
            print(col, end="")
        print()

    for i in range(72):
        print("-", end="")
    print()

print("YOUR SCORE: " + str(asteroids_destroyed))
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
