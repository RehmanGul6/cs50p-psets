hello =  input("Greeting: ").strip().lower()

    
if hello.startswith("hello") :
    print ("$0") 

elif hello.startswith("h",0,10) : 
    print("$20")

else : 
    print("$100")