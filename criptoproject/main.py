from cripters import criptalettere1, criptalettere2, criptalettere3
from decripters import decripter1, decripter2, decripter3, get_decr_indx, deleteprefix



def creatutto():
    print("""
    Benvenuto nel cripter fenomenale di Spakka_14!
    Per iniziare inserisci le tue credenziali per accedere al database!
     
""")
    
def afetrlogin(user: str):
    print(f"""
    Benvenuto {user}!
    Scegli azione da effettuare:
    1) Visuallizza credenzili accesso
    2) Crea nuove credenziali d'accesso
    3) Modifica credenziali d'accesso
    4) Elimina credenziale d'accesso
    5) esci
    """)


