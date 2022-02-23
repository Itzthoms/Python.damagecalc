# Listan som ni ska använda i programmet
todo = []

# Skapa funktioner för de olika menyvalen:


# I följande funktion ska ni kommentera koden och förklara vad programmet gör
def main():
    #Skriver ut menyvalen
    print("\n1. lägg till sak i listan")
    print("2. ta bort första saken i listan")
    print("3. se listan")
    print("4. redigera sak i listan")
    print("5. ta bort specifik sak i listan")
    print("6. byt ordning på saker i listan")
    print("7. avsluta programmet")

    #Läser in användarens menyval
    val = input("vilket val?\n")
    while val != "7":  # Kör om koden tills man väljer menyval: 7
        # Skriv if-satser för de olika menyvalen som kör funktionerna
        


        # Skriver ut menyvalen
        print("\n1. lägg till sak i listan")
        print("2. ta bort första saken i listan")
        print("3. se listan")
        print("4. redigera sak i listan")
        print("5. ta bort specifik sak i listan")
        print("6. byt ordning på saker i listan")
        print("7. avsluta programmet")
        
        # Läser in användarens menyval
        val = input("vilket val?\n")
    print("Programmet avslutas")

main()