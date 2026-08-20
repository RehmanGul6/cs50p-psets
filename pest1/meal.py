def main():
    time = input("what time is it ? ").split(":")
    converted_time = convert(time )
    if 7 <= converted_time <= 8:
        print("breakFast time ")
    elif 12 <= converted_time <= 13 :
        print("lunch time ")
    elif 18 <= converted_time <= 19 :
        print("dinner time ")        

def convert(time):
    hours , mins = time
    hours = float(hours)
    mins = float(mins) /60
    return mins + hours 

    



main()