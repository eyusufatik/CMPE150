def hw3():
    cumulative_sum = 0
    n = int(input())
    x = int(input())
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    inputs = []

    for i in range(x):
        inputs.append(int(input()))
    
    for i in range(1,n+1):
        s=0
        for j in range(x-1, x-1-i, -1):
            temp = j
            if j<0:
                j = j % x
            s += inputs[j] * 10**(x-temp-1)
            j = temp
        cumulative_sum += s

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    print(cumulative_sum)
    return cumulative_sum


if __name__ == "__main__":
    hw3()

