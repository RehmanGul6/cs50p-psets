# happy to emoji 
# sad  to emoji 
#take input 

def main():
    user_input = input()
    print(convert(user_input))

def convert(user_input):
    converted = user_input.replace(":(" , "🙁").replace(":)" , "🙂")    
    return converted

main()   