account_balance = 200
#greater_than_zero = account_balance > 0
#print(greater_than_zero)

if account_balance > 0:   # alternativ:  not (account_balance <= 0)
    # block i Python ska alltid vara indenterade
    print("Du har pengar på kontot: " + str(account_balance))
    if 10 < account_balance < 100:
        print("Du har vunnit en brödrost!")

print("Nu tar banken semester...")


#print(1 == 1)    # True, samma värde
#print(2.0 == 2)  # Olika datatyp, men omvandlas till samma värde -> True
#print("hej" == "HEJ")   # False, olika strängar
#print(2 < 2)     # False



