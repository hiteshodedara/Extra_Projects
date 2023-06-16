import colorama
from colorama import Fore
class letter:

    def a():
            
        height = 5
        width = 4 


        for row in range(height):
            for col in range(width):
                if (row == 0 or row == height // 2 or col == 0 or col == width - 1):
                    print( "*", end="")
                else:
                    print( " ", end="")
            print()


    def b():
        height = 5
        width = 4

        for row in range(height):
            for col in range(width):
                if (col == 0 or (row == 0 or row == height // 2 or row == height - 1) and col < width - 1
                        or (row == height // 4 or row == 3 * height // 4) and col == width - 1):
                    print( "*", end="")
                else:
                    print( " ", end="")
            print()

    def c():
        height = 5
        width = 4

        for row in range(height):
            for col in range(width):
                if (col == 0 or (row == 0 or row == height - 1) and col > 0):
                    print( "*", end="")
                else:
                    print( " ", end="")
            print()

    def d():
        height = 5
        width = 4

        for row in range(height):
            for col in range(width):
                if (col == 0 or (row == 0 or row == height - 1) and col < width - 1
                        or col == width - 1 and (row != 0 and row != height - 1)):
                    print( "*", end="")
                else:
                    print( " ", end="")
            print()
    def e():
        height = 5
        width = 4

        for row in range(height):
            for col in range(width):
                if (col == 0 or row == 0 or row == height - 1 or (row == height // 2 and col < width - 1)):
                    print( "*", end="")
                else:
                    print(" ", end="")
            print()

    def f():
        height = 5
        width = 4

        for row in range(height):
            for col in range(width):
                if col == 0 or (row == 0 or row == height // 2) and col < width - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    def g():
        letter_g = [
        " **** ",
        "*     ",
        "*  ** ",
        "*   * ",
        " **** "
        ]

        for line in letter_g:
            print(line)



    def h():

        height = 5
        width = 4

        for row in range(height):
            for col in range(width):
                if (col == 0 or col == width - 1 or row == height // 2):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    def i():
        letter_i = [
            "***",
            " * ",
            " * ",
            " * ",
            "***"
        ]

        for line in letter_i:
            print(line)
    def j():
        pattern = [
            "*****",
            "   *",
            "   *",
            "*  *",
            " ***",

        ]

        for line in pattern:
            print(line)

    def k():
        pattern = [
            "*  *",
            "* *",
            "**",
            "* *",
            "*  *"
        ]

        for line in pattern:
            print(line)
    def l():
        pattern = [
        "*",
        "*",
        "*",
        "*",
        "****"
        ]

        for line in pattern:
            print(line)

    def m():
        pattern = [
        "*     *",
        "* * * *",
        "*  *  *",
        "*     *",
        "*     *",
    
        ]

        for line in pattern:
            print(line)
    def n():
        pattern = [
        "*     *",
        "* *   *",
        "*   * *",
        "*     *",
        
        
        ]

        for line in pattern:
            print(line)

    def o():
        pattern = [
        "  ****  ",
        " *    * ",
        "*      *",
        "*      *",
        " *    * ",
        "  ****  "
        ]

        for line in pattern:
            print(line)
    def p():
        pattern = [
        "****",
        "*   *",
        "*   *",
        "**** ",
        "*    ",
        "*    "
        ]

        for line in pattern:
            print(line)

    def q():
        pattern = [
            " ****",
            "*    *",
            "*    *",
            "*    *",
            " *  * ",
            "  ** *"
        ]

        for line in pattern:
            print(line)

    def r():
        pattern = [
            "****",
            "*   *",
            "*   *",
            "****",
            "*  *",
            "*   *",
        ]

        for line in pattern:
            print(line)

    def s():
        pattern = [
            " ****",
            "*    ",
            "**** ",
            "    *",
            "**** "
        ]

        for line in pattern:
            print(line)

    def t():
        pattern = [
            "*****",
            "  *  ",
            "  *  ",
            "  *  ",
            "  *  "
        ]

        for line in pattern:
            print(line)

    def u():
        pattern = [
            "*   *",
            "*   *",
            "*   *",
            "*   *",
            " *** "
        ]

        for line in pattern:
            print(line)
    def v():
        pattern = [
            "*   *",
            "*   *",
            " * * ",
            " * * ",
            "  *  "
        ]

        for line in pattern:
            print(line)

    def w():
        pattern = [
            "*     *",
            "*     *",
            "*  *  *",
            "* * * *",
            "*     * ",
        ]

        for line in pattern:
            print(line)

    def x():
        pattern = [
            "*   *",
            " * * ",
            "  *  ",
            " * * ",
            "*   *"
        ]

        for line in pattern:
            print(line)
    def y():
        pattern = [
            "*   *",
            " * * ",
            "  *  ",
            "  *  ",
            "  *  "
        ]

        for line in pattern:
            print(line)

    def z():
        pattern = [
            "*****",
            "   * ",
            "  *  ",
            " *   ",
            "*****"
        ]

        for line in pattern:
            print(line)

    def mai(self):
        name=input(Fore.GREEN +"Enter Your Name: ")
        new=name.lower()
        coun=len(new)

        dic={
            "a":letter.a,"b":letter.b,"c":letter.c,"d":letter.d,"e":letter.e,"f":letter.f,"g":letter.g,"h":letter.h,"i":letter.i,
            "j":letter.j,"k":letter.k,"l":letter.l,"m":letter.m,"n":letter.n,"o":letter.o,"p":letter.p,"q":letter.q,"r":letter.r,
            "s":letter.s,"t":letter.t,"u":letter.u,"v":letter.v,"w":letter.w,"x":letter.x,"y":letter.y,"z":letter.z
            }
        
        for fo in range(int(coun)):
            print("\n")
            font=new[fo]
            dic[font]()
    
if __name__ == '__main__':
    fon=letter()
    fon.mai()
