import os

def crlib(name):
    os.mkdir(name)
    os.chdir("./" + name)
    
    f = open( name + ".cpp", 'w')
    f.write('#include "' + name + '.h"' + "\n")
    f.close()

    f = open( name + ".h", 'w')
    f.write("int i" + name + ";" + "\n")
    f.close()

    f = open( "jamfile.jam", 'w')
    f.write("lib " + name + " : " + name + ".cpp ; " + "\n")
    f.close()
    
    os.chdir("..")
    
alfa = ["a","b","c","d","e","f","g","h","i","j"]
numdir = [5,5,5,5,5,5,5]

def mkproj(g, g2, name):
    
    os.mkdir(name)
    os.chdir("./" + name)

    if ( g > 1):
        f = open("jamfile.jam", 'w')
        p = []
        n = numdir [-g]
        while n:
            n -= 1
            t = name + alfa[n]
            p.append(t)
            mkproj(g-1,g2,t)
            f.write("build-project " + t +" ;" "\n")

        f.write("lib " + name + " : " + name + ".cpp : <variant>release <threading>multi ;" "\n")
        f.write("lib " + name + " : " + name + ".cpp : <variant>release <threading>single ;" "\n")
        f.write("lib " + name + " : " + name + ".cpp : <variant>debug <threading>multi ;" "\n")
        f.write("lib " + name + " : " + name + ".cpp : <variant>debug <threading>single ;" "\n")
        f.close()

        f = open(name + ".cpp", 'w')
        f.write("\n")
        f.close()
    
    if ( g == 1):
        f = open("jamfile.jam", 'w')
        p = []
        n = numdir [-g]
        while n:
            n -= 1
            t = name + alfa[n]
            p.append(t)
            crlib(t)
            f.write("build-project " + t +" ;" "\n")

        f.write("lib " + name + " : " + name + ".cpp : <variant>release <threading>multi ;" "\n")
        f.write("lib " + name + " : " + name + ".cpp : <variant>release <threading>single ;" "\n")
        f.write("lib " + name + " : " + name + ".cpp : <variant>debug <threading>multi ;" "\n")
        f.write("lib " + name + " : " + name + ".cpp : <variant>debug <threading>single ;" "\n")
        f.close()

        f = open(name + ".cpp", 'w')
        f.write("\n")
        f.close()

        
        
    if ( g == g2):
        f = open(name + ".cpp", 'w')
        f.write("int main() {}")
        f.close()

        f = open("jamroot.jam", 'w')
        f.close()
        
    os.chdir("..")

    
mkproj(5,5,"big3")
