queue = []
name = input("Skriv in ditt namn: ")
queue.append(name)
#queue = ["tomas, "johan"]
print(queue)
helping = queue.pop(0)
print(helping)

name1 = input("Lägg till yttligare ett namn: ")
name2 = input("Lägg till ett sista namn: ")
queue.append(name1)
queue.append(name2)

for x in queue:
     print(x)

queue.remove(name2)

for x in queue:
     print(x)