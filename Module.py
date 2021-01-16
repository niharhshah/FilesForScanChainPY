global SizeOfIPVector
global SizeOfOPVector
global mask
global sIP
global numBits
global num
global j,i
global s
global q
def opfn(x,y):
    raise NotImplemented
    return 0
#Nihar
#Please Define your output function here only
#DO NOT CHANGE ANYTHING 
def tobin(number,bits):
    num = number
    numbits = 0
    p=""
    while(numbits < bits):
        vari = num %2
        if (vari == 1):
            p+="1"
        else:
            p+="0"
        num = int ( num / 2)
        numbits+=1
    return p[::-1]
#
#SizeOfIPVector = 3
def setup():
    
    print("This code creates trace file for given function defined in Output Function")
    print("This is currently set on \"+\" ")
    print("")
    print("please enter lenth of Single input and total output")
    print("please enter input and output")
    SizeOfIPVector = int(input("INPUTPINS: "))
    SizeOfOPVector = int(input("OUTPUTPINS: "))
    return SizeOfIPVector,SizeOfOPVector
    #file1.write("=====INPUT=========OUTPUT========Mask========\n")


def CheckFunction(SizeOfIPVector,SizeOfOPVector):
    i = 0
    mask = "1"*SizeOfOPVector
    sIP = 2**SizeOfIPVector
    numBits = 0
    num = 0
    j=0
    s = ""
    q=""
    while ( i < sIP):
        s=tobin(i,SizeOfIPVector)
        while ( j <sIP):
            mul = opfn(i,j)
            js=tobin(j,SizeOfIPVector)
            q=tobin(mul,SizeOfOPVector)
            j+=1
            print(s+js+" "+q+" "+mask)
        i +=1
        j=0
def Save(SizeOfIPVector,SizeOfOPVector):
    file1= open("TRACEFILE.txt","w",newline='')
    print("=====INPUT=========OUTPUT========Mask========")
    while ( i < sIP):
        s=tobin(i,SizeOfIPVector)
        while ( j <sIP):
            mul = opfn(i,j)
            js=tobin(j,SizeOfIPVector)
            q=tobin(mul,SizeOfOPVector)
            j+=1
            print(s+js+" "+q+" "+mask)
            file1.write(s+js+" "+q+" "+mask)
            file1.write('\n')
        i +=1
        j=0
    print("==============Done======================")
#file1.write("==============Done======================\n")
    file1.close
if __name__ == "__main__":
    x,y = setup()
    CheckFunction(x,y)
#    Save()
