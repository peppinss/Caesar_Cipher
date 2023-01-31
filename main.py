# Write your code below this line 👇
def prime_checker(number):
    y = 0
    if str(number) in primenumber:
        print("It's a prime number.")
    else:
        for x in range(2,10):
            if number % x != 0:
                y += 1
                print(y)
            else:
                print(y)
                continue
        if y == 8:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")

primenumber = "1", "2", "3", "5", "7"
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)