def makechange(total):
    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    coins, remaining = sorted(denominations, reverse=True), total
    pieces_used = [0] * len(denominations)

    for i, coin in enumerate(coins):
        coins_used = remaining // coin
        pieces_used[i] = coins_used
        remaining -= coins_used * coin

    total_pieces = sum(pieces_used)
    
    # Adjusting the number of 1000 denomination coins used
    pieces_used[-1] += remaining // 1000

    return total_pieces, reversed(pieces_used)

# Read input from 'example.in.txt' and write the result to 'out.txt'
with open('conio1/example.in.txt', 'r') as input_file:
    with open('conio1/out.txt', 'w') as output_file:
        n = int(input_file.readline())
        for i in range(n):
            total = int(input_file.readline())
            total_pieces, pieces_used = makechange(total)
            output_file.write(str(total_pieces) + '\n')
            output_file.write(' '.join(map(str, pieces_used)) + '\n')