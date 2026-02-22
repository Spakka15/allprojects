from cripters import criptalettere1, criptalettere2, criptalettere3
from decripters import decripter1, decripter2, decripter3, get_decr_indx, deleteprefix
from usefulfuncs import puliscilista
import sqlite3
import time



def main():

    print("""
    Benvenuto nel cripter fenomenale di Spakka_14!
    Premi 0 per inserire le tue credenziali per accedere al database!
    Premi 1 per creare credenziali
    Premi 2 per uscire
     
""")
    
    try:

        decision = int(input())

        if decision == 0:
            login()
        elif decision == 1:
            create_user()
        elif decision == 2:
            pass
        else:
            print("Indice inserito non valido")

    except Exception as e:
        print(f"Si è verificato un errore: {e}")       



def login():
    username = input("Inserisci Username per accesso: ")
    password = input("Inserisci Password per accesso: ")

def create_user():

    inserire = []
    letters = []

    try: 
        with open("settings.dat", "a+") as f:
            userina = input("Inserisci username sicuro: ")
            for i in range(len(userina)):
                letters.append(userina[i])
            inserire = criptalettere1(letters)
            for i in range(len(inserire)):
                f.write(inserire[i])

            
            puliscilista(letters)
            puliscilista(inserire)

            while True:
                passerina = input("Inserisci password sicura: ")
                passerian2 = input("Inserisci nuovamente la password: ")

                if passerina == passerian2:
                    for i in range(len(passerian2)):
                        letters.append(passerian2[i])
                    inserire = criptalettere2(letters)
                    for i in range(len(inserire)):
                        f.write(inserire[i])
                    
                    puliscilista(letters)
                    puliscilista(inserire)
                    print("Credenziali salvate con successo")
                    break

                else:
                    print("Le due password non corrispondono, reinseriscile!")

    except Exception as e:
        print(f"Si è verificato un problema {e}")

    pass
    
def afetrlogin(user: str):

    while True:
        print(f"""
        Benvenuto {user}!
        Scegli azione da effettuare:
        1) Visuallizza credenzili accesso
        2) Crea nuove credenziali d'accesso
        3) Modifica credenziali d'accesso
        4) Elimina credenziale d'accesso
        5) esci
        """)

        scelta = int(input())

        if scelta == 1:
            visualizza()
        elif scelta == 2:
            crea()
        elif scelta == 3:
            modifica()
        elif scelta == 4:
            delete()
        elif scelta == 5:
            break
        else:
            print("Numero inserito non valido")

def visualizza():
    pass

def crea():
    pass

def modifica():
    pass

def delete():
    pass


def cripta(string:str):
    start= time.time()


if __name__ == "__main__":
    main()