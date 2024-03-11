height = int(input("Your height in cm: "))
weight = int(input("Your weight in kg: "))
bmi=(weight/height**2)*10000
print("Your Bmi is %02.2d"%(bmi))

if bmi<18.5 : 
    print("You are underweight")
elif bmi<=24.9: 
    print("You are normal")
elif bmi<=29.9 : 
    print("You are overweight")
elif bmi<=34.9 : 
    print("You are obese")
else:
    print("You are extremly obese")


    