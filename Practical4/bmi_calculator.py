weight = float(input("please enter your weight(kg)："))#input weight
height = float(input("please enter your height(m)："))#input height
bmi = weight / (height ** 2)#calculate bmi
#determine the category of bmi
if bmi < 18.5:#if bmi is less than 18.5, it is underweight
    category = "underweight"#category is underweight
elif 18.5 <= bmi < 30:
    category = "normal weight"#category is normal weight
else:
    category = "obese"#category is obese

print(f"BMI: {bmi:.2f}, your bmi category is ：{category}")#output bmi and category