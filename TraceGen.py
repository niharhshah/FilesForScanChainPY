#Nihar
#Please Define your output function here only
def opfn(vec1,vec2):
    mul=vec1+vec2
    return mul
#DO NOT CHANGE ANYTHING THIS IS VERY DEEP AND IMPORTANT SHIT
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
print("please enter input and output")
SizeOfIPVector = int(input("INPUTPINS: "))
SizeOfOPVector = int(input("OUTPUTPINS: "))
file1= open("TRACEFILE.txt","w",newline='')
print("=====INPUT=========OUTPUT========Mask========")
#file1.write("=====INPUT=========OUTPUT========Mask========\n")
mask = "1"*SizeOfOPVector
sIP = 2**SizeOfIPVector
i = 0
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
        file1.write(s+js+" "+q+" "+mask)
        file1.write('\n')
    i +=1
    j=0
print("==============Done======================")
#file1.write("==============Done======================\n")
file1.close
