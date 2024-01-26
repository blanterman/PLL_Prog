import UFace

def test_bench():
    print ("Testing: Creating cube object a ..."),
    a = UFace.UFace()
    if list(a.uface) == [['a','b','c'],['d','e','f'],['g','h','i']]:
        print ("Passed")
    else:
        print ("Failed to create Cube Object")
        return 0

    print ("Testing disp_uface")
    a.disp_uface()
    meas = input("Is the uface displayed correctly? (y or n) ")
    if meas == 'y' or meas == 'Y':
        print ("Passed")
    else:
        print ("Failed to display uface correctly")
        return 0

    print ("Testing Aa Perm")
    a.perf_Aa()
    if list(a.uface) == [['i','b','a'],['d','e','f'],['g','h','c']]:
        print("passed")
    else:
        print("Failed to perform Aa Perm")
        a.disp_uface()
        return 0

    print ("Testing Ab Perm")
    a.perf_Ab()
    if list(a.uface) == [['a','b','c'],['d','e','f'],['g','h','i']]:
        print("Passed")
    else:
        print("Failed to perform Ab Perm")
        a.disp_uface()
        return 0

    # Now
    # a b c
    # d e f
    # g h i

    print("Testing E Perm")
    a.perf_E()
    if list(a.uface) == [['g','b','i'],['d','e','f'],['a','h','c']]:
        print("passed")
    else:
        print("failed to perform E Perm")
        a.disp_uface()
        return 0

    # Now
    # g b i
    # d e f
    # a h c

    print("testing F perm")
    a.perf_F()
    if list(a.uface) == [['g','h','c'],['d','e','f'],['a','b','i']]:
        print("passed")
    else:
        print("failed to perform F Perm")
        a.disp_uface()
        return 0

    # now after F
    # g h c
    # d e f
    # a b i

    print("testing Ga perm")
    a.perf_Ga()
    if list(a.uface) == [['a','f','g'],['h','e','d'],['c','b','i']]:
        print("passed Ga")
    else:
        print("failed to perform Ga perm")
        a.disp_uface()
        return 0

    # After Ga
    # a f g
    # h e d
    # c b i
    
    print("testing Gb perm")
    a.perf_Gb()
    if list(a.uface) == [['g','h','c'],['d','e','f'],['a','b','i']]:
        print("Passed Gb")
    else:
        print("failed to perform Gb perm")
        a.disp_uface()
        return 0

    # After Gb
    # g h c 
    # d e f
    # a b i

    print("testing Gc perm")
    a.perf_Gc()
    if list(a.uface) == [['c','d','i'],['f','e','h'],['a','b','g']]:
        print ("passed Gc")
    else:
        print("failed to perfom Gc perm")
        a.disp_uface()
        return 0

    # after Gc
    # c d i
    # f e h
    # a b g
    
    print("testing Gd perm")
    a.perf_Gd()
    if list(a.uface) == [['c','h','g'],['b','e','f'],['a','d','i']]:
        print("passed Gd")
    else:
        print("failed to perfom Gd perm")
        a.disp_uface()
        return 0

    # after Gd without rotate
    # a b c
    # d e h
    # i f g

    # after Gd with rotate
    # c h g
    # b e f
    # a d i

    print("testing H perm")
    a.perf_H()
    if list(a.uface) == [['c','d','g'],['f','e','b'],['a','h','i']]:
        print("passed H")
    else:
        print("failed to perform H Perm")
        a.disp_uface()
        return 0
    
    # after H 
    # c d g
    # f e b
    # a h i

    print("testing Jb perm")
    a.perf_Jb()
    if list(a.uface) == [['c','d','i'],['f','e','h'],['a','b','g']]:
        print("passed Jb")
    else:
        print("failed to perform Jb Perm")
        a.disp_uface()
        return 0

    # after Jb
    # c d i
    # f e h
    # a b g
    
    print("testing Ja (back) perm")
    a.perf_Jab()
    if list(a.uface) == [['i','f','c'],['d','e','h'],['a','b','g']]:
        print("passed Ja (back)")
    else:
        print("failed to perform Ja (back) Perm")
        a.disp_uface()
        return 0

    # after Ja back
    # i f c
    # d e h
    # a b g

    print("testing Na perm")
    a.perf_Na()
    if list(a.uface) == [['i','f','a'],['h','e','d'],['c','b','g']]:
        print("passed Na")
    else:
        print("failed to perform Na Perm")
        a.disp_uface()
        return 0

    # after Na
    # i f a
    # h e d
    # c b g

    print("testing Nb perm")
    a.perf_Nb()
    if list(a.uface) == [['g','f','a'],['d','e','h'],['c','b','i']]:
        print("Passed Nb")
    else:
        print("failed to perform Nb Perm")
        a.disp_uface()
        return 0

    # after Nb
    # g f a
    # d e h
    # c b i

    print("testing Ra perm")
    a.perf_Ra()
    if list(a.uface) == [['g','d','i'],['f','e','h'],['c','b','a']]:
        print("Passed Ra")
    else:
        print("failed to perform Ra Perm")
        a.disp_uface()
        return 0

    # after Ra
    # g d i
    # f e h
    # c b a

    print("testing Rb perm")
    a.perf_Rb()
    if list(a.uface) == [['i','d','g'],['f','e','b'],['c','h','a']]:
        print("Passed Rb")
    else:
        print("failed to perform Rb Perm")
        a.disp_uface()
        return 0

    # after Rb
    # i d g 
    # f e b
    # c h a

    print("testing T perm")
    a.perf_T()
    if list(a.uface) == [['i','d','a'],['b','e','f'],['c','h','g']]:
        print("Passed T")
    else:
        print("failed to perform T Perm")
        a.disp_uface()
        return 0

    # after T
    # i d a
    # b e f
    # c h g

    print("testing Ua (front) perm")
    a.perf_Uaf()
    if list(a.uface) == [['i','d','a'],['f','e','h'],['c','b','g']]:
        print("Passed Ua (front)")
    else:
        print("failed to perform Ua (front) Perm")
        a.disp_uface()
        return 0

    # after Ua front
    # i d a
    # f e h
    # c b g

    print("testing Ub perm")
    a.perf_Ub()
    if list(a.uface) == [['i','d','a'],['b','e','f'],['c','h','g']]:
        print("Passed Ub")
    else:
        print("failed to perform Ub Perm")
        a.disp_uface()
        return 0

    # after Ub
    # i d a
    # b e f
    # c h g

    print("testing V perm")
    a.perf_V()
    if list(a.uface) == [['c','b','g'],['h','e','f'],['i','d','a']]:
        print("Passed V")
    else:
        print("failed to perform V Perm")
        a.disp_uface()
        return 0

    # after V before rotate
    # g f a
    # b e d
    # c h i

    # after V after rotate
    # c b g
    # h e f
    # i d a

    print("testing Y perm")
    a.perf_Y()
    if list(a.uface) == [['a','h','g'],['b','e','f'],['i','d','c']]:
        print("Passed Y")
    else:
        print("failed to perform Y Perm")
        a.disp_uface()
        return 0

    # after Y
    # a h g
    # b e f
    # i d c

    print("testing Z perm")
    a.perf_Z()
    if list(a.uface) == [['a','f','g'],['d','e','h'],['i','b','c']]:
        print("Passed Z")
    else:
        print("failed to perform Z Perm")
        a.disp_uface()
        return 0

    # after Z
    # a f g
    # d e h
    # i b c

    print("Testing y' perm")
    a.perf_yprime()
    if list(a.uface) == [['g','h','c'],['f','e','b'],['a','d','i']]:
        print("passed y prime")
    else:
        print("failed to perform y prime")
        a.disp_uface()
        return 0

    # after y'
    # g h c
    # f e b
    # a d i

    print("testing Ua (right) perm")
    a.perf_Uar()
    if list(a.uface) == [['g','b','c'],['f','e','d'],['a','h','i']]:
        print("Passed Ua (right)")
    else:
        print("failed to perform Ua (right) Perm")
        a.disp_uface()
        return 0

    # after Ua right
    # g b c
    # f e d
    # a h i

    print("testing the solved Setter/Checker")
    # Code up y' perm and then do an Gc to solve
    a.set_solved()
    if a.check_solved():
        print("Passed solved Setter/Checker")
    else:
        print("failed Solved Setter/Checker")
        a.disp_uface()
        return 0
    
    # after solved Checker
    # a b c        c f i        i h g        g d a
    # d e f   or   b e h   or   f e d   or   h e b
    # g h i        a d g        c b a        i f c


    print("Passed All Test")


if __name__ == "__main__":
    test_bench()
