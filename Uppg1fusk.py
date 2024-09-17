tal = []
import statistics
notal = int(input("Hur många tal vill du mata in?: "))
i = 1
while i <= notal:
    tal.append(int(input(f"tal {i}:")))
    i += 1
tal.sort()
print(f"medel: {statistics.mean(tal)}")
print(f"median: {statistics.median(tal)}")
print(f"min: {tal[0]}")
print(f"max: {tal[notal-1]}")
print(f"summa: {sum(tal)}")

