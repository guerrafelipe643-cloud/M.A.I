import mai
mai = mai.MAI()
mai.create(10000000,50,2)
while True:
    ent = str(input("digite a entrada: "))
    mai.process_and_memorize(ent)
    mai.map()