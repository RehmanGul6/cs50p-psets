def main():
    plate = input("Plate: ")

    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    return is_length_valid(plate) and first_2_letters(plate) and no_punctuation(plate) and numbers_last(plate)
    
def is_length_valid(plate):
   return 2 <= len(plate) <= 6 

def first_2_letters(plate):
    return plate[0].isalpha() and plate[1].isalpha()

def no_punctuation(plate):
    return plate.isalnum()

                       
def numbers_last(plate):
    seen_digit = False
    for char in plate:
        if char.isdecimal():
            if seen_digit == False:
                if char == "0":
                    return False
                else:
                    seen_digit = True
            else:
                seen_digit = True
        else:
            if seen_digit == True:
                return False
    return True


    


main()