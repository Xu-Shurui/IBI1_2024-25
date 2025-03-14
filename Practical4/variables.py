a=15
b=75
c=a+b
d=90
e=5
f=d+e
if c<f:
    print("Taking the bus is quicker")
else:
    print("Driving is quicker")
#Taking the bus is quicker
X = True
Y = False
W = X and Y

print(f"Initial values: X={X}, Y={Y} => W={W}")


print("\nTruth table for W (X and Y):")

for X in [True, False]:
    for Y in [True, False]:
        W = X and Y
        print(f"X: {X}, Y: {Y} => W: {W}")