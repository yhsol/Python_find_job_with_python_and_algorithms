def al_hanoi(n, start, middle, end):
    if n == 1:
        print(start, "->", end)
        return "end"

    al_hanoi(n-1, start, end, middle)
    print(start, "->", end)
    al_hanoi(n-1, middle, start, end)
