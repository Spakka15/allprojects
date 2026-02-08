import random
import sqlite3


password = "abcdefg"

CONST_PATH = "dates.dat"

def criptalettere1(passw: str):
    numbers = []
    lenght = len(passw)

    for i in range(lenght):
        if passw[i] == 'a':
            numbers.append(random.randint(1, 5))
            numbers.append("|")
        if passw[i] == 'b' :
            numbers.append(random.randint(1, 5))
            numbers.append("!")
        if passw[i] == 'c' :
            numbers.append(random.randint(1, 5))
            numbers.append("ì")
        if passw[i] == 'd' :
            numbers.append(random.randint(1, 5))
            numbers.append("(")
        if passw[i] == 'e' :
            numbers.append(random.randint(1, 5))
            numbers.append("%")
        if passw[i] == 'f':
            numbers.append(random.randint(1, 5))
            numbers.append("£")
        if passw[i] == 'g':
            numbers.append(random.randint(1, 5))
            numbers.append("$")
        if passw[i] == 'h':
            numbers.append(random.randint(1, 5))
            numbers.append("{")
        if passw[i] == 'i':
            numbers.append(random.randint(1, 5))
            numbers.append("}")
        if passw[i] == 'j':
            numbers.append(random.randint(1, 5))
            numbers.append("*")
        if passw[i] == 'k':
            numbers.append(random.randint(1, 5))
            numbers.append("#")
        if passw[i] == 'l':
            numbers.append(random.randint(6, 9))
            numbers.append("#")
        if passw[i] == 'm':
            numbers.append(random.randint(6, 9))
            numbers.append("*")
        if passw[i] == 'n':
            numbers.append(random.randint(6, 9))
            numbers.append("}")
        if passw[i] == 'o':
            numbers.append(random.randint(6, 9))
            numbers.append("{")
        if passw[i] == 'p':
            numbers.append(random.randint(6, 9))
            numbers.append("$")
        if passw[i] == 'q' :
            numbers.append(random.randint(6, 9))
            numbers.append("£")
        if passw[i] == 'r':
            numbers.append(random.randint(6, 9))
            numbers.append("%")
        if passw[i] == 's' :
            numbers.append(random.randint(6, 9))
            numbers.append("(")
        if passw[i] == 't' :
            numbers.append(random.randint(6, 9))
            numbers.append("(")
        if passw[i] == 'u' :
            numbers.append(random.randint(6, 9))
            numbers.append("ì")
        if passw[i] == 'v' :
            numbers.append(random.randint(6, 9))
            numbers.append("!")
        if passw[i] == 'w' :
            numbers.append(random.randint(6, 9))
            numbers.append("|")
        if passw[i] == 'x' :
            numbers.append(random.randint(6, 9))
            numbers.append("ç")
        if passw[i] == 'y' :
            numbers.append(random.randint(6, 9))
            numbers.append("°")
        if passw[i] == 'z' :
            numbers.append(random.randint(6, 9))
            numbers.append("^")



    with open(CONST_PATH, "a") as f:

        f.write("fff__!")

        for i in range(2*lenght):

            if i == ((2*lenght)/2):
                choose = random.randint(0,1)

                if choose == 0:
                    f.write("?")
                
                else:
                    f.write("@")

            else:
                if  isinstance(numbers[i], str):
                    f.write(str(numbers[i]))
                    if random.randint(0, 50) <= 25:
                        f.write("&")
                    else:
                        f.write("/")
                else:
                    f.write(str(numbers[i]))
            
        f.write("\n")
        f.close()
        return

def criptalettere2(passw : str):
    numbers = []
    lenght = len(passw)

    for i in range(lenght):
        if passw[i] == 'a' or passw[i] == 'A':
            numbers.append(random.randint(1, 5))
            numbers.append("^")
        if passw[i] == 'b' or passw[i] == 'B':
            numbers.append(random.randint(1, 5))
            numbers.append(")")
        if passw[i] == 'c' or passw[i] == 'C':
            numbers.append(random.randint(1, 5))
            numbers.append("|")
        if passw[i] == 'd' or passw[i] == 'D':
            numbers.append(random.randint(1, 5))
            numbers.append("'")
        if passw[i] == 'e' or passw[i] == 'E':
            numbers.append(random.randint(1, 5))
            numbers.append("£")
        if passw[i] == 'f' or passw[i] == 'F':
            numbers.append(random.randint(1, 5))
            numbers.append("%")
        if passw[i] == 'g' or passw[i] == 'G':
            numbers.append(random.randint(1, 5))
            numbers.append("*")
        if passw[i] == 'h' or passw[i] == 'H':
            numbers.append(random.randint(1, 5))
            numbers.append("]")
        if passw[i] == 'i' or passw[i] == 'I':
            numbers.append(random.randint(1, 5))
            numbers.append("[")
        if passw[i] == 'j' or passw[i] == 'J':
            numbers.append(random.randint(1, 5))
            numbers.append("#")
        if passw[i] == 'k' or passw[i] == 'K':
            numbers.append(random.randint(1, 5))
            numbers.append("à")
        if passw[i] == 'l' or passw[i] == 'L':
            numbers.append(random.randint(6, 9))
            numbers.append("à")
        if passw[i] == 'm' or passw[i] == 'M':
            numbers.append(random.randint(6, 9))
            numbers.append("#")
        if passw[i] == 'n' or passw[i] == 'N':
            numbers.append(random.randint(6, 9))
            numbers.append("[")
        if passw[i] == 'o' or passw[i] == 'O':
            numbers.append(random.randint(6, 9))
            numbers.append("]")
        if passw[i] == 'p' or passw[i] == 'P':
            numbers.append(random.randint(6, 9))
            numbers.append("*")
        if passw[i] == 'q' or passw[i] == 'Q':
            numbers.append(random.randint(6, 9))
            numbers.append("%")
        if passw[i] == 'r' or passw[i] == 'R':
            numbers.append(random.randint(6, 9))
            numbers.append("£")
        if passw[i] == 's' or passw[i] == 'S':
            numbers.append(random.randint(6, 9))
            numbers.append("'")
        if passw[i] == 't' or passw[i] == 'T':
            numbers.append(random.randint(6, 9))
            numbers.append("|")
        if passw[i] == 'u' or passw[i] == 'U':
            numbers.append(random.randint(6, 9))
            numbers.append(")")
        if passw[i] == 'v' or passw[i] == 'V':
            numbers.append(random.randint(6, 9))
            numbers.append("^")
        if passw[i] == 'w' or passw[i] == 'W':
            numbers.append(random.randint(6, 9))
            numbers.append("<")
        if passw[i] == 'x' or passw[i] == 'X':
            numbers.append(random.randint(6, 9))
            numbers.append(">")
        if passw[i] == 'y' or passw[i] == 'Y':
            numbers.append(random.randint(6, 9))
            numbers.append("°")
        if passw[i] == 'z' or passw[i] == 'Z':
            numbers.append(random.randint(6, 9))
            numbers.append("=")

    with open(CONST_PATH, "a") as f:

        f.writelines(1, "ciao")

        f.write("BBB-_/")

        for i in range(2*lenght):

            if i == ((2*lenght)/2):
                choose = random.randint(0,1)

                if choose == 0:
                    f.write("?")
                
                else:
                    f.write("@")

            else:
                if  isinstance(numbers[i], str):
                    f.write(str(numbers[i]))
                    if random.randint(0, 50) <= 25:
                        f.write("*")
                    else:
                        f.write("+")
                else:
                    f.write(str(numbers[i]))
            
        f.write("\n")

        f.close()
        return

def indirizza():
    print()


def countlines():

    with open(CONST_PATH, "r") as f:
        pass



#criptalettere1(password)
#criptalettere2(password)
countlines()