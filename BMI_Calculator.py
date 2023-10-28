weight=int(input("Enter your weight"))
height=float(input("Enter your height in meters"))
BMI=(weight/(height*height))
if BMI<18.5:
    print(f"your BMI is:{BMI}")
    print("You are Underweight")
elif BMI>18.5 and BMI<24.9:
    print(f"your BMI is:{BMI}")
    print("Your BMI is normal")
else:
    print(f"your BMI is:{BMI}")
    print("You are overweight")
