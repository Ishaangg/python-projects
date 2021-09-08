num = int(input("Enter numbers between 0 and 1000: "))

last_number = num % 10

num1 = num // 10

middle_number = num1 % 10

num2 = num1 // 10

first_number = num2 % 10

new_num = last_number + middle_number + first_number 

print("the sum of numbers are", new_num)


