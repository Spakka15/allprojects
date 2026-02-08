import random



def criptalettere1(passw: str):
    numbers = []
    lenght = len(passw)

    for i in range(lenght):

        if passw[i] == 'a':
            if random.randint(1, 5) %2 == 0:
                numbers.append("|")
            else:               #bar vert e punto escl
                numbers.append("!")
        elif passw[i] == 'b' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("£")
            else:               #pund e perc
                numbers.append("%")
        elif passw[i] == 'c' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("^")
            else:               #pot e punto dom
                numbers.append("?")
        elif passw[i] == 'd' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("+")
            else:               #piu e per
                numbers.append("*")
        elif passw[i] == 'e' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("{")
            else:               #graffa ap quadra chius
                numbers.append("]")
        elif passw[i] == 'f':
            if random.randint(1, 5) %2 == 0:
                numbers.append("}")
            else:               #graf chius quadra apt
                numbers.append("[")
        elif passw[i] == 'g':
            if random.randint(1, 5) %2 == 0:
                numbers.append("(")
            else:               #quadara apt e dollaro
                numbers.append("$")
        elif passw[i] == 'h':
            if random.randint(1, 5) %2 == 0:
                numbers.append("/")
            else:               #norm slash . e comm
                numbers.append("&")
        elif passw[i] == 'i':
            if random.randint(1, 5) %2 == 0:
                numbers.append("ì")
            else:               #i acc e e acc
                numbers.append("è")
        elif passw[i] == 'j':
            if random.randint(1, 5) %2 == 0:
                numbers.append(")")
            else:               #quadra chius e ugu
                numbers.append("=")
        elif passw[i] == 'k':
            if random.randint(1, 5) %2 == 0:
                numbers.append("#")
            else:               #canc e chiocc
                numbers.append("@")
        elif passw[i] == 'l':
            if random.randint(1, 5) %2 == 0:
                numbers.append("°")
            else:               #gradi virgola
                numbers.append(",")
        elif passw[i] == 'm': #mezooooooooooooo
            if random.randint(1, 5) %2 == 0:
                numbers.append(":")
            else:               #du punt e punt
                numbers.append(".")
        elif passw[i] == 'n':
            if random.randint(1, 5) %2 == 0:
                numbers.append(";")
            else:               #punt virgola e tratt 
                numbers.append("-")
        elif passw[i] == 'o':
            if random.randint(1, 5) %2 == 0:
                numbers.append("_")
            else:               #tratt low u acc
                numbers.append("ù")
        elif passw[i] == 'p':
            if random.randint(1, 5) %2 == 0:
                numbers.append("§")
            else:               #s strana e c rumena
                numbers.append("ç")
        elif passw[i] == 'q' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("1")
            else:               #1 e 8
                numbers.append("8")
        elif passw[i] == 'r':
            if random.randint(1, 5) %2 == 0:
                numbers.append("<")
            else:               #magg e minore
                numbers.append(">")
        elif passw[i] == 's' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("7")
            else:               # 7 e  3
                numbers.append("3")
        elif passw[i] == 't' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("6")
            else:               #5 e 6
                numbers.append("5")
        elif passw[i] == 'u' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("Ñ")
            else:               #egne maiusc e minusc
                numbers.append("ñ")
        elif passw[i] == 'v' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("ɛl")
            else:               #l norvegese
                numbers.append("ɛl")
        elif passw[i] == 'w' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("kʉ")
            else:               #q norvegese
                numbers.append("kʉ")
        elif passw[i] == 'x' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("æ")
            else:               #strana norvegese
                numbers.append("æ")
        elif passw[i] == 'y' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("ø")
            else:               #o norvegese
                numbers.append("ø")
        elif passw[i] == 'z' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("å")
            else:               #a norvegese
                numbers.append("å")
        else:
            numbers.append(f"cc{passw[i]}")
    return


def criptalettere2(passw: str):
    numbers = []
    lenght = len(passw)

    for i in range(lenght):

        if passw[i] == 'a':
            if random.randint(1, 5) %2 == 0:
                numbers.append("!")
            else:               #bar vert e punto escl
                numbers.append("|")
        elif passw[i] == 'b' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("%")
            else:               #pund e perc
                numbers.append("£")
        elif passw[i] == 'c' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("?")
            else:               #pot e punto dom
                numbers.append("^")
        elif passw[i] == 'd' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("*")
            else:               #piu e per
                numbers.append("*")
        elif passw[i] == 'e' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("]")
            else:               #graffa ap quadra chius
                numbers.append("{")
        elif passw[i] == 'f':
            if random.randint(1, 5) %2 == 0:
                numbers.append("[")
            else:               #graf chius quadra apt
                numbers.append("}")
        elif passw[i] == 'g':
            if random.randint(1, 5) %2 == 0:
                numbers.append("$")
            else:               #quadara apt e dollaro
                numbers.append("(")
        elif passw[i] == 'h':
            if random.randint(1, 5) %2 == 0:
                numbers.append("&")
            else:               #norm slash . e comm
                numbers.append("/")
        elif passw[i] == 'i':
            if random.randint(1, 5) %2 == 0:
                numbers.append("è")
            else:               #i acc e e acc
                numbers.append("ì")
        elif passw[i] == 'j':
            if random.randint(1, 5) %2 == 0:
                numbers.append("=")
            else:               #quadra chius e ugu
                numbers.append(")")
        elif passw[i] == 'k':
            if random.randint(1, 5) %2 == 0:
                numbers.append("@")
            else:               #canc e chiocc
                numbers.append("#")
        elif passw[i] == 'l':
            if random.randint(1, 5) %2 == 0:
                numbers.append(",")
            else:               #gradi virgola
                numbers.append("°")
        elif passw[i] == 'm': #mezooooooooooooo
            if random.randint(1, 5) %2 == 0:
                numbers.append(".")
            else:               #du punt e punt
                numbers.append(":")
        elif passw[i] == 'n':
            if random.randint(1, 5) %2 == 0:
                numbers.append("-")
            else:               #punt virgola e tratt 
                numbers.append(";")
        elif passw[i] == 'o':
            if random.randint(1, 5) %2 == 0:
                numbers.append("ù")
            else:               #tratt low u acc
                numbers.append("_")
        elif passw[i] == 'p':
            if random.randint(1, 5) %2 == 0:
                numbers.append("ç")
            else:               #s strana e c rumena
                numbers.append("§")
        elif passw[i] == 'q' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("8")
            else:               #1 e 8
                numbers.append("1")
        elif passw[i] == 'r':
            if random.randint(1, 5) %2 == 0:
                numbers.append(">")
            else:               #magg e minore
                numbers.append("<")
        elif passw[i] == 's' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("3")
            else:               # 7 e  3
                numbers.append("7")
        elif passw[i] == 't' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("5")
            else:               #5 e 6
                numbers.append("6")
        elif passw[i] == 'u' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("ñ")
            else:               #egne maiusc e minusc
                numbers.append("Ñ")
        elif passw[i] == 'v' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("ɛl")
            else:               #l norvegese
                numbers.append("ɛl")
        elif passw[i] == 'w' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("kʉ")
            else:               #q norvegese
                numbers.append("kʉ")
        elif passw[i] == 'x' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("æ")
            else:               #strana norvegese
                numbers.append("æ")
        elif passw[i] == 'y' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("ø")
            else:               #o norvegese
                numbers.append("ø")
        elif passw[i] == 'z' :
            if random.randint(1, 5) %2 == 0:
                numbers.append("å")
            else:               #a norvegese
                numbers.append("å")
        else:
            numbers.append(f"cc{passw[i]}")
    return

