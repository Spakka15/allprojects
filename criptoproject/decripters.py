
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
    return


def decripter1(numbers:list):
    pass

def decripter2(numbers:list):
    pass

def decripter3(numbers:list):
    pass


        

    