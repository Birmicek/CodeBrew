def range_divisible():
    start = int(input("Enter a start number: "))
    stop = int(input("Enter an end number: "))
    divisor = int(input("Enter a divisor: "))

    if start >= stop:
        print("The start number can not be bigger or equal to end number!")
    elif divisor == 0:
        print("Cannot divide by zero")
        return
    
    initial_range = list(range(start,stop + 1))
    final_range = []
    #print(initial_range)
    for i in initial_range:
        if i % divisor == 0:
            final_range.append(i)
    print(f"Numbers in range ({start},{stop}) divisible by {divisor}:")
    print(final_range)     

range_divisible()