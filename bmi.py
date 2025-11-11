import sys
if len(sys.argv)==3:
  w = int(sys.argv[1])
  h = float(sys.argv[2])

else:
  w = 40
  h = 1.5


bmi = w/ (h*h)

print("The BMI value is : " , bmi)
