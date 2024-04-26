## VR505019 - KHOI MAI TIEU
## VR501305 - PEDRO ALONSO LOPEZ TORRES

import sys

def makechange(total):
    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    coins, remaining = sorted(denominations, reverse=True), total
    pieces_used = [0] * len(denominations)

    for i, coin in enumerate(coins):
        coins_used = remaining // coin
        pieces_used[i] = coins_used
        remaining -= coins_used * coin

    total_pieces = sum(pieces_used)

    return total_pieces, reversed(pieces_used)

if __name__ == "__main__":

    # Read input file name from command line arguments

    # If no arguments are provided, use the default input file name are conio1/example.in.txt
    if len(sys.argv) == 1:
        input_file_name = './conio1/example.in.txt'
    # If one argument is provided, use the provided argument as the input file name
    elif len(sys.argv) == 2:
        input_file_name = sys.argv[1]
    else:
        print("Usage: python conio1-sol.py [input-file-path.txt]")
        sys.exit(1)

    output_file_name = input_file_name.replace(".txt", "_output.txt")

    # Read input from input file and write the result to output file
    with open(input_file_name, 'r') as input_file:
        with open(output_file_name, 'w') as output_file:
            # Read the number of test cases
            n = int(input_file.readline())
            for i in range(n):
                # Read the total amount and pass to the function
                total = int(input_file.readline())
                total_pieces, pieces_used = makechange(total)
                output_file.write(str(total_pieces) + '\n')
                output_file.write(' '.join(map(str, pieces_used)) + '\n')
