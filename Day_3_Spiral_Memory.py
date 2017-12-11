def run_Spiral_Memory_1(input):

    if (input**0.5) == int((input**0.5)):
        square_size = int((input**0.5))
    else:
        square_size = int((input**0.5)) + 1

    if square_size%2 == 0.0:
        square_size += 1

    tmp = []
    right_bottom = square_size**2
    dist = right_bottom
    for i in xrange(4):
        dist -= (square_size-1)
        tmp.append(abs(dist+square_size//2 - input))
    print 'The solution to ' + str(input) + ' spreadsheet is: \n' + str(min(tmp)+square_size//2)


def run_Spiral_Memory_2(input):

    def next_position(previous_position, direction_delta):
        return tuple(map(sum, zip(previous_position, direction_delta)))

    def fill_in(position, center=False):
        x, y = position
        filled_in.add(position)
        if center:
            grid[x][y] = 1
            return 1

        direction_deltas = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        value_i = 0
        for i in range(len(direction_deltas)):
            direction_delta = direction_deltas[i]
            position_tmp = next_position(position, direction_delta)
            if position_tmp in filled_in:
                value_i+=grid[position_tmp[0]][position_tmp[1]]
        grid[x][y] = value_i
        return value_i

    def position_is_ok(position):
        if position in filled_in:
            return False
        if not all(coord in range(square_size) for coord in position):
            return False
        return True

    if (input**0.5) == int((input**0.5)):
        square_size = int((input**0.5))
    else:
        square_size = int((input**0.5)) + 1

    if square_size%2 == 0.0:
        square_size += 1

    grid = []
    for i in range(square_size):
        grid.append(['0'] * square_size)

    # First value into grid
    filled_in = set()
    posi_origin = (square_size//2, square_size//2)
    value = fill_in((posi_origin[0],posi_origin[1]), True)
    direction_deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    num_directions = len(direction_deltas)
    previous_direction = 0
    previous_position = posi_origin


    while value < input:
        for i in range(num_directions):
            next_direction = (i) % num_directions
            direction_delta = direction_deltas[next_direction]
            position = next_position(previous_position, direction_delta)
            if position_is_ok(position) and ((next_direction == previous_direction) or (next_direction == (1 + previous_direction)% num_directions)):
                value = fill_in(position)
                previous_position = position
                previous_direction = next_direction

    print 'The solution to ' + str(input) + ' spreadsheet is: \n' + str(value)

if __name__ == '__main__':

    input = 361527

    run_Spiral_Memory_1(input)
    run_Spiral_Memory_2(input)
