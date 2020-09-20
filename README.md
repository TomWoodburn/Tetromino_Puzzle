# Tetromino_Puzzle
The Tetriling Puzzle. 

Description: The Computing Tetromino Coursework challenged me to create an algorithm that scanned a **Target Matrix** (recognising which positions were 0s, and which were 1s), then generate and fill-in a same-sized **Solution Matrix** with seected Tetris pieces. maximising the accuracy in matching the Target Matrix. The algorithm was assessed on the accuracy of puzzle placement (comparing the Target and Solution matrices) as well as the algorithm runtime at different Matrix sizes (10,100,1000).

![Tetriling Puzzle: Target & Solution Matrix](https://github.com/TomWoodburn/Tetromino_Puzzle/blob/master/Target%20%26%20Solution%20Matrices/10x10%20Matrix%2C%2088pct%20Placement%20Accuracy.png)
<br/>Above: The visualisation of the Target and Solution Matrix after runing "performance_test_v2.py". For a 10x10 Matrix, 88% of the Target Matrix is covered by Tetris Pieces Solution, the runtime was 0.00013 seconds. 

**Included Files**

Three files required to run the tetris puzzle solving algorithm and visualise the result using MatPlotLib

*File One: "Main.py"*

Tetris puzzle solving algorithm developed in this file (within the **Tetris(target)** function). 

Inside the function **Tetris(target)**, the algorithm: 
1. Defines a **Solution Matrix** of the same size as the **Target Matrix**
2. 2 creates a Neighbouring Matrix (4 rows, 5 columns), from which all 19 tetris shapes can be compared against the **Target Matrix** & if well-fitting, placed into the **Solution Matrix**.
3. One of 19 tetris shapes is either placed, if no shaped fit at that position, no shape is placed. Then, the algorithm traverses to the next position in the matrix. 

*File Two: "performance_test_v2.py"*

Developed by the lecturers. 
This file runs the function **Tetris(target)** from "Main.py"; measuring it's runtime and accuracy of tetris piece positioning, the script then displays the MatPlotLib visualisation. 

*File Three: "Utils.py"*

Developed by the lecturers. 
Backend functionality for the running of the algorithm in "Main.py"
