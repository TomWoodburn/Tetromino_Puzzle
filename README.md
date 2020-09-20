# Tetromino_Puzzle
The Tetriling Puzzle. 

Description: The Computing Tetromino Coursework challenged me to create an algorithm that returned a solution of tetromino pieces
to fill a specified sized polyomino matrix (matrix sizes: 10x10, 100x100, 1000x1000) 
Explain better here: 

![Tetriling Puzzle: Target & Solution Matrix](https://github.com/TomWoodburn/Tetromino_Puzzle/blob/master/Target%20%26%20Solution%20Matrices/10x10%20Matrix%2C%2088pct%20Placement%20Accuracy.png)

Three files required to run the tetris puzzle solving algorithm and visualise the result using MatPlotLib

File One: "Main.py"

Tetris puzzle solving algorithm developed in this file (within the Tetris(target) function). 

Inside the function Tetris(target), my algorithm: defines a solution matrix of the same size as the target matrix; 
creates a neighbouring matrix, from which all the co-ordinates of tetromino shapes can be accessed from a ‘home position’; 
combines co-ordinates within the neighbouring matrix into tetromino shapes 
and then traverses the target matrix and inputs the tetromino shapes into the solution matrix.


File Two: "performance_test_v2.py"

File Three: "Utils.py"
