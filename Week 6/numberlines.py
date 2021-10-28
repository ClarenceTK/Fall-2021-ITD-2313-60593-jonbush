input_filename = input('Enter input file name: ')
output_filename = input('Enter output file name: ')

with open(input_filename, 'r') as f, open(output_filename, 'w') as w:
    number = 0
    for line in f:
        number += 1
        w.write('{:>4}> {}'.format(number, line))