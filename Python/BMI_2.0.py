weight=float(input("Enter your weight in kg : "))
height=float(input("Enter your height in m : "))
bmi=weight/(height**2)
result=round(bmi)
if result<=18.5:
    print(f"Your BMI is {result}, You are underweight")
elif result>18.5 and result<25:
    print(f"Your BMI is {result}, You have a Normal wieght")
elif result>25 and result<30:
    print(f"Your BMI is {result}, You are slightly overweight")
elif result>30 and result<35:
    print(f"Your BMI is {result}, You are obese")
else:
    print(f"Your BMI is {result}, You are clinically obese")