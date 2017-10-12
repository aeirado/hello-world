'''Maze Sotution Algorithm'''

LABYRINTH = [
['x', 'x', 'x', 'x', 'x', '-', 'x', 'x'],
['x', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', '-', 'x', '-', '-', 'x'],
['x', '-', 'x', '-', 'x', 'x', '-', 'x'],
['x', '-', 'x', '-', 'x', '-', '-', 'x'],
['x', '-', '-', '-', '-', '-', '-', 'x'],
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]
GOAL = 'G'
PERSON = '☺'
WALL = 'x'
PATH = '-'
MSG1 = ''


def print_maze_coordinates(maze):
    print('\n{:^19}'.format('LABYRINTH'))
    print(' -----------------')
    print('   1 2 3 4 5 6 7 8 ')
    for i in range(8):
        print('', i + 1, end=' ')
        for j in maze[i]:
            print(j, end=' ')
        print()


def input_print(*msg):
    pass


def true_coord(x, y):
    coord = (x, y)
    coord = tuple(i - 1 for i in coord)
    return coord


def insert_G_P(maze, goal, person, gxy=(1, 6), pxy=(4, 4)):
    gxy = true_coord(gxy[0], gxy[1])
    pxy = true_coord(pxy[0], pxy[1])
    maze[gxy[0]][gxy[1]] = goal
    maze[pxy[0]][pxy[1]] = person
    return maze#, gxy, pxy


def map_maze(maze):
    maze_indexes = [(x, y) for x in range(len(maze)) for y in range(len(maze))]
    maze_map = dict(zip(maze_indexes,
                   [j for i in range(len(maze)) for j in maze[i]]))
    # for k in maze_map.copy():
    #     if maze_map[k] == 'x':
    #         maze_map.pop(k)
    # the for above works too
    maze_map = {k : v for k, v in iter(maze_map.items()) if v is not 'x'}

    return maze_map


def count_distances(maze_map, gxy, pxy, person):








if __name__ == "__main__":
    lab = insert_G_P(LABYRINTH, GOAL, PERSON)
    print_maze_coordinates(lab)
    print('\n', map_maze(lab))
