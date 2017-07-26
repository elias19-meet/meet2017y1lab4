speed=int(input('enter the speed '))
bday=input('is it your birthday')
if bday=='yes':
    speed =speed-5
if speed<31:
    print("no ticket")
elif speed>30 and speed<51:
    print("small ticket")
elif speed>50:
    print("big ticket ")
