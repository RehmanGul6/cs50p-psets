expression = input("Expression: ").split()

x,y,z = expression
x = float(x)
z = float(z)

if y == "+":
    print (f"{x+z:.1f}")
elif y =="-":
    print (f"{x-z:.1f}")
elif y =="*":
    print (f"{x*z:.1f}")
elif y =="/":
    print (f"{x/z:.1f}")

else : 
    print("unknow operator!!!!!")