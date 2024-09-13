tal = []
notal = int(input("Hur många tal vill du mata in?: "))
i = 1
while i <= notal:
    tal.append(int(input(f"tal {i}:")))
    i += 1
tal.sort()
summa = sum(tal)
medel = sum(tal)/len(tal)
print(f"summa: {summa}")
print(f"medel: {medel}")
print(f"min: {tal[0]}")
print(f"max: {tal[notal-1]}")
if len(tal)%2 ==1:
    print(f"median: {tal[len(tal)//2]}")
else:
    print(f"median: {float(tal[(len(tal)//2)]+tal[((len(tal)//2)-1)])/2}")

