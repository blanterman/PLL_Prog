# This is the UFace class. This creates an object that is a 3x3 array that
# represents the top layer of a rubiks cube. The last step to solving a 3x3
# rubiks cube is to execute an algorithm that moves the positions of the pieces
# of the last layer of the cube so they are all in their correct position.
# This step is called the PLL (Permute Last Layer) step. There are 21 unique
# cases for this step. Two other factors: 1) starting position and 2) cube
# rotaions can be incorporated as well, so many more than the base 21 cases can
# and are used. This class will have functions for performing PLL algorithms,
# printing out the current state of the UFace, resetting the cube to a
# solved possition etc. etc. Each function has a description of what it does.

class UFace:

    # Constructor
    def __init__(self):
        # The object is initialized here. Just a 3x3 array in a "solved" state.
        self.uface = [['a','b','c'],['d','e','f'],['g','h','i']]

    # Setter function for returning the cube to a solved state
    def set_solved(self):
        self.uface = [['a','b','c'],['d','e','f'],['g','h','i']]

    # Function for displaying the UFace in a readable fashion
    def disp_uface(self):
        for row in self.uface:
            print(" ".join(row))

    # Function that checks if the UFace is solved. It is solved if it is in the
    # oringinal state or in the original state rotated once, twice, or three
    # times. Returns a True if solved, False if not solved.
    def check_solved(self):
        if self.uface == [['a','b','c'],['d','e','f'],['g','h','i']] or \
                self.uface == [['c','f','i'],['b','e','h'],['a','d','g']] or \
                self.uface == [['i','h','g'],['f','e','d'],['c','b','a']] or \
                self.uface == [['g','d','a'],['h','e','b'],['i','f','c']]:
            return True
        else:
            return False

    # Function of Aa(back) perm. Rotates 3 corner cubies clockwise. The
    # headlights are in the back on this one.
    def perf_Aa(self):
        hold = str(self.uface[2][2])
        self.uface[2][2] = str(self.uface[0][2])
        self.uface[0][2] = str(self.uface[0][0])
        self.uface[0][0] = hold

    # Function of Ab(right) perm. Rotates 3 corner cubies counter clockwise.
    # The headlights are on the right on this one.
    def perf_Ab(self):
        hold = str(self.uface[2][2])
        self.uface[2][2] = str(self.uface[0][0])
        self.uface[0][0] = str(self.uface[0][2])
        self.uface[0][2] = hold

    # Function of E(front to back) perm. Front corners with the ones on the
    # back layer. No criscrossing occurs.
    def perf_E(self):
        hold1 = str(self.uface[0][0])
        hold2 = str(self.uface[0][2])
        self.uface[0][0] = str(self.uface[2][0])
        self.uface[0][2] = str(self.uface[2][2])
        self.uface[2][0] = hold1
        self.uface[2][2] = hold2

    # Function of F(left) perm. Front right corner is swapped with back right
    # corner and front edge is swapped with back edge. The completed side is on
    # the left.
    def perf_F(self):
        hold1 = str(self.uface[0][1])
        hold2 = str(self.uface[0][2])
        self.uface[0][1] = str(self.uface[2][1])
        self.uface[0][2] = str(self.uface[2][2])
        self.uface[2][1] = hold1
        self.uface[2][2] = hold2

    # Function for Ga perm. Front left corner, back left corner, and back right
    # corner rotate positions in a clockwise direction. Left edge, back edge, 
    # and right edge rotate positions counter clockwise.
    def perf_Ga(self):
        hold1 = str(self.uface[2][0])
        hold2 = str(self.uface[1][0])
        self.uface[2][0] = str(self.uface[0][2])
        self.uface[0][2] = str(self.uface[0][0])
        self.uface[0][0] = hold1
        self.uface[1][0] = str(self.uface[0][1])
        self.uface[0][1] = str(self.uface[1][2])
        self.uface[1][2] = hold2

    # Function for Gb perm. Front left corner, back left corner, and back right
    # corner rotate positions in a counter clockwise direction. Left edge, back
    # edge, and right edge rotate positions clockwise.
    def perf_Gb(self):
        hold1 = str(self.uface[2][0])
        hold2 = str(self.uface[1][0])
        self.uface[2][0] = str(self.uface[0][0])
        self.uface[0][0] = str(self.uface[0][2])
        self.uface[0][2] = hold1
        self.uface[1][0] = str(self.uface[1][2])
        self.uface[1][2] = str(self.uface[0][1])
        self.uface[0][1] = hold2

    def perf_Gc(self):
        hold1 = str(self.uface[2][2])
        hold2 = str(self.uface[1][2])
        self.uface[2][2] = str(self.uface[0][0])
        self.uface[0][0] = str(self.uface[0][2])
        self.uface[0][2] = hold1
        self.uface[1][2] = str(self.uface[0][1])
        self.uface[0][1] = str(self.uface[1][0])
        self.uface[1][0] = hold2

    def perf_Gd(self):
        hold1 = str(self.uface[2][0])
        hold2 = str(self.uface[1][0])
        self.uface[2][0] = str(self.uface[0][2])
        self.uface[0][2] = str(self.uface[0][0])
        self.uface[0][0] = hold1
        self.uface[1][0] = str(self.uface[0][1])
        self.uface[0][1] = str(self.uface[2][1])
        self.uface[2][1] = hold2
        hold3 = list(zip(*self.uface))[::-1]
        self.uface = [list(elem) for elem in hold3]

    def perf_H(self):
        hold1 = str(self.uface[0][1])
        hold2 = str(self.uface[1][0])
        self.uface[0][1] = str(self.uface[2][1])
        self.uface[2][1] = hold1
        self.uface[1][0] = str(self.uface[1][2])
        self.uface[1][2] = hold2

    def perf_Jab(self):
        hold1 = str(self.uface[0][0])
        hold2 = str(self.uface[1][0])
        self.uface[0][0] = str(self.uface[0][2])
        self.uface[0][2] = hold1
        self.uface[1][0] = str(self.uface[0][1])
        self.uface[0][1] = hold2

    def perf_Jar(self):
        hold1 = str(self.uface[0][2])
        hold2 = str(self.uface[0][1])
        self.uface[0][2] = str(self.uface[2][2])
        self.uface[2][2] = hold1
        self.uface[0][1] = str(self.uface[1][2])
        self.uface[1][2] = hold2

    def perf_Jal(self):
        hold1 = str(self.uface[2][0])
        hold2 = str(self.uface[2][1])
        self.uface[2][0] = str(self.uface[0][0])
        self.uface[0][0] = hold1
        self.uface[2][1] = str(self.uface[1][0])
        self.uface[1][0] = hold2

    def perf_Jb(self):
        hold1 = str(self.uface[2][2])
        hold2 = str(self.uface[2][1])
        self.uface[2][2] = str(self.uface[0][2])
        self.uface[0][2] = hold1
        self.uface[2][1] = str(self.uface[1][2])
        self.uface[1][2] = hold2

    def perf_Na(self):
        hold1 = str(self.uface[0][2])
        hold2 = str(self.uface[1][2])
        self.uface[0][2] = str(self.uface[2][0])
        self.uface[2][0] = hold1
        self.uface[1][2] = str(self.uface[1][0])
        self.uface[1][0] = hold2

    def perf_Nb(self):
        hold1 = str(self.uface[0][0])
        hold2 = str(self.uface[1][0])
        self.uface[0][0] = str(self.uface[2][2])
        self.uface[2][2] = hold1
        self.uface[1][0] = str(self.uface[1][2])
        self.uface[1][2] = hold2

    def perf_Ra(self):
        hold1 = str(self.uface[0][2])
        hold2 = str(self.uface[0][1])
        self.uface[0][2] = str(self.uface[2][2])
        self.uface[2][2] = hold1
        self.uface[0][1] = str(self.uface[1][0])
        self.uface[1][0] = hold2

    def perf_Rb(self):
        hold1 = str(self.uface[0][2])
        hold2 = str(self.uface[1][2])
        self.uface[0][2] = str(self.uface[0][0])
        self.uface[0][0] = hold1
        self.uface[1][2] = str(self.uface[2][1])
        self.uface[2][1] = hold2

    def perf_T(self):
        hold1 = str(self.uface[0][2])
        hold2 = str(self.uface[1][2])
        self.uface[0][2] = str(self.uface[2][2])
        self.uface[2][2] = hold1
        self.uface[1][2] = str(self.uface[1][0])
        self.uface[1][0] = hold2

    def perf_Uaf(self):
        hold = str(self.uface[2][1])
        self.uface[2][1] = str(self.uface[1][0])
        self.uface[1][0] = str(self.uface[1][2])
        self.uface[1][2] = hold

    def perf_Uar(self):
        hold = str(self.uface[0][1])
        self.uface[0][1] = str(self.uface[1][2])
        self.uface[1][2] = str(self.uface[2][1])
        self.uface[2][1] = hold

    def perf_Ub(self):
        hold = str(self.uface[2][1])
        self.uface[2][1] = str(self.uface[1][2])
        self.uface[1][2] = str(self.uface[1][0])
        self.uface[1][0] = hold

    def perf_V(self):
        hold1 = str(self.uface[0][0])
        hold2 = str(self.uface[0][1])
        self.uface[0][0] = str(self.uface[2][2])
        self.uface[2][2] = hold1
        self.uface[0][1] = str(self.uface[1][2])
        self.uface[1][2] = hold2
        hold3 = list(zip(*self.uface[::-1]))
        self.uface = [list(elem) for elem in hold3]

    def perf_Y(self):
        hold1 = str(self.uface[0][0])
        hold2 = str(self.uface[0][1])
        self.uface[0][0] = str(self.uface[2][2])
        self.uface[2][2] = hold1
        self.uface[0][1] = str(self.uface[1][0])
        self.uface[1][0] = hold2

    def perf_Z(self):
        hold1 = str(self.uface[0][1])
        hold2 = str(self.uface[1][0])
        self.uface[0][1] = str(self.uface[1][2])
        self.uface[1][2] = hold1
        self.uface[1][0] = str(self.uface[2][1])
        self.uface[2][1] = hold2

    def perf_yprime(self):
        hold = list(zip(*self.uface))[::-1]
        self.uface = [list(elem) for elem in hold]

