## Biological Computation - Final Project

We wrote a computer program in Python ('main.py') that finds all the monotonic regulation conditions of the reasoning engine.
The data was taken from Table D in the project assignment and was inserted into a CSV file ('biocomp_data.csv').

The program checks each regulation condition and determines whether it is monotonic or not, according to these conditions:

1. The presence of more activators (or fewer inhibitors) should not decrease the output
2. The presence of more inhibitors (or fewer activators) should not increase the output.

### How to run this program
First clone this repository to your machine in your desired folder

```bash
git init
git clone https://github.com/YuvalDisatnik/BiologicalComputationProject.git
```

You will need to create a virtual enviroment and download the needed dependecies.\
In the same folder of your project, type:
```bash
python -m venv myvenv
source myvenv/bin/activate

pip install requirements.txt
```
And finally run the program
```python
python main.py
```

~The output will be a list of row indices corresponding to the monotonic regulation conditions.~
