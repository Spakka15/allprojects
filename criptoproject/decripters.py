
ciao = ["a", "b", "c", "d", "e", "f", "g", "h"]


def get_decr_indx(numbers:list):

    cont = 0

    if numbers[0]=='£' and numbers[1]=='£' and numbers[2]=='%' and numbers[3]=='/' and numbers[4]=='$':
        return cont + 1
    if numbers[0]=='&' and numbers[1]=='%' and numbers[2]=='1' and numbers[3]=='1' and numbers[4]==';':
        return cont + 2
    if numbers[0]=='|' and numbers[1]=='|' and numbers[2]=='0' and numbers[3]=='&' and numbers[4]=='_':
        return cont + 3
    


def deleteprefix(numbers:list):

    for i in range(5):
        numbers.pop(0)
    return numbers


def decripter1(numbers: list):
    finale = []

    for i in range(len(numbers)):
        if numbers[i] == "|" or numbers[i] == "!":
            finale.append("a")

        elif numbers[i] == "£" or numbers[i] == "%":
            finale.append("b")

        elif numbers[i] == "^" or numbers[i] == "?":
            finale.append("c")

        elif numbers[i] == "+" or numbers[i] == "*":
            finale.append("d")

        elif numbers[i] == "{" or numbers[i] == "]":
            finale.append("e")

        elif numbers[i] == "}" or numbers[i] == "[":
            finale.append("f")

        elif numbers[i] == "(" or numbers[i] == "$":
            finale.append("g")

        elif numbers[i] == "/" or numbers[i] == "&":
            finale.append("h")

        elif numbers[i] == "ì" or numbers[i] == "è":
            finale.append("i")

        elif numbers[i] == ")" or numbers[i] == "=":
            finale.append("j")

        elif numbers[i] == "#" or numbers[i] == "@":
            finale.append("k")

        elif numbers[i] == "°" or numbers[i] == ",":
            finale.append("l")

        elif numbers[i] == ":" or numbers[i] == ".":
            finale.append("m")

        elif numbers[i] == ";" or numbers[i] == "-":
            finale.append("n")

        elif numbers[i] == "_" or numbers[i] == "ù":
            finale.append("o")

        elif numbers[i] == "§" or numbers[i] == "ç":
            finale.append("p")

        elif numbers[i] == "1" or numbers[i] == "8":
            finale.append("q")

        elif numbers[i] == "<" or numbers[i] == ">":
            finale.append("r")

        elif numbers[i] == "7" or numbers[i] == "3":
            finale.append("s")

        elif numbers[i] == "6" or numbers[i] == "5":
            finale.append("t")

        elif numbers[i] == "Ñ" or numbers[i] == "ñ":
            finale.append("u")

        elif numbers[i] == "ɛl":
            finale.append("v")

        elif numbers[i] == "kʉ":
            finale.append("w")

        elif numbers[i] == "æ":
            finale.append("x")

        elif numbers[i] == "ø":
            finale.append("y")

        elif numbers[i] == "å":
            finale.append("z")

        else:
            
            if numbers[i] == "c" or numbers[i] == "h":
                continue
            else:
                finale.append(numbers[i])

    return finale


def decripter2(numbers: list):

    finale = []

    for i in range(len(numbers)):

        if numbers[i] == "!" or numbers[i] == "|":
            finale.append("a")

        elif numbers[i] == "%" or numbers[i] == "£":
            finale.append("b")

        elif numbers[i] == "?" or numbers[i] == "^":
            finale.append("c")

        elif numbers[i] == "*":
            finale.append("d")

        elif numbers[i] == "]" or numbers[i] == "{":
            finale.append("e")

        elif numbers[i] == "[" or numbers[i] == "}":
            finale.append("f")

        elif numbers[i] == "$" or numbers[i] == "(":
            finale.append("g")

        elif numbers[i] == "&" or numbers[i] == "/":
            finale.append("h")

        elif numbers[i] == "è" or numbers[i] == "ì":
            finale.append("i")

        elif numbers[i] == "=" or numbers[i] == ")":
            finale.append("j")

        elif numbers[i] == "@" or numbers[i] == "#":
            finale.append("k")

        elif numbers[i] == "," or numbers[i] == "°":
            finale.append("l")

        elif numbers[i] == "." or numbers[i] == ":":
            finale.append("m")

        elif numbers[i] == "-" or numbers[i] == ";":
            finale.append("n")

        elif numbers[i] == "ù" or numbers[i] == "_":
            finale.append("o")

        elif numbers[i] == "ç" or numbers[i] == "§":
            finale.append("p")

        elif numbers[i] == "8" or numbers[i] == "1":
            finale.append("q")

        elif numbers[i] == ">" or numbers[i] == "<":
            finale.append("r")

        elif numbers[i] == "3" or numbers[i] == "7":
            finale.append("s")

        elif numbers[i] == "5" or numbers[i] == "6":
            finale.append("t")

        elif numbers[i] == "ñ" or numbers[i] == "Ñ":
            finale.append("u")

        elif numbers[i] == "ɛl":
            finale.append("v")

        elif numbers[i] == "kʉ":
            finale.append("w")

        elif numbers[i] == "æ":
            finale.append("x")

        elif numbers[i] == "ø":
            finale.append("y")

        elif numbers[i] == "å":
            finale.append("z")

        elif numbers[i]== "c" or numbers[i] == "h":
            continue

        else:
            finale.append(numbers[i])

    return finale


        
def decripter3(numbers: list):

    finale = []

    for i in range(len(numbers)):

        if numbers[i] == "å":
            finale.append("a")

        elif numbers[i] == "ø":
            finale.append("b")

        elif numbers[i] == "æ":
            finale.append("c")

        elif numbers[i] == "kʉ":
            finale.append("d")

        elif numbers[i] == "ɛl":
            finale.append("e")

        elif numbers[i] == "ñ" or numbers[i] == "Ñ":
            finale.append("f")

        elif numbers[i] == "5" or numbers[i] == "6":
            finale.append("g")

        elif numbers[i] == "3" or numbers[i] == "7":
            finale.append("h")

        elif numbers[i] == ">" or numbers[i] == "<":
            finale.append("i")

        elif numbers[i] == "=" or numbers[i] == ")":
            finale.append("j")

        elif numbers[i] == "8" or numbers[i] == "1":
            finale.append("k")

        elif numbers[i] == "," or numbers[i] == "°":
            finale.append("l")

        elif numbers[i] == "." or numbers[i] == ":":
            finale.append("m")

        elif numbers[i] == "-" or numbers[i] == ";":
            finale.append("n")

        elif numbers[i] == "ù" or numbers[i] == "_":
            finale.append("o")

        elif numbers[i] == "ç" or numbers[i] == "§":
            finale.append("p")

        elif numbers[i] == "@" or numbers[i] == "#":
            finale.append("q")

        elif numbers[i] == "è" or numbers[i] == "ì":
            finale.append("r")

        elif numbers[i] == "&" or numbers[i] == "/":
            finale.append("s")

        elif numbers[i] == "$" or numbers[i] == "(":
            finale.append("t")

        elif numbers[i] == "[" or numbers[i] == "}":
            finale.append("u")

        elif numbers[i] == "]" or numbers[i] == "{":
            finale.append("v")

        elif numbers[i] == "*":
            finale.append("w")

        elif numbers[i] == "?" or numbers[i] == "^":
            finale.append("x")

        elif numbers[i] == "%" or numbers[i] == "£":
            finale.append("y")

        elif numbers[i] == "!" or numbers[i] == "|":
            finale.append("z")

        elif numbers[i] == "c" or numbers[i] == "h":
            continue

        else:
            finale.append(numbers[i])

    return finale



        

    