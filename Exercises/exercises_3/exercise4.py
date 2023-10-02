times = int(input("How many values"))

sum = 0

for time in range(times):
    number = int(input(f"Insert the number {time+1}"))
    sum += number


average = sum / times

print(f"The whole sum is: {sum}")
print(f"The average is: {average}")
