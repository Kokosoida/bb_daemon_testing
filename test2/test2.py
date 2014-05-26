import os
import random

alfa = ["a","b","c","d","e","f","g","h","i","j"]
string = ["x = y + z;\n", "x = y - z;\n", "x = x * y - x * z;\n" ]
numdir = [5,5,5,5,5,5,5]

def crlib(name):
    alfa1 = alfa + ["uoo"]
    
    f = open( name + ".cpp", 'w')
    f.write("#include <iostream>\n")
    f.write("using namespace std;" + "\n")
    f.write("int " + name + "()" + "\n")
    f.write("{" + "\n")

    f.write("int ")
    for i in alfa:
        f.write(i + ", ")
    f.write("uoo = 0;\n")

    for i in alfa:
        f.write("cin >>" + i + ";\n")

    for i in range(0,50000):
        ss = random.choice(string)
        ss = ss.replace("x", random.choice(alfa1) )
        ss = ss.replace("y", random.choice(alfa1) )
        ss = ss.replace("z", random.choice(alfa1) )
        f.write(ss)

    f.write("return 0;" + "\n")
    f.write("}\n")
    f.close()

f = open( "jamfile.jam", 'w')
for i in range(1,11):
    f.write("lib f" + str(i) +" : f" + str(i) + ".cpp ;\n")
    crlib("f" + str(i))

f.close()
