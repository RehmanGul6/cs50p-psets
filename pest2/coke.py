amount_due = 50 

while(True):
    print("Amount Due: ", amount_due)
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin == 25 or inserted_coin == 10 or inserted_coin == 5 :
        amount_due -= inserted_coin
    if (amount_due == 0 ):
        break
    elif amount_due < 0:
        amount_due = abs(amount_due)
        break   
print("Change owned: " , amount_due )    