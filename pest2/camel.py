camelcase = input("camelCase: ")
for snake_case in camelcase :
    if snake_case.isupper() == True :
        snake_case =  "_" + snake_case.lower()
    print(snake_case,end="")        
