# Listan som ni ska använda i programmet
todo = []



# Skapa funktioner för de olika menyvalen:
def insert(alist):
  inp = input("Lägg till värde?")
  alist.append(inp)



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
    if val == "1":
        print("Lägg till en sak i listan")
    elif val == "2":
        print="ta bort första saken i listan"
    elif val == "3":
        print(3)
    while val != "7":  # Kör om koden tills man väljer menyval: 7
        # Skriv if-satser för de olika menyvalen som kör funktionerna



        # Skriver ut menyvalen
        print("\n1. lägg till sak i listan")
        insert(todo)
        print("2. ta bort första saken i listan")
        print("3. se listan")
        print("4. redigera sak i listan")
        print("5. ta bort specifik sak i listan")
        print("6. byt ordning på saker i listan")
        print("7. avsluta programmet")
        
        # Läser in användarens menyval
        if val == todo:
            insert(todo)
    print("Programmet avslutas")

main()