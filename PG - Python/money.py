#Här är värdena som ska jämföras
money = input("Skiv in värde här:")
money = int(money)
own = 100
decrease = 30

otherwise = 90
lessen = 15

#Om värdet är mer än hundra, subtraherar man med 30.
if money >= 100:
    money = money - decrease
    print(money)

#Om värdet är mer än 90, subtraherar man med 15
elif money >= 90:
    money = money - lessen
    print(money)

#Här skriver man in money's värde multiplicerat med multi's värde.
else:
    multi = input("Prova igen:")
    multi = int(multi)
    money = money * multi
    print(money)