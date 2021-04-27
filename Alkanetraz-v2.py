from tkinter import *
import tkinter.font as font
from scipy.optimize import minimize

"""
The following four functions (myclick, ..., Myclick4) basically allow to change the text on the button between a blank,
a carbon ("C") and a bond ("-" or "|")
"""


def my_click(a, b):
    button[a][b].configure(text='C', command=lambda: my_click2(a, b))


def my_click2(a, b):
    button[a][b].configure(text='-', command=lambda: my_click3(a, b))


def my_click3(a, b):
    button[a][b].configure(text='|', command=lambda: my_click4(a, b))


def my_click4(a, b):
    button[a][b].configure(text=' ', command=lambda: my_click(a, b))


def build_default_dataset():

    """
    This function is called to write a file containing all the compounds from the by default dataset
    """

    db = open('database.txt', 'w+')
    f = \
        '5 4 3 2 1 0 0 13 341.9\n5 5 3 2 0 0 2 11 334\n5 5 4 1 0 0 \
1 12 336.4\n5 7 3 0 0 0 3 9 322.9\n5 6 4 0 0 0 4 10 331.2\n6 5 \
4 3 2 1 0 21 371.6\n6 6 6 3 0 0 0 20 366.6\n6 6 5 3 1 0 1 19 \
364.97\n6 6 4 3 2 0 2 18 363.2\n6 7 6 2 0 0 3 17 362.9\n6 8 6 1 \
0 0 2 16 359.2\n6 7 4 4 0 0 4 15 353.7\n6 8 4 3 0 0 3 14 \
352.3\n6 9 6 0 0 0 5 13 354.1\n7 6 5 4 3 2 0 34 398.7\n7 7 6 4 \
3 1 1 31 392\n7 7 7 5 2 0 0 32 391.7\n7 9 9 3 0 0 1 28 391.5\n7 \
8 8 4 1 0 2 29 391\n7 7 6 5 2 1 1 30 390.9\n7 7 5 4 3 2 2 29 \
390.7\n7 8 8 5 0 0 2 28 388.8\n7 8 7 4 2 0 3 27 389\n7 10 9 2 \
0 0 4 23 387.8\n7 9 8 4 0 0 5 24 386.8\n7 9 7 4 1 0 2 25 \
385.1\n7 10 8 3 0 0 4 22 383.1\n7 8 6 5 2 0 3 26 382\n7 8 5 4 4 \
0 4 25 382.1\n7 9 5 4 3 0 3 23 380\n7 12 9 0 0 0 6 17 379.6\n7 \
10 5 6 0 0 5 19 372.4\n8 7 6 5 4 3 0 55 423.8\n8 8 8 6 4 2 0 52 \
416.42\n8 8 8 7 4 1 0 51 414.45\n8 8 7 5 4 3 1 50 417\n8 8 7 6 \
4 2 1 49 415\n8 10 12 6 0 0 0 48 419.3\n8 9 10 7 2 0 1 48 \
413.55\n8 8 6 5 4 3 2 47 416.1\n8 9 9 6 3 1 2 46 413.6\n8 9 9 7 \
3 0 2 45 411.15\n8 9 8 6 4 1 2 45 408.76\n8 10 10 6 2 0 1 44 \
413.75\n8 9 8 5 4 2 3 44 413\n8 9 8 7 4 0 2 44 406.95\n8 9 7 5 \
5 2 3 43 408\n8 10 10 6 2 0 4 41 412\n8 10 8 5 4 1 2 41 410\n8 \
9 7 7 3 2 3 41 406\n8 11 12 5 0 0 3 40 414.75\n8 9 6 5 4 4 4 40 \
408\n8 11 11 5 1 0 3 39 413.31\n8 10 10 8 0 0 4 39 409.81\n8 10 \
8 7 2 1 2 39 408.08\n8 10 6 5 4 3 3 37 405\n8 10 8 6 4 0 5 37 \
404\n8 11 10 5 2 0 4 36 410.23\n8 11 10 7 0 0 3 36 406.9\n8 11 \
9 5 3 0 4 35 406.27\n8 11 8 7 2 0 4 34 404\n8 12 12 4 0 0 6 33 \
414.65\n8 11 7 7 3 0 4 33 399.6\n8 11 6 5 6 0 5 32 397\n8 12 10 \
6 0 0 6 31 406.15\n8 13 12 3 0 0 5 30 413.42\n8 13 6 9 0 0 6 24 \
395.4\n9 8 7 6 5 4 0 89 447.3\n9 9 7 6 5 4 2 76 440.09\n9 9 8 6 \
5 4 1 81 440.9\n9 9 8 7 5 4 1 79 440\n9 9 8 7 6 3 1 80 \
438.26\n9 9 9 7 5 4 0 84 439.15\n9 9 9 8 6 3 0 83 436.51\n9 11 \
7 6 5 4 3 60 427.15\n9 10 9 6 5 4 3 71 437.39\n9 10 8 8 5 3 3 \
67 429.05\n9 10 8 7 6 3 3 68 430.08\n9 10 8 6 5 5 3 69 432\n9 \
10 7 6 5 4 4 65 433.2\n9 11 9 6 5 4 2 66 434.35\n9 10 9 8 5 3 2 \
71 432\n9 11 9 8 5 2 2 64 430.65\n9 10 10 8 5 2 2 73 435.57\n9 \
9 9 9 6 3 0 81 435\n9 10 10 9 6 1 2 72 431.95\n9 11 11 7 5 2 1 \
72 437\n9 10 10 8 6 2 1 76 431.45\n9 11 11 9 4 1 1 69 432.15\n9 \
12 8 9 4 3 4 52 422\n9 12 8 6 7 3 4 55 419.15\n9 12 7 6 5 6 5 \
51 421.48\n9 12 11 6 5 2 4 59 433.2\n9 11 11 8 4 2 4 65 429\n9 \
11 9 6 6 4 5 61 423\n9 12 9 10 3 2 4 53 422.7\n9 11 8 9 4 4 5 \
56 419.9\n9 12 9 6 7 2 4 57 425.95\n9 12 10 8 5 1 3 59 \
428.82\n9 11 13 9 3 0 0 76 437.63\n9 10 12 10 4 0 0 80 435.9\n9 \
12 9 9 6 0 3 56 420.2\n9 12 11 9 4 0 3 60 431.15\n9 14 13 6 3 0 \
5 47 432\n9 13 12 8 3 0 5 53 429.8\n9 13 10 7 6 0 6 48 421.8\n9 \
13 9 8 6 0 6 47 421.19\n9 14 7 6 9 0 6 41 410.32\n9 13 14 7 2 0 \
5 56 437.74\n9 13 11 8 4 0 6 49 426\n9 13 13 8 2 0 5 55 435.4\n9 \
12 12 8 4 0 6 58 428.6\n9 14 15 6 1 0 4 53 443.47\n9 12 12 12 0 \
0 6 54 430.19\n9 13 12 11 0 0 5 50 428.45\n9 13 15 8 0 0 5 57 \
442.59\n9 15 15 6 0 0 7 43 439.2\n9 15 12 9 0 0 7 40 432.44\n10 \
9 8 7 6 5 0 144 468\n10 10 8 7 6 5 2 123 462.3\n10 10 9 7 6 5 1 \
131 464.05\n10 10 9 8 6 5 1 128 460.1\n10 10 9 8 7 5 1 129 \
459.95\n10 12 14 12 6 1 0 120 456.5\n10 13 12 12 6 2 3 94 \
443.15\n10 16 11 9 9 0 7 61 438.3\n10 14 9 11 5 6 6 71 \
435.2\n10 15 8 7 6 9 6 65 433.45\n10 16 14 9 6 0 7 64 446.2\n10 \
13 9 10 6 4 4 85 443.2\n10 12 10 10 6 5 4 97 441.15\n10 12 8 7 \
6 5 3 97 459.15\n10 11 10 7 6 5 3 115 459.95\n10 11 9 9 6 5 3 \
108 451.15\n10 12 12 11 6 4 4 102 451.25\n10 13 12 10 6 4 6 89 \
446.7\n10 15 14 7 6 3 5 77 452.8\n10 13 15 11 5 1 2 107 454\n10 \
12 12 8 6 5 1 116 458.9\n10 12 14 10 6 3 0 124 459.9\n10 10 10 \
10 8 5 0 132 455.75\n11 10 9 8 7 6 0 233 489\n11 17 10 13 6 9 7 \
90 451\n11 11 9 8 7 6 2 199 483.2\n11 16 13 8 11 6 4 130 \
462.9\n11 15 10 11 8 5 6 118 457.85\n11 16 9 8 7 6 6 106 460\n11 \
17 11 16 5 6 7 91 458.2\n11 15 16 12 9 3 4 149 470.95\n11 11 11 \
9 7 6 0 220 482\n11 11 11 10 8 6 0 217 477.65\n11 11 10 8 7 6 1 \
212 484.35\n11 11 10 9 7 6 1 207 480.25\n11 11 10 9 8 6 1 209 \
477.75\n11 12 14 14 10 4 0 205 473.65\n11 14 12 12 9 4 6 137 \
459.4\n11 13 9 8 7 6 3 157 472.15\n11 12 11 8 7 6 3 \
186 476.55\n11 12 10 10 7 6 3 175 471.65\n11 12 12 10 9 6 2 194 \
470.65\n11 11 11 9 7 6 0 220 481.95\n11 14 13 12 8 8 6 141 \
460\n11 16 14 9 10 6 7 118 461.95\n11 16 11 8 7 10 5 116 \
455.9\n11 15 11 12 9 4 6 121 457\n11 18 16 12 9 0 8 97 465\n11 \
12 11 11 10 7 2 183 462\n11 13 13 12 7 6 4 165 470.85\n11 14 10 \
11 7 6 4 137 464.75\n11 13 11 12 7 7 4 153 459.15\n11 13 10 9 \
10 5 5 154 463\n11 12 13 10 8 8 0 208 476\n11 13 15 11 7 6 0 \
200 478\n11 12 13 12 9 5 1 199 467.65\n11 13 13 11 10 5 1 185 \
469.15\n11 11 11 11 9 7 0 213 475.65\n11 11 11 11 10 7 0 215 \
477.65\n12 11 10 9 8 7 0 377 508.59\n13 12 11 10 9 8 0 610 \
526.72\n14 13 12 11 10 9 0 987 543.78\n15 14 13 12 11 10 0 1597 \
559.943\n16 15 14 13 12 11 0 2584 574.97\n17 16 15 14 13 12 0 \
4181 589.27\n18 17 16 15 14 13 0 6765 602.85\n19 18 17 16 15 14 \
0 10946 615.85\n20 19 18 17 16 15 0 17711 629.65\n21 20 19 18 \
17 16 0 28657 641.75'
    db.write(f)
    db.close()


def graph_to_boiling_point(button, ndim):

    """
    This function calculates the methyl index, Wiener path numbers and Hosoya index using the function Myfc,                ## CHANGE THIS!
    retrieves the current optimal parameters from the relevant file and use all the aforementioned data to calculate the
    boiling point by calling the function boilingpoint2.
    """

    nmatches, pathvector, methylindex = graph_to_descriptors(button, ndim)
    try:
        bp = open('parameters.txt')
        bp.close()
    except IOError:
        pm = open('parameters.txt', 'w+')
        pm.write('847.41474 221.61698 -1182.20853 0.00125 -3.02445 -2.16070 -0.56366 -2.10575 -9.61075\n')
        pm.write('0.49420 0.03689 3.39724 0.93751 1.01631 1.38233 0.5695 0.19907')
        pm.close()
    screxecuter.configure(text='Boil. Point')
    pm = open('parameters.txt', 'r')
    AB = pm.readlines()
    A = AB[0].split()
    B = AB[1].split()
    pm.close()
    for i in range(len(A) - 1):
        A[i] = float(A[i])
        B[i] = float(B[i])
    A[len(A) - 1] = float(A[len(A) - 1])
    for i in range(len(B)):
        A.append(B[i])
    chempar = []
    for i in range(6):
        chempar.append(pathvector[i + 1])
    chempar.append(methylindex)
    chempar.append(nmatches)
    bpoint = boiling_point(A, chempar)

    scrtext.configure(text='Boiling point ' + str(bpoint) + ' K')


def append_to_database(button, ndim):

    """
    This function creates the by default data base using the function buildfile if it doesn't already exists,
    then recovers the methyl index, Wiener path numbers and Hosoya index using the function Myfc and adds the parameters
    as well as the temperature provided by the user, to the list.
    """

    temp = tempentry.get()
    try:
        float(temp)
    except ValueError:
        scrfitter.configure(text='Error!')
        return
    nmatches, pathvector, methylindex = graph_to_descriptors(button, ndim)
    try:
        open('database.txt')
    except IOError:
        build_default_dataset()
    db = open('database.txt', 'r')
    f = db.readlines()
    expvar = [[]]
    for x in range(len(f)):
        f1 = f[x].split()
        expvar.append(
            [float(f1[0]), float(f1[1]), float(f1[2]), float(f1[3]), float(f1[4]), float(f1[5]), float(f1[6]),
             float(f1[7]), float(f1[8])]
        )
        if (
                float(f1[0]) == pathvector[1] and float(f1[1]) == pathvector[2]
                and float(f1[2]) == pathvector[3] and float(f1[3]) == pathvector[4]
                and float(f1[4]) == pathvector[5] and float(f1[5]) == pathvector[6]
                and float(f1[6]) == methylindex and float(f1[7]) == nmatches
        ):
            scrfitter.configure(text='already in the base!')
            return
    db.close()
    db = open('database.txt', 'a')
    db.write(
        '\n' + str(pathvector[1]) + ' '
        + str(pathvector[2]) + ' ' + str(pathvector[3]) + ' '
        + str(pathvector[4]) + ' ' + str(pathvector[5]) + ' '
        + str(pathvector[6]) + ' ' + str(methylindex) + ' '
        + str(nmatches) + ' ' + str(temp)
    )
    db.close()
    scrfitter.configure(text='Added to the base!')


def learn_from_new_set():

    """
    This function creates a file containing by-default parameters if it doesn't exist, then writes a file containing the
    by-default a data set if it doesn't exist. Then, it minimizes the standard deviation of the boiling points using
    the function bpdum using the scipy minimize routine with a Nelder-Mead algorithm,  and if the new set of parameters
    indeed yield a lower standard deviation, the parameter file is replaced with a file containing the new parameters.
    """

    try:
        open('parameters.txt')
    except IOError:
        pm = open('parameters.txt', 'w+')
        pm.write('847.41474 221.61698 -1182.20853 0.00125 -3.02445 -2.16070 -0.56366 -2.10575 -9.61075\n')
        pm.write('0.49420 0.03689 3.39724 0.93751 1.01631 1.38233 0.5695 0.19907')
        pm.close()
    pm = open('parameters.txt', 'r')
    try:
        open('database.txt')
    except IOError:
        build_default_dataset()
    AB = pm.readlines()
    A = AB[0].split()
    B = AB[1].split()
    for i in range(len(A) - 1):
        A[i] = float(A[i])
        B[i] = float(B[i])
    A[len(A) - 1] = float(A[len(A) - 1])
    for i in range(len(B)):
        A.append(B[i])
    optdic = {
        'maxiter': 10000,
        'disp': False
    }
    optres = minimize(
        cost_function, A, args=(), method='Nelder-Mead', jac=None, hess=None, hessp=None, bounds=None, constraints=(),
        tol=10 ** (-3), callback=None, options=optdic
    )
    Abis = optres.x
    fun0 = cost_function(A)
    if optres.fun <= fun0:
        A = Abis
        pm = open('parameters.txt', 'w+')
        pm.write(
            str(A[0]) + ' '
            + str(A[1]) + ' ' + str(A[2]) + ' '
            + str(A[3]) + ' ' + str(A[4]) + ' '
            + str(A[5]) + ' ' + str(A[6]) + ' '
            + str(A[7]) + ' ' + str(A[8]) + '\n'
            + str(A[9]) + ' ' + str(A[10]) + ' '
            + str(A[11]) + ' ' + str(A[12]) + ' '
            + str(A[13]) + ' ' + str(A[14]) + ' '
            + str(A[15]) + ' ' + str(A[16])
        )
    return


def cost_function(A):

    """
    Calculates the standard deviation of the boiling points over the range of all the data points in the data file
    using the input parameters.
    """

    db = open('database.txt', 'r')
    findthem = db.readlines()
    f = 0
    for i in range(len(findthem)):
        tuple1 = findthem[i].split()
        for j in range(len(tuple1)):
            tuple1[j] = float(tuple1[j])
        f1 = A[0] \
             + A[1] * (tuple1[0] ** A[9]) \
             + A[2] * (tuple1[1] ** A[10]) \
             + A[3] * (tuple1[2] ** A[11]) \
             + A[4] * (tuple1[3] ** A[12]) \
             + A[5] * (tuple1[4] ** A[13]) \
             + A[6] * (tuple1[5] ** A[14]) \
             + A[7] * (tuple1[6] ** A[15]) \
             + A[8] * (tuple1[7] ** A[16])
        f1 = f1 + 273.15
        f = f + (f1 - tuple1[8]) ** 2
    f = (f / len(findthem)) ** 0.5

    return f


def boiling_point(A, tuple1):

    """
    calculates the boiling points for a a given Hosoya index, path numbers, methyl index and set of parameters.
    """

    f1 = A[0] \
         + A[1] * (tuple1[0] ** A[9]) \
         + A[2] * (tuple1[1] ** A[10]) \
         + A[3] * (tuple1[2] ** A[11]) \
         + A[4] * (tuple1[3] ** A[12]) \
         + A[5] * (tuple1[4] ** A[13]) \
         + A[6] * (tuple1[5] ** A[14]) \
         + A[7] * (tuple1[6] ** A[15]) \
         + A[8] * (tuple1[7] ** A[16])
    f1 = f1 + 273.15

    return f1


def find_bond_extremities(button, i, j, bond, nbond):

    """
    For a given bond, this function appends the position indexes of the bound atoms to the bond vector, and increments
    the number of bonds in the molecule (nbond) by 1. Doesn't do anything if the bond is not neighbour to an atom
    (avoids double counting "long" bonds, i. e. when 2 or more bonds are next to each other).
    """

    a = i
    b = j
    if button[i][j]['text'] == '-' and button[i][j - 1]['text'] == 'C':
        nbond = nbond + 1
        a = i
        b = j
        while button[a][b]['text'] != 'C':
            b = b + 1
        bond.append([[i, j - 1], [a, b]])
    elif button[i][j]['text'] == '|' and button[i - 1][j]['text'] == 'C':
        nbond = nbond + 1
        a = i
        b = j
        while button[a][b]['text'] != 'C':
            a = a + 1
        bond.append([[i - 1, j], [a, b]])

    return bond, nbond


def bond_index_creator(button, ndim):

    """
   This function returns the list matrix , which contains the coordinates of the atoms at the extremity of each bond.
    """

    bond = [[[]]]
    nbond = 0
    for i in range(ndim):
        for j in range(ndim):
            if button[i][j]['text'] == '-' or button[i][j]['text'] == '|':
                bond, nbond = find_bond_extremities(button, i, j, bond, nbond)

    return bond, nbond


def match_counter(table, nbond, bond):

    """
    This function returns the number of matches
    """

    nmatches = nbond + 1
    for i in range(2 ** nbond):
        flag = 0
        for j in range(nbond):
            flag = flag + table[i][j]
        if (flag > 1):
            count = match_or_nomatch(i, table, nbond, bond)
            if count == 'yes':
                nmatches = nmatches + 1

    return nmatches


def graph_to_descriptors(button, ndim):

    """
    Generally: returns all relevant graph theory based descriptors for the given graph.
    In details: Stores in a list for each bond the coordinates of the atoms at its extremities in a vector bond (Fonction
    bond_index_creator). Then calculates the Hosoya index in two steps: (1) generates a list of all possible set
    of selected bonds using the function generate_table, and (2) counts the number of matches in that list with the
    function match_counter. Then calculates the methyl index in two step: (1) stores the coordinates of all atoms using
    the function build_Cindex, (2) calculates the methyl index using the function mymethylindex. Finally, calculates
    the path numbers stored in a vector (pathvector[i] corresponds to the path number for atoms separated by i bonds)
    using the function mypathnum.
    """

    bond, nbond = bond_index_creator(button, ndim)
    table = generate_table(nbond)
    nmatches = match_counter(table, nbond, bond)
    Cindex, ncarb = build_Cindex(button, ndim)
    distancematrix = distance_matrix_builder(ncarb, bond, nbond, Cindex)
    methylindex = mymethylindex(distancematrix, ncarb)
    pathvector = path_number_calculator(distancematrix, ncarb)

    return nmatches, pathvector, methylindex


def match_or_nomatch(i, table, nbond, bond):

    """
    Check whether the bonds selected in the vector table[i] actually constitute a match (returns 'yes') or
    not (returns 'no').
    Returns
    """

    count = 'yes'
    for j in range(nbond):
        if table[i][j] == 1:
            for k in range(j + 1, nbond):
                if (
                        table[i][k] == 1
                        and bond[j + 1][0][0] == bond[k + 1][0][0]
                        and bond[j + 1][0][1] == bond[k + 1][0][1]
                ):
                    # Then this is not a match
                    count = 'no'
                elif (
                        table[i][k] == 1
                        and bond[j + 1][0][0] == bond[k + 1][1][0]
                        and bond[j + 1][0][1] == bond[k + 1][1][1]
                ):
                    # Then this is not a match
                    count = 'no'
                elif (
                        table[i][k] == 1
                        and bond[j + 1][1][0] == bond[k + 1][0][0]
                        and bond[j + 1][1][1] == bond[k + 1][0][1]
                ):
                    # Then this is not a match
                    count = 'no'
                elif (
                        table[i][k] == 1
                        and bond[j + 1][1][0] == bond[k + 1][1][0]
                        and bond[j + 1][1][1] == bond[k + 1][1][1]
                ):
                    # Then this is not a match
                    count = 'no'

    return count


def build_Cindex(button, ndim):

    """
    builds and returns Cindex, a vector containing the coordinates of the carbones drawn on the graphical
    interface (button)
    """

    ncarb = 0
    Cindex = [[]]
    for i in range(ndim):
        for j in range(ndim):
            if button[i][j]['text'] == 'C':
                Cindex.append([i, j])
                ncarb = ncarb + 1

    return Cindex, ncarb


def index_list(list, element):

    """
    Returns in a list the multiple indexes of a given ocurrence from a list
    """

    indxlist = []
    indx = 0
    flag = 'continue'
    while flag != 'stop':
        try:
            if indxlist == []:
                indx = list.index(element)
                indxlist.append(indx)
            else:
                indx = list.index(element, indx + 1, len(list))
                indxlist.append(indx)
        except:
            flag = 'stop'
    return indxlist


def distance_matrix_builder(ncarb, bond, nbond, Cindex):

    """
    returns the distance matrix, i.e. a list of vectors which associates a given atom to the relative position
    (bond-wise) of its neighbours. It is therefore a NxN matrix, where N is the number of atoms.
    """

    distancematrix = []
    for i in range(ncarb):
        distancematrix.append([0] * ncarb)
        for j in range(1, nbond + 1):
            if Cindex[i + 1] == bond[j][0]:
                neighbour = Cindex.index(bond[j][1])
                distancematrix[i][neighbour - 1] = 1
            elif Cindex[i + 1] == bond[j][1]:
                neighbour = Cindex.index(bond[j][0])
                distancematrix[i][neighbour - 1] = 1
    for j in range(1, ncarb):
        for i in range(ncarb):
            neighbours = index_list(distancematrix[i], j)
            for k in neighbours:
                neighboursneighbours = index_list(distancematrix[k], 1)
                for l in neighboursneighbours:
                    if distancematrix[i][l] == 0 and l != i:
                        distancematrix[i][l] = j + 1

    return distancematrix


def path_number_calculator(distancematrix, ncarb):

    """
    Calculates the path numbers by two steps: (1) builds the distance matrix using
    one vector referencing the carbons coordinates, and the other representing the bonds coordinates and that of the
    atoms at their extremities. (2) Counts the relevant numbers of the upper triangle of the distance matrix. Then
    calculates the methyl index also using the function mymethylindex.
    """

    pathvector = []
    for i in range(7):
        pathvector.append(0)
    for i in range(ncarb):
        for j in range(i, ncarb):
            a = distancematrix[i][j]
            if distancematrix[i][j] <= 6:
                pathvector[a] = pathvector[a] + 1

    return pathvector


def training_set_agreement():

    """
    First construct the writes the by default data set and by default parameters in the appropriate files IF ANY SUCH
    FILE DOES NOT EXIST, then using the current parameter and data set plots a list of calc. vs exp. couple of points
    for each data point present in the data set file using the function bpdumbis.
    """

    try:
        open('parameters.txt')
    except IOError:
        pm = open('parameters.txt', 'w+')
        pm.write('847.41474 221.61698 -1182.20853 0.00125 -3.02445 -2.16070 -0.56366 -2.10575 -9.61075\n')
        pm.write('0.49420 0.03689 3.39724 0.93751 1.01631 1.38233 0.5695 0.19907')
        pm.close()
    try:
        open('database.txt')
    except IOError:
        build_default_dataset()
    pm = open('parameters.txt', 'r')
    AB = pm.readlines()
    A = AB[0].split()
    B = AB[1].split()
    pm.close()
    for i in range(len(A) - 1):
        A[i] = float(A[i])
        B[i] = float(B[i])
    A[len(A) - 1] = float(A[len(A) - 1])
    for i in range(len(B)):
        A.append(B[i])
    training_set_calculator(A)


def training_set_calculator(A):
    """
     For each point in the data set, calculates the boiling point and writes the couple (calculated temperature +
     experimental temperature) in the file 'training-set.txt', which can then be plot by other program (plot not
     available in this program at the moment)
    """

    db = open('database.txt', 'r')
    findthem = db.readlines()
    file1 = open('training-set.txt', 'w+')
    for i in range(len(findthem)):
        tuple1 = findthem[i].split()
        for j in range(len(tuple1)):
            tuple1[j] = float(tuple1[j])
        f1 = (
                A[0] + A[1] * (tuple1[0] ** A[9])
                + A[2] * (tuple1[1] ** A[10])
                + A[3] * (tuple1[2] ** A[11])
                + A[4] * (tuple1[3] ** A[12])
                + A[5] * (tuple1[4] ** A[13])
                + A[6] * (tuple1[5] ** A[14])
                + A[7] * (tuple1[6] ** A[15])
                + A[8] * (tuple1[7] ** A[16])
        )
        f1 = f1 + 273.15
        file1.write(str(f1) + ' ' + str(tuple1[8]) + '\n')
    file1.close()
    db.close()

    return


def mymethylindex(distancematrix, ncarb):
    """
    Calculates the methyl index by checking the relevant atoms in the distance matrix.
    """

    methylindex = 0
    for i in range(ncarb):
        flag = 0
        for j in range(ncarb):
            if distancematrix[i][j] == 1:
                memvar = j
                flag = flag + 1
        if flag == 1:
            flag = 0
            for j in range(ncarb):
                if distancematrix[memvar][j] == 1:
                    flag = flag + 1
            if flag >= 3:
                methylindex = methylindex + 1

    return methylindex


def generate_table(nbond):

    """
    Generates a list of all possible set of selected bonds in the molecule
    """

    table = [[]]
    i = nbond
    for j in range(2 ** nbond):
        table.append([])

    while i > 0:
        n = 0
        for j in range(2 ** nbond):
            if j > 0 and j % 2 ** (i - 1) == 0 and n == 0:
                n = 1
            elif j > 0 and j % 2 ** (i - 1) == 0 and n == 1:
                n = 0
            if n == 0:
                table[j].append(0)
            elif n == 1:
                table[j].append(1)

        i = i - 1
    return table


'''
MAIN PROGRAM (mostly graphical settings)
'''

root = Tk()
indexi = [0, 0, 0, 0]
indexj = [0, 0, 0, 0]
button = [[]]
ndim = 30
for i in range(ndim):
    button.append([])
    for j in range(ndim):
        button[i].append(0)

button[2][2] = 69

myFont = font.Font(size=8)
for i in range(ndim):
    for j in range(ndim):
        button[i][j] = Button(root, padx=12, pady=4, text='  ', command=lambda a=i, b=j: my_click(a, b))
        button[i][j]['font'] = myFont
        button[i][j].grid(row=i, column=j, sticky=NSEW)

for i in range(ndim):
    button[i][0].configure(text='M', bg='black', state=DISABLED)
    button[0][i].configure(text='M', bg='black', state=DISABLED)
    button[i][ndim - 1].configure(text='M', bg='black', state=DISABLED)
    button[ndim - 1][i].configure(text='M', bg='black', state=DISABLED)

label1 = Label(root, text='')
label1.grid(row=ndim + 1, column=int(ndim / 2))
screxecuter = Button(root, padx=3, pady=3, text='Boil. Point', command=lambda: graph_to_boiling_point(button, ndim))
screxecuter.grid(row=ndim + 2, column=int(ndim / 2) - 9, columnspan=2)
scrfitter = Button(root, padx=3, pady=3, text='add to database', command=lambda: append_to_database(button, ndim))
scrfitter.grid(row=ndim + 2, column=int(ndim / 2) + 6, columnspan=6)
tempentry = Entry(root, width=20)
tempentry.insert(1, 'insert boiling point (K)')
tempentry.grid(row=ndim + 1, column=int(ndim / 2) + 6, columnspan=6)
scrtext = Label(root, text='')
scrtext.grid(row=ndim + 3, column=int(ndim / 2) - 10, columnspan=6)
getparameters = Button(root, text='get new set of parameters', command=learn_from_new_set)
getparameters.grid(row=ndim + 2, column=int(ndim / 2) + 10, columnspan=6)
printparameters = Button(root, text='print calc/exp agreement', command=training_set_agreement)
printparameters.grid(row=ndim + 3, column=int(ndim / 2) + 10, columnspan=6)
root.mainloop()
