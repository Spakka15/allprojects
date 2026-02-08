import random



password = "abcdefg"

CONST_PATH = "dates.dat"

def criptalettere1(passw: str):
    numbers = []
    lenght = len(passw)

    for i in range(lenght):

        if passw[i] == 'a':
            if random.randint(1, 5) %2 == 0:
                numbers.append("|")
            else:               #bar vert e punto escl
                numbers.append("!")
        if passw[i] == 'b' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("£")
            else:               #pund e perc
                numbers.append("%")
        if passw[i] == 'c' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("^")
            else:               #pot e punto dom
                numbers.append("?")
        if passw[i] == 'd' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("+")
            else:               #piu e per
                numbers.append("*")
        if passw[i] == 'e' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("{")
            else:               #graffa ap quadra chius
                numbers.append("]")
        if passw[i] == 'f':
            if random.randint(1, 5) %2 == 0:
                numbers.append("}")
            else:               #graf chius quadra apt
                numbers.append("[")
        if passw[i] == 'g':
            if random.randint(1, 5) %2 == 0:
                numbers.append("(")
            else:               #quadara apt e dollaro
                numbers.append("$")
        if passw[i] == 'h':
            if random.randint(1, 5) %2 == 0:
                numbers.append("/")
            else:               #norm slash . e comm
                numbers.append("&")
        if passw[i] == 'i':
            if random.randint(1, 5) %2 == 0:
                numbers.append("ì")
            else:               #i acc e e acc
                numbers.append("è")
        if passw[i] == 'j':
            if random.randint(1, 5) %2 == 0:
                numbers.append(")")
            else:               #quadra chius e ugu
                numbers.append("=")
        if passw[i] == 'k':
            if random.randint(1, 5) %2 == 0:
                numbers.append("#")
            else:               #canc e chiocc
                numbers.append("@")
        if passw[i] == 'l':
            if random.randint(1, 5) %2 == 0:
                numbers.append("°")
            else:               #gradi virgola
                numbers.append(",")
        if passw[i] == 'm': #mezooooooooooooo
            if random.randint(1, 5) %2 == 0:
                numbers.append(":")
            else:               #du punt e punt
                numbers.append(".")
        if passw[i] == 'n':
            if random.randint(1, 5) %2 == 0:
                numbers.append(";")
            else:               #punt virgola e tratt 
                numbers.append("-")
        if passw[i] == 'o':
            if random.randint(1, 5) %2 == 0:
                numbers.append("_")
            else:               #tratt low u acc
                numbers.append("ù")
        if passw[i] == 'p':
            if random.randint(1, 5) %2 == 0:
                numbers.append("§")
            else:               #s strana e c rumena
                numbers.append("ç")
        if passw[i] == 'q' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("1")
            else:               #1 e 8
                numbers.append("8")
        if passw[i] == 'r':
            if random.randint(1, 5) %2 == 0:
                numbers.append("<")
            else:               #magg e minore
                numbers.append(">")
        if passw[i] == 's' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("7")
            else:               # 7 e  3
                numbers.append("3")
        if passw[i] == 't' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("6")
            else:               #5 e 6
                numbers.append("5")
        if passw[i] == 'u' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("Ñ")
            else:               #egne maiusc e minusc
                numbers.append("ñ")
        if passw[i] == 'v' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("ɛl")
            else:               #l norvegese
                numbers.append("ɛl")
        if passw[i] == 'w' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("kʉ")
            else:               #q norvegese
                numbers.append("kʉ")
        if passw[i] == 'x' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("æ")
            else:               #strana norvegese
                numbers.append("æ")
        if passw[i] == 'y' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("ø")
            else:               #o norvegese
                numbers.append("ø")
        if passw[i] == 'z' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("å")
            else:               #a norvegese
                numbers.append("å")



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

