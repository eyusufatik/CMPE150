def hw2():
    str_input = input()
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    str_input = str_input.strip()
    words = str_input.split()
    count = len(words)

    if count == 0:
        print("No words")
    elif count == 1:
        print(f"One word\n{words[0]}")
    elif count == 2:
        print(f"Two words\n{words[0]} {words[1]}")
    else:
        print(f"{count} words!\n{words[0]} {words[count-1]}")
    
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    return


if __name__ == "__main__":
    hw2()
