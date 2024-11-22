from os.path import split

napis = str("Imie Nazwisko")

def wyodrebnianie(x):

    jeden = napis.split()[0]
    dwa = napis.split()[1]
    print(jeden)
    print(dwa)

    nazwiskoImie = napis.split()[1] + " " + napis.split()[0]
    print(nazwiskoImie)

    print(dwa[0]+jeden[0])


    print(
        jeden[0] + dwa[1:len(dwa)],
        dwa[0] + jeden[1:len(jeden)]
    )




wyodrebnianie(napis)