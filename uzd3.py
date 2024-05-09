fails = open("file.txt")
saturs = fails.readlines()
for line in saturs:
    print(line[2:3])
fails.close()