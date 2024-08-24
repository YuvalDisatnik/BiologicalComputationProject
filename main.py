# By: Benjamin Boshoer & Yuval Disatnik
# URL to the GitHub repository: https://github.com/YuvalDisatnik/BiologicalComputationProject.git
import pandas

# Define pairs of states that differ only in one digit, i.e. there is a change only in one activator/inhibitor.
# These pairs represent the states changes we would like to check
# in order to determine whether the given regular condition is monotonic or not.
states_pairs = [('00','10'), ('01','00'), ('11','10'), ('01','11'),
                ('10','20'), ('02','01'), ('12','11'), ('11','21'),
                ('02','12'), ('21','20'), ('12','22'), ('22','21')]

############## dont know if neccesary to divide ##############################3
states_pairs_should_not_increase = [('00','10'), ('00','01'), ('10','11'), ('01','11'),
                ('10','20'), ('01','02'), ('11','12'), ('11','21'),
                ('02','12'), ('20','21'), ('12','22'), ('21','22')]
###############################################################################

# Define a function to check if a regular condition is monotonic,
# by checking the validity of the values in all the states pairs
def isRegularConditionMonotonic(regular_condition):
    print(f"checking row: {regular_condition}")
    for (state1, state2) in states_pairs:
        print(f"checking monotonicity between states: {state1} and {state2}")
        # Verify the states exists in the regular condition's row before comparing
        if state1 in regular_condition.index and state2 in regular_condition.index:
            # Compare the columns: If col2 > col1, then it must be consistent with activation/inhibition
            print(f"comparing values - in {state1}: {regular_condition[state1]}, in {state2}: {regular_condition[state2]}")
            if regular_condition[state1] > regular_condition[state2]:
                print("returning not monotonic")
                return False
    print("returning monotonic")
    return True


def main():
    # Data's structure in the csv file:
    # Every row is a regular condition (0-17)
    # Every column is a state of activators-inhibitors - left digit is the number of active activators,
    # right digit is the number of active inhibitors

    # Extract the data from the csv file (table d from the project)
    data = pandas.read_csv('biocomp_data.csv')
    """for regular_condition in data:
        print(regular_condition)"""

    # Declare a list to hold all monotonic regular conditions
    monotonic_regular_conditions = []

    # Iterate through all the regular conditions, check for each one if monotonic
    for i, row in data.iterrows():
        if(isRegularConditionMonotonic(row)):
            monotonic_regular_conditions.append(i)
    print(monotonic_regular_conditions)



if __name__ == '__main__':
    main()