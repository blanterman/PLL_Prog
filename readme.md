This python script solves a rubik's cubing question, but a little backgroud first.

When solving the rubik's cube using the CFOP method, the last step is called PLL.
PLL stands for Permute Last Layer. Working up to PLL, you have completely solved
the bottom two layers, then oriented the pieces of the top layer so the appropriate
color is facing up. This leaves you with the top layer needing some of its pieces
(cubies) moved around to finish solving the cube. In fact, there are only twenty
one unique patterns that can exist (barring symmetrical cases) at this stage of
solving the rubiks cube.

To solve each of the twenty one patterns that exist at this stage, a cuber will 
use sequences of cube side rotations (algorithms or algs) that have been discovered
for each case. Each of the twenty one algorithms has been given a unique designation.

PLL Algorithms:
1.  Aa
2.  Ab
3.  E
4.  F
5.  Ga
6.  Gb
7.  Gc
8.  Gd
9.  H
10. Ja
11. Jb
12. Na
13. Nb
14. Ra
15. Rb
16. T
17. Ua
18. Ub
19. V
20. Y
21. Z


To decrease the time taken to solve the rubik's cube, a cuber will practice these
PLL algorithms over and over. When I wanted to practice them, I would do them in 
order, all twenty one, one after the other. The only issue was that if I started
with a solved cube, then went through the twenty one algs, the cube would be 
unsolved and I would have to perform one more PLL alg to completely solve the cube.

A question then arose, is there a magical sequency of PLL algorithms that will
allow me to one, start with a solved cube; two, perform each algorithm only once;
and three, end with a solved cube.

This script answers this question.

To answer the question for your self just insert the algorithms into the list
alglist_start in the PLL_Prog script. I recommend putting them in the order closest
to the what you want. Then run the script. The script will iterate through different
orderings to find one that starts solved and ends solved. It will then print out
the list of algs in the order needed.

Known issues:
It is a fact that though there are only twenty one unique cases for the PLL, each
case can occur in four different starting positions. This script currently assumes
a specific starting position (the one that I use) for each algorithm. So results
may not work out right if the assumed starting position doesn't match mine. 

Features:
- The script will ask you for a chunk size. This will break your alg list into smaller
lists and attempt to solve each of them in turn. It tries to be smart about this
so no matter what chunk size you give it, it doesn't end up with a 'too small' chunk
size. With too small chunck sizes you often get no solution, but with the proper
chunk size the solution can be found with greater speed. (Using the given code, 
try making your chunk size 21 and see how long it takes to find the solution, then
rerun with chunk size 12 to see the difference).

Future work
- (in progress) Allow for PLL algroithms from all orientations to be input. This
will be done with additional designation letters added to the alg name:
Aab (back), Aal (left), Aar (right), Aaf (front). I have started this for Ja and 
Ua.
- Alg interpreter - The user will be able to provide a list of algorithms in the
standard algorithm notation and the program will determing the algorithms with 
starting positions, then execute the script to find a solution.

