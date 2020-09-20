# Tetromino_Puzzle
The Tetriling Puzzle. 

Description: The Computing Tetromino Coursework challenged me to create an algorithm that scanned a Target Matrix (recognising which positions were 0s, and which were 1s) and then filled a same-sized Solution Matrix with Tetris tetromino pieces maximising the accuracy in matching the Target Matrix. The algorithm was assessed on the accuracy of puzzle placement and it's computational runtime. 

![Tetriling Puzzle: Target & Solution Matrix](https://github.com/TomWoodburn/Tetromino_Puzzle/blob/master/Target%20%26%20Solution%20Matrices/10x10%20Matrix%2C%2088pct%20Placement%20Accuracy.png)
Above: The visualisation of the Target and Solution Matrix after runing "performance_test_v2.py". For a 10x10 Matrix, 88% of the Target Matrix is covered by Tetris Pieces Solution, the runtime was 0.00013 seconds. 

Three files required to run the tetris puzzle solving algorithm and visualise the result using MatPlotLib

File One: "Main.py"

Tetris puzzle solving algorithm developed in this file (within the Tetris(target) function). 

Inside the function Tetris(target), the algorithm: 
1. defines a solution matrix of the same size as the target matrix
2. 2 creates a neighbouring matrix (4 rows, 5 columns), from which all 19 tetris shapes can be compared against the Target Matrix & if well-fitting, placed into the Solution Matrix.
3. One of 19 tetris shapes is either placed, or no shape is placed. Then, the algorithm traverses to the next position in the matrix. 

File Two: "performance_test_v2.py"

Developed by the lecturers. 
This file runs the function Tetris(target) from "Main.py"; measuring it's runtime and accuracy of tetris piece positioning then displays the MatPlotLib visualisation. 

File Three: "Utils.py"

Developed by the lecturers. 
Backend functionality for the running of the algorithm in "Main.py"
