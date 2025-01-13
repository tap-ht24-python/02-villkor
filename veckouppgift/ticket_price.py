# Uppgift 2
ticket_price = 100  # biljettpris
money_on_hand = 200  # pengar på fickan
money_left = money_on_hand - ticket_price

#print("Det blir", (y - x), "kronor över.")
#print("Det blir " + str(money_on_hand - ticket_price) + " kronor över.")
print("Det blir " + str(money_left) + " kronor över.")



# operator precedence - division räknas ut före subtraktion
#half_of_money_left = (money_on_hand - ticket_price) / 2
half_of_money_left = money_left / 2
print("Hälften är: " + str(half_of_money_left))
#print("Hälften är: ", z)


# Bra variabelnamn:
# - uttrycksfulla (beskriver vad de är till för)
# - inga förkortningar
# - lagom långa
# - använd engelska konsekvent
