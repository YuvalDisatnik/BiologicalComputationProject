**Biological Computation - Final Project**

We wrote a computer program in Python ('main.py') that finds all the monotonic regulation conditions of the reasoning engine.
The data was taken from Table D in the project assignment and was inserted into a CSV file ('biocomp_data.csv').

The program checks each regulation condition and determines whether it is monotonic or not, according to these conditions:

1. The presence of more activators (or fewer inhibitors) should not decrease the output
2. The presence of more inhibitors (or fewer activators) should not increase the output.

To run the code, make sure you have the Python script 'main.py' and the CSV file 'biocomp_data.csv' present in the same path. Then, in your terminal (while in the same directory of the files) type the command 'python main.py'.

The output will be a list of row indices corresponding to the monotonic regulation conditions.
