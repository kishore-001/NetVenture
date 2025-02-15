import csv

def process_logic_operations(input_file):

  results = []
  
  # Open input.csv
  with open(input_file, mode='r') as infile:
    csvreader = csv.reader(infile)
    next(csvreader)

    # Read input from input.csv
    for row in csvreader:
        input1 = int(row[0])
        input2 = int(row[1])
        input3 = int(row[2])
        input4 = int(row[3])

        and_output1 = input1 & input2 # First AND operation
        and_output2 = input3 & input4 # Second AND operation

        final_output = and_output1 | and_output2 # Final OR operation

        results.append(str(final_output))
    
    return ''.join(results)

input_file = 'input.csv'
output = process_logic_operations(input_file)

print(output)