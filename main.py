import itertools
NUM_ROWS = 4
NUM_COLS = 12
NUM_LAYERS = 5

layer_1 = [
    [3, 0, 6, 0, 10, 0, 7, 0, 15, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
layer_2 = [
    [6, 0, 11, 11, 6, 11, 0, 6, 17, 7, 3, 0],
    [15, 0, 0, 14, 0, 9, 0, 12, 0, 4, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
layer_3 = [
    [17, 4, 5, 0, 7, 8, 9, 13, 9, 7, 13, 21],
    [11, 26, 14, 1, 12, 0, 21, 6, 15, 4, 9, 18],
    [22, 0, 16, 0, 9, 0, 5, 0, 10, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
layer_4 = [
    [7, 14, 11, 0, 8, 0, 16, 2, 7, 0, 9, 0],
    [6, 0, 14, 12, 3, 8, 9, 0, 9, 20, 12, 3],
    [2, 13, 9, 0, 17, 19, 3, 12, 3, 26, 6, 0],
    [12, 0, 6, 0, 10, 0, 10, 0, 1, 0, 9, 0],
]
layer_5 = [
    [11, 11, 14, 11, 14, 11, 14, 14, 11, 14, 11, 14],
    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    [4, 4, 6, 6, 3, 3, 14, 14, 21, 21, 9, 9],
    [8, 3, 4, 12, 2, 5, 10, 7, 16, 8, 7, 8],
]

#layers from top down
layers = [layer_1, layer_2, layer_3, layer_4, layer_5]

#combine layers
#if value at layer is zero, go to a layer below and keep going until value is nonzero
def combine_layers(layers):
    combined_layer = []
    for row in range(NUM_ROWS):
        combined_layer.append([])
        for col in range(NUM_COLS):
            combined_layer[row].append([])
            for layer in range(NUM_LAYERS):
                if layers[layer][row][col] != 0:
                    combined_layer[row][col] = layers[layer][row][col]
                    break
    return combined_layer

print(combine_layers(layers))

# get the column sums of a combined layer
def get_column_sums(combined_layer):
    column_sums = []
    for col in range(NUM_COLS):
        column_sums.append(0)
        for row in range(NUM_ROWS):
            column_sums[col] += combined_layer[row][col]
    return column_sums

print(get_column_sums(combine_layers(layers)))

# return true if the column sums are all equal
def win(column_sums):
    for col in range(NUM_COLS):
        if column_sums[col] != column_sums[0]:
            return False
    return True

# rotate a row by a given rotation index
def rotate_row(row, rotation_index):
    return row[rotation_index:] + row[:rotation_index]

# rotate a layer by a given rotation index
def rotate_layer(layer, rotation_index):
    rotated_layer = []
    for row in range(NUM_ROWS):
        rotated_layer.append([])
        rotated_layer[row] = rotate_row(layer[row], rotation_index)
    return rotated_layer

# returns combined layer
def apply_rotation(layers, rotations):
    rotated_layers = []
    for layer in range(NUM_LAYERS):
        rotated_layers.append([])
        rotated_layers[layer] = rotate_layer(layers[layer], rotations[layer])
    return combine_layers(rotated_layers)

# returns true if the rotation is a win
def is_win(layers, rotations):
    return win(get_column_sums(apply_rotation(layers, rotations)))

# find the winning set of rotations
def find_winning_rotations(layers):
    for rotations in itertools.product(range(NUM_COLS), repeat=NUM_LAYERS):
        if is_win(layers, rotations):
            return rotations

rotation = find_winning_rotations(layers)
print(apply_rotation(layers, rotation))