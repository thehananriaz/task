#q21

# print("number \t","sqaure \t" , "cube" )
# for i in range(0,5):
#     s = i*i
#     c = i*i*i
#     print( i , "\t" , s , "\t", c)


#q22 

# sum=0
# for n in range(1,31):
#     if n%2==0:
#         sum += n

# print(sum) 
    
# positive_count = 0
# negative_count = 0
# zero_count = 0


#q23

# while True:

#     num = float(input("Enter a number (enter 0 to stop): "))

#     if num == 0:
#         break
#     if num > 0:
#         positive_count += 1
#     elif num < 0:
#         negative_count += 1
#     else:
#         zero_count += 1

# print("ositive numbers:", positive_count)
# print("negative numbers:", negative_count)
# print("total zeros:", zero_count)


#q24

# decimal_number = int(input("Enter a decimal number: "))
# def decimal_to_binary(n):
#     if n == 0:
#         return '0'
#     binary = ''
#     while n > 0:
#         binary = str(n % 2) + binary
#         n //= 2
#     return binary



# binary_number = decimal_to_binary(decimal_number)
# print(f"The binary equivalent of {decimal_number} is: {binary_number}")


#q26

# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             print(i, j, k)


#q27

hours = int(input("Enter Your number of hours: "))
rate = int(input("Enter Your hourly rate: "))

if hours>40:
    extra = (hours - 40) * rate
    extra_rate = extra * 1.5
    salary = (40 * rate) + extra_rate
    print("salary with extra: ", salary)
else:
    salary = hours * rate 
    print("salary: ", salary)

