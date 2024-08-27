# By: Benjamin Boshoer & Yuval Disatnik
# URL to the GitHub repository: https://github.com/YuvalDisatnik/BiologicalComputationProject.git
import pandas
import csv
import matplotlib.pyplot as plt

# Define pairs of states that differ only in one digit, i.e. there is a change only in one activator/inhibitor.
# These pairs represent the states changes we would like to check
# in order to determine whether the given regular condition is monotonic or not.
states_pairs = [('00','10'), ('01','00'), ('11','10'), ('01','11'),
                ('10','20'), ('02','01'), ('12','11'), ('11','21'),
                ('02','12'), ('21','20'), ('12','22'), ('22','21')]


# Define a function to check if a regular condition is monotonic,
# by checking the validity of the values in all the states pairs
def isRegularConditionMonotonic(regular_condition):
    for (state1, state2) in states_pairs:
        # Verify the states exists in the regular condition's row before comparing
        if state1 in regular_condition.index and state2 in regular_condition.index:
            # Compare the columns: If col2 > col1, then it must be consistent with activation/inhibition
            if regular_condition[state1] > regular_condition[state2]:
                return False
    return True

def saveAllMonotonic(monotonic_list):
    # Open biocomp_data_all for reading
    with open('biocomp_data_all.csv', mode='r', newline='') as source_file:
        reader = csv.reader(source_file)
    
        # Open the destination CSV file for writing
        with open('monotonic_conditions.csv', mode='w', newline='') as destination_file:
            writer = csv.writer(destination_file)
            
            # Copy the specific row from the source to the destination
            for index, row in enumerate(reader):
                if index-1 in monotonic_list:  # For example, copying the third row (index 2)
                    writer.writerow(row)
    
    print("monotonic_conditions.csv created!")
                    
def plotTable():
    columns = ['Reg.Con.','00','10','20','01','11','21','02','12','22']
    with open('monotonic_conditions.csv', mode='r', newline='') as source_file:
        reader = csv.reader(source_file)
        rows = [item for item in reader]

    counter = 0
    for row in rows:
        row.insert(0,counter)
        counter+=1
    
    rows.insert(0, columns)

    # Step 2: Create the cell colors list of lists based on the data
    cell_colors = [[color_cell(value) for value in row] for row in rows]

    # Step 3: Create a figure and add a table to it
    fig, ax = plt.subplots(figsize=(10,5))
    ax.axis('off')  # Hide the axes

    # Add the table
    the_table = ax.table(cellText=rows,
                        cellColours=cell_colors,
                        cellLoc='center',
                        loc='center')

    # Step 4: Customize the table appearance (optional)
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)
    the_table.scale(1.2, 1.2)

    # Show the plot
    plt.show()

# Step 1: Define a color function to determine cell color
def color_cell(value):
    if value == '1':
        return 'red'
    else:
        return 'white'  # Default color    


def main():
    # Data's structure in the csv file:
    # Every row is a regular condition (0-17)
    # Every column is a state of activators-inhibitors - left digit is the number of active activators,
    # right digit is the number of active inhibitors

    # Extract the data from the csv file (table d from the project)
    data = pandas.read_csv('biocomp_data_all.csv')

    # Declare a list to hold all monotonic regular conditions
    monotonic_regular_conditions = []

    # Iterate through all the regular conditions, check for each one if monotonic
    for i, row in data.iterrows():
        if(isRegularConditionMonotonic(row)):
            if i == 0 or i == 511:
                continue
            monotonic_regular_conditions.append(i)

    saveAllMonotonic(monotonic_regular_conditions)
    plotTable()


if __name__ == '__main__':
    main()
