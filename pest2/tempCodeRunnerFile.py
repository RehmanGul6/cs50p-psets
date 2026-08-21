plate = "ab1234"                             
def numbers_last(plate):
    check = 2
    for check in range (6):
        if plate[check].isdecimal():
            print("yes")