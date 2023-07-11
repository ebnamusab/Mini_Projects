print("This is a BMI calculator \n")
name = input("Enter Your Name : ")
weight = float(input("Enter your weight : "))
height = float(input("Enter your height (meter): "))

bmi = weight / ( height ** 2 )

if bmi < 25:
    print(f"{name} is underweight by {bmi} BMI")
else:
    print(f"{name} is overweight by {bmi} BMI")