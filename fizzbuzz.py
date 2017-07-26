x=0
i=1
for i in range(101):
    if int(i)%3==0 and int(i)%5==0:
        print("fizzbuzz")
    elif int(i)%3==0:
        print("fizz")
    elif int(i)%5==0:
        print("buzz")
    else:
        print(i)
