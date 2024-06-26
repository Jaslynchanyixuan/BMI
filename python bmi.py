def bmi(weight,height):
    return round(weight/height**2,2)

name_list = []
bmi_list = []

name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

bmi = bmi(weight,height)

name_list.append(name)
bmi_list.append(bmi)

if bmi < 18.5 :
    print(name, "your bmi is", str(bmi), ". You are underweight. \n")
elif bmi >= 18.5 and bmi <= 24.9 :
    print(name, "your bmi is", str(bmi), ". Your are normal. \n")
elif bmi >= 25 and bmi <= 29.9:
    print(name, "your bmi is", str(bmi), ". You are Overweight. \n")
elif bmi >= 30 and bmi <= 34.9:
    print(name, "your bmi is", str(bmi), ". You are Obese Class I. \n")
elif bmi >= 35 and bmi <= 39.9:
    print(name, "your bmi is", str(bmi), ". You are Obese Class II. \n")
elif bmi >= 40 and bmi <= 49.9:
    print(name, "your bmi is", str(bmi), ". You are Morbid Obese. \n")
elif bmi >=50:
    print(name, "your bmi is", str(bmi), ". You are Obese Class III. \n")

print("The name", [name_list], 'have the respective BMI", [bmi_list])
