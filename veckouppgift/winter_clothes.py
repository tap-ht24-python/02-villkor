# 1a Använd input för att be användaren om ett heltal. Spara värdet i en
# variabel. Omvandla variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt.
# Kodexempel med input:
# x = input("Fråga här")

x = input("Ge mig ett tal, tack: ")
x = int(x)

# 1b Fråga användaren efter ett annat heltal. Skriv ut summan av talen, alltså tal1 + tal2.
# Testa genom att hitta på två tal och räkna ut summan i huvudet. Kontrollera om programmet räknar rätt.
y = input("Ge mig ett tal till: ")
y = int(y)
sum = x + y
print(sum)

# 2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor. Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala.
# 2b Gör om programmet så att användaren kan skriva in en procentsats.
# Testa genom att hitta på en procentsats och räkna ut vad programmet ska
# svara med, innan du kör det. Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.

jacket_price = 2000
jacket_discount = float(input("Hur många procent rabatt är det på jackan? "))

final_price = jacket_price * (100 - jacket_discount) / 100
print("Du ska betala " + str(final_price) + " för jackan.")
