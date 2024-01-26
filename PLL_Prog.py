import itertools                    # Used for the Generator of permutations
import UFace                        # This is where all the algs are

def Ex_PLL_Prog():
    # Program Code Begins here

    # Initialize all variables and flag variables
    sec_size_flag = True
    solution = []
    alglist = []
    addon_var = 2
    ind2 = 0

    # Create a list of the PLLs that you want to find the order of that will
    # start solved and end solved
    alglist_start = ['Aa','Ab','E','F','Ga','Gb','Gd','Gc','H','Jb','Jab',\
            'Na','Nb','Ra','Rb','T','Uaf','Ub','V','Y','Z']

    # Creates an object that is the u face of a Rubiks Cube
    cube = UFace.UFace()

    # Prompts the user for the chunk size for breaking up the list of algs
    while sec_size_flag:
        sectionsize = int(input('How big should the chunks be? '))
        # Input Checking: if out of range, asks user for valid input
        if sectionsize <= 0 or sectionsize > len(alglist_start):
            print ("Please input a number between 1 and " + \
                    str(len(alglist_start)))
        else:
            sec_size_flag = False

    # If the chunk size is less than half the length of the alg list then the
    # list is broken up and the left over algs are tacked onto the last chunk,
    # (This is the case if addon_var == 2). If you make your sectionsize over
    # half the size of the alg list, then this would make the first chunk to
    # check the ENTIRE list. To avoid this we set the addon_var to 1 so that if
    # the chunk size is over half the size of the list, the first chunk is
    # chunk size and the second chunk is what is left over.
    if sectionsize > len(alglist_start)/2.0:
        addon_var = 1

    # A float that represents how many chunks the alg list will be broken up
    # into.
    chunks = len(alglist_start)/sectionsize

    # Creates a list of sublists. Each sublist is a chunk of the alg list. Each
    # chunk (sublist) should be the length of the sectionsize as chosen by the
    # user. The last chunk will be longer or shorter than the others depending
    # on the sectionsize chosen (This is determined by the addon_var value)
    while chunks != 0:                      # while sublists can still be made
        if chunks >= addon_var:             # if we are not on the last chunk
            # Creates a new sublist that is length chosen by the user and is
            # the first or next section of the alglist.
            newsection = alglist_start[ind2:ind2+sectionsize]
            alglist.append(newsection)     # Appends the new sublist to alglist
            ind2 += sectionsize           # Updates index to beg. of next chunk
            chunks -= 1                     # One less sublist to add now
        else:                               # If we are on the last chunk
            # Last sublist will continue where left off to end of list
            newsection = alglist_start[ind2:len(alglist_start)]
            alglist.append(newsection)     # Appends last sublist to alglist
            chunks = 0                      # No more sublists to make

    # Iterates through all the sublists in alglist
    for entry in alglist:
        # Uses a generator that generates the next permutation of the sublist
        # and tests that permutation to see if it ends solved. The first
        # iteration resets the cube.
        for item in itertools.permutations(entry):
            cube.set_solved()                   # Resets the cube.
            # Executes the list of algorithms
            for entry in item:
                if entry == 'Aa':
                    cube.perf_Aa()
                if entry == 'Ab':
                    cube.perf_Ab()
                if entry == 'E':
                    cube.perf_E()
                if entry == 'F':
                    cube.perf_F()
                if entry == 'Ga':
                    cube.perf_Ga()
                if entry == 'Gb':
                    cube.perf_Gb()
                if entry == 'Gc':
                    cube.perf_Gc()
                if entry == 'Gd':
                    cube.perf_Gd()
                if entry == 'H':
                    cube.perf_H()
                if entry == 'Jab':
                    cube.perf_Jab()
                if entry == 'Jar':
                    cube.perf_Jar()
                if entry == 'Jal':
                    cube.perf_Jal()
                if entry == 'Jb':
                    cube.perf_Jb()
                if entry == 'Na':
                    cube.perf_Na()
                if entry == 'Nb':
                    cube.perf_Nb()
                if entry == 'Ra':
                    cube.perf_Ra()
                if entry == 'Rb':
                    cube.perf_Rb()
                if entry == 'T':
                    cube.perf_T()
                if entry == 'Uaf':
                    cube.perf_Uaf()
                if entry == 'Uar':
                    cube.perf_Uar()
                if entry == 'Ub':
                    cube.perf_Ub()
                if entry == 'V':
                    cube.perf_V()
                if entry == 'Y':
                    cube.perf_Y()
                if entry == 'Z':
                    cube.perf_Z()

            # After the algorithms are executed the cube is checked to see if
            # it is solved
            if cube.check_solved():
                print(list(item))           # Prints the Sublist just checked
                # Appends all the algs to a solution list that will be printed
                # for the user.
                for turns in list(item):
                    solution.append(turns)
                break

        # If the solution includes all the algs then we know we found a
        # complete solution
        if len(solution) == len(alglist_start):
            print("\n******************************************************************\n\
A solution was found. If your cube is solved when you start, doing\n\
the provided PLLs in this order will return to a solved cube:\n\
******************************************************************\n")
            print(solution)                 # Solution is printed
            break

    if len(solution) != len(alglist_start):
        print("There was no solution with that chunk size")

if __name__ == "__main__":
    Ex_PLL_Prog()
