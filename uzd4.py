def read_file_content(nosauk, paplašinājums):
    if paplašinājums == "txt":
        with open(nosauk) as fails:
            saturs = fails.read()
            print(saturs)
    elif paplašinājums == "csv":
        import csv
        with open(nosauk) as fails:
            reader = csv.reader(fails)
            for row in reader:
                print(row)
    elif paplašinājums == "json":
        import json
        with open(nosauk) as fails:
            saturs = json.load(fails)
            print(saturs)
    else:
        print("Nepareizs faila paplašinājums")

nosauk = input("Ievadīt faila nosaukumu")
paplašinājums = input("Ievadīt faila paplašinājumu (txt, csv, json)")
read_file_content(nosauk, paplašinājums)