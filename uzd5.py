vards = input("Ievadiet vārdu")

with open("lietotajs.txt") as fails:
    fails.write(vards)