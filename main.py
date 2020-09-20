# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: Tom Woodburn Tetromino Coursewok
#
# Last updated: 07/12/17
# ####################################################


def Tetris(target):
    solution = [
        [(0,0) for a in range(len(target))]  # Line 1
        for b in range(len(target[0]))  # Line 2
    ]

    # Line 1: creating an empty tuple of (0,0) in the solution. The solution is displayed as a list of lists.
    # 'a' is a list of the same range as the number of lists in the target matrix
    # (i.e. the number of rows in solution matrix)
    # Line 2: 'b' represents an element within the list of 'a'. Same as before there are equal number of
    # 'element-wise' lists in the solution matrix as there are in the target matrix.
    # (i.e. the number of columns in solution matrix)

    global TetrominoNumber  # global variable, can be referenced by every function
    TetrominoNumber = 1  # Value of TetrominoNumber, which counts the number of Tetrominos placed starts at 1

    def Array1(M, A, S, a, b):  # see below for explanation Line 1
        try:  # Line 2
            if M[b + 0][a + 1] == 1 and S[b + 0][a + 1] == (0, 0):  # Line 3
                A[0][3] = 1 # Line 4
        except IndexError:  # Line 5
            pass  # Line 6

    #M: Target Matrix - filled with 0s and 1s making up the tetromino puzzle
    #A: 5 rows, 4 columns array (home co-ord 0,2) which reads each square in M, checking the state of the 20 surrounding squares 
    #A cont: (in both target Matrix, M & checking if empty or filled in Solution Matrix, S)
    #S: Solution Matrix is constructed same size as target matrix, starts as matrix of empty tuples (0,0). Algorithm checks to see if
    #S cont: corresponding square from target matrix is empty or full in Solution matrix & places a tetromino (with correct ShapeID accordingly).

    # e.g Line 1: function for inputting tetris shapes around a home coordinate. The home co-ordinate is at (0,2) inside
    # a 5x4 array in the target matrix. From (0,2) you check the value of surrounding co-ordinates in M.
    # Line 2: A is 5x4 array, with home co-ordinate (0,2)
    # Line 3: Home co-ordinate has position (a,b) here it is (0,2). In given target if (a+1,b) is a target square (==1)
    # and equivalent square in solution matrix is the the tuple (0,0) ...
    # M[b+0][a+1] is a list of lists e.g. [list number] [element within list] - I am calling it a matrix
    # Line 4: if true, assign that co-ord in General Array (A) as 1
    # Line 5: "Sequence subscript is out of range", if M[b+0][a+1] == 0 (not a target square) or that square is
    # not in the target matrix
    # Line 6: null operation, nothing happens (pass)

    # Below, this is continued for the 12 co-ordinates around position (0,2). In which the 19 ShapeIDs can be placed.

    def Array2(M, A, S, a, b):
        try:
            if M[b + 0][a + 2] == 1 and S[b + 0][a + 2] == (0, 0):
                A[0][4] = 1
        except IndexError:
            pass

    def Array3(M, A, S, a, b):
        try:
            if M[b + 0][a + 3] == 1 and S[b + 0][a + 3] == (0, 0):
                A[0][5] = 1
        except IndexError:
            pass

    def Array4(M, A, S, a, b):
        try:
            if M[b + 1][a - 2] == 1 and S[b + 1][a - 2] == (0, 0):
                A[1][0] = 1
        except IndexError:
            pass

    def Array5(M, A, S, a, b):
        try:
            if M[b + 1][a - 1] == 1 and S[b + 1][a - 1] == (0, 0):
                A[1][1] = 1
        except IndexError:
            pass

    def Array6(M, A, S, a, b):
        try:
            if M[b + 1][a + 0] == 1 and S[b + 1][a + 0] == (0, 0):
                A[1][2] = 1
        except IndexError:
            pass

    def Array7(M, A, S, a, b):
        try:
            if M[b + 1][a + 1] == 1 and S[b + 1][a + 1] == (0, 0):
                A[1][3] = 1
        except IndexError:
            pass

    def Array8(M, A, S, a, b):
        try:
            if M[b + 1][a + 2] == 1 and S[b + 1][a + 2] == (0, 0):
                A[1][4] = 1
        except IndexError:
            pass

    def Array9(M, A, S, a, b):
        try:
            if M[b + 2][a - 1] == 1 and S[b + 2][a - 1] == (0, 0):
                A[2][1] = 1
        except IndexError:
            pass

    def Array10(M, A, S, a, b):
        try:
            if M[b + 2][a + 0] == 1 and S[b + 2][a + 0] == (0, 0):
                A[2][2] = 1
        except IndexError:
            pass

    def Array11(M, A, S, a, b):
        try:
            if M[b + 2][a + 1] == 1 and S[b + 2][a + 1] == (0, 0):
                A[2][3] = 1
        except IndexError:
            pass

    def Array12(M, A, S, a, b):
        try:
            if M[b + 3][a + 0] == 1 and S[b + 3][a + 0] == (0, 0):
                A[3][2] = 1
        except IndexError:
            pass

    def ShapePlacing(a, b, T, S):
        global TetrominoNumber
        A = [
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        # Above, in the functions 'Array'n'(M, A, S, a, b):' I created a method to test the surrounding co-ordinates
        # to position (0,2) in the array A.  In the function 'ShapePlacing' I define (0,2) as the home co-ordinate
        # around which shapes will be tested against the target matrix.
        # A[0][2] is always a 1 value

        #print('Testing ShapeID at co-ordinate in target matrix', x, y)
        Array1(T, A, S, a, b)
        Array2(T, A, S, a, b)
        Array3(T, A, S, a, b)
        Array4(T, A, S, a, b)
        Array5(T, A, S, a, b)
        Array6(T, A, S, a, b)
        Array7(T, A, S, a, b)
        Array8(T, A, S, a, b)
        Array9(T, A, S, a, b)
        Array10(T, A, S, a, b)
        Array11(T, A, S, a, b)
        Array12(T, A, S, a, b)

        # Calling the defined functions for positions adjacent to home co-ordinate [0][2]
        # Then calling the parameters created outside of the function. These are target Matrix, The General Array
        # Solution matrix, and the co-ordinates x and y

        if A[0][3] == 1 and A[1][2] == 1 and A[1][3] == 1:  # Line 1
            S[b][a] = S[b][a + 1] = S[b + 1][a] = S[b + 1][a + 1] = (1, TetrominoNumber)  # Line 2
            TetrominoNumber += 1  # Line 3

            # Line 1: The home co-ordinate has the position A[0][2], for shapeID 1, it checks the neighbouring
            # 3 co-ordinates to see if they are also 1s in the target matrix.
            # Line 2: S[b][a] represents the home co-ordiantes location in the solution matrix, all 4 co-ordinates
            # of this shape belong to the ShapeID 1. '=(1, TetrominoNumber)' this labels the ShapeID as '1',
            # use of global variable TetrominoNumber
            # Line 3: += 1 adds +1 to the TetrominoNumber analysed next

            # This method is continued for all 19 shapeIDs

        elif A[1][2] == 1 and A[2][2] == 1 and A[3][2] == 1:
            S[b][a] = S[b + 1][a] = S[b + 2][a] = S[b + 3][a] = (2, TetrominoNumber)
            TetrominoNumber += 1

        elif A[0][3] == 1 and A[0][4] == 1 and A[0][5] == 1:
            S[b][a] = S[b][a + 1] = S[b][a + 2] = S[b][a + 3] = (3, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][2] == 1 and A[2][2] == 1 and A[2][3] == 1:
            S[b][a] = S[b + 1][a] = S[b + 2][a] = S[b + 2][a + 1] = (4, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][0] == 1 and A[1][1] == 1 and A[1][2] == 1 and a >= 2:
            S[b][a] = S[b + 1][a - 2] = S[b + 1][a - 1] = S[b + 1][a] = (5, TetrominoNumber)
            TetrominoNumber += 1

            # Using 'and a>= 2' as 2 of the 4 blocks in 'Shape ID: 5' have co-ordinates in the columns left of home
            # co-ordinate (0,2), these are (1,0) and (1,1). When the function 'ShapePlacing' is checking co-ordinates in
            # the first 2 columns of the target matrix, 'and a>=2' prevents it inputting Shape ID 5 in the solution
            # matrix. As the target and solution matrices are displayed as arrays (list of lists), if 'and a>=2' is not
            # used, a can be negative. In line [189] when '=S[b+1][a-2]' and '=S[b+1][a-1], if 'a' were 0 or 1, '[a-1]'
            # '[a-2] would be negative.  These two co-ordinates of 'shapeID 5' would be 'wrapped'
            # around the list and displayed in the two last columns. Not inputting 'and a>=2' creates incorrectly
            # labelled ShapeIDs, increases the missing blocks and increases the excess blocks.

        elif A[0][3] == 1 and A[1][3] == 1 and A[2][3] == 1:
            S[b][a] = S[b][a + 1] = S[b + 1][a + 1] = S[b + 2][a + 1] = (6, TetrominoNumber)
            TetrominoNumber += 1

        elif A[0][3] == 1 and A[0][4] == 1 and A[1][2] == 1:
            S[b][a] = S[b][a + 1] = S[b][a + 2] = S[b + 1][a] = (7, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][2] == 1 and A[2][1] == 1 and A[2][2] == 1 and a >= 1:
            S[b][a] = S[b + 1][a] = S[b + 2][a - 1] = S[b + 2][a] = (8, TetrominoNumber)
            TetrominoNumber += 1

        elif A[0][3] == 1 and A[0][4] == 1 and A[1][4] == 1:
            S[b][a] = S[b][a + 1] = S[b][a + 2] = S[b + 1][a + 2] = (9, TetrominoNumber)
            TetrominoNumber += 1

        elif A[0][3] == 1 and A[1][2] == 1 and A[2][2] == 1:
            S[b][a] = S[b][a + 1] = S[b + 1][a] = S[b + 2][a] = (10, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][2] == 1 and A[1][3] == 1 and A[1][4] == 1:
            S[b][a] = S[b + 1][a] = S[b + 1][a + 1] = S[b + 1][a + 2] = (11, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][2] == 1 and A[1][3] == 1 and A[2][2] == 1:
            S[b][a] = S[b + 1][a] = S[b + 1][a + 1] = S[b + 2][a] = (12, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][1] == 1 and A[1][2] == 1 and A[1][3] == 1 and a >= 1:
            S[b][a] = S[b + 1][a - 1] = S[b + 1][a] = S[b + 1][a + 1] = (13, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][1] == 1 and A[1][2] == 1 and A[2][2] == 1 and a >= 1:
            S[b][a] = S[b + 1][a - 1] = S[b + 1][a] = S[b + 2][a] = (14, TetrominoNumber)
            TetrominoNumber += 1

        elif A[0][3] == 1 and A[0][4] == 1 and A[1][3] == 1:
            S[b][a] = S[b][a + 1] = S[b][a + 2] = S[b + 1][a + 1] = (15, TetrominoNumber)
            TetrominoNumber += 1

        elif A[0][3] == 1 and A[1][1] == 1 and A[1][2] == 1 and a >= 1:
            S[b][a] = S[b][a + 1] = S[b + 1][a - 1] = S[b + 1][a] = (16, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][2] == 1 and A[1][3] == 1 and A[2][3] == 1:
            S[b][a] = S[b + 1][a] = S[b + 1][a + 1] = S[b + 2][a + 1] = (17, TetrominoNumber)
            TetrominoNumber += 1

        elif A[0][3] == 1 and A[1][3] == 1 and A[1][4] == 1:
            S[b][a] = S[b][a + 1] = S[b + 1][a + 1] = S[b + 1][a + 2] = (18, TetrominoNumber)
            TetrominoNumber += 1

        elif A[1][1] == 1 and A[1][2] == 1 and A[2][1] == 1 and a >= 1:
            S[b][a] = S[b + 1][a - 1] = S[b + 1][a] = S[b + 2][a - 1] = (19, TetrominoNumber)
            TetrominoNumber += 1

    for x in range(len(target)):  # Line 1
        for y in range(len(target[x])):  #line 2
            if solution[x][y] != (0, 0) or target[x][y] == 0:  #Line 3
                continue  # Line 4
            else:  # Line 5
                ShapePlacing(y, x, target, solution)  # Line 6
                continue  #Line 7

    #print(solution)
    return solution

    # Line 1: For x co-ordinates within the Target Matrix's row length [length of list]
    # Line 2: For y co-ordinates within the Target Matrix's column length [index of element within list]
    # Line 3: For the same co-ordinates x and y in the solution matrix, if the values are not equal to an
    # empty tuple or if they are not values of 1 within the target matrix (i.e. not target positons)
    # Line 4: 'Continue', continues with the next cycle of the nearest enclosing loop
    # Line 5: else: if line 3 is false
    # Line 6: When positions in the target matrix are 1, Use the 'ShapePlacing'  function to choose
    # an appropriate shapeID to place in the Solution matrix.

