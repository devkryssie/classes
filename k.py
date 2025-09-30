def find_max(**numbers):
    large = numbers[0]
    for num in numbers:
       if num > large:
           large = num
    return large
print(find_max(2,3,5,10))
 
