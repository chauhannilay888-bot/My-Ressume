# BMI Calculator
def BMI_calculator(weight, height):
    BMI = weight / height**2
    return BMI
input1 = BMI_calculator(40, 1.4)
input2 = BMI_calculator(50, 2)
input3 = BMI_calculator(200, 12) 

print(f"{input1}") 
print(f"{input2}")
print(f"{input3}")
