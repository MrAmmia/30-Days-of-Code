def average():
    s = input("Enter Numbers separated by space ")
    numbers = [int (i) for i in s.split()]
    mean = sum(numbers)/len(numbers)
    print("The Average is ")
    return mean
print(average())
