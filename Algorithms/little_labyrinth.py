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
    print('\n{:^25}'.format('LABYRINTH'))
    print(' ------------------------')
    print('   1  2  3  4  5  6  7  8 ')
    for i in range(8):
        print('', i + 1, end=' ')
        for j in maze[i]:
            print('{:' '<2}'.format(j), end=' ')
        print()


def input_print(*msg):
    pass


def true_coord(x, y):
    coord = (x, y)
    coord = tuple(i - 1 for i in coord)
    return coord


def insert_G_P(maze, goal, person, gxy=(6, 1), pxy=(1, 6)):
    gxy = true_coord(gxy[0], gxy[1])
    pxy = true_coord(pxy[0], pxy[1])
    maze[gxy[0]][gxy[1]] = goal
    maze[pxy[0]][pxy[1]] = person
    return maze, gxy, pxy


def map_maze(maze, wall):
    maze_indexes = [(x, y) for x in range(len(maze)) for y in range(len(maze))]
    maze_maped = dict(zip(maze_indexes,
                   [j for i in range(len(maze)) for j in maze[i]]))
    # for k in maze_maped.copy():
    #     if maze_maped[k] == 'x':
    #         maze_maped.pop(k)
    # the for above works too
    maze_maped = {k : v for k, v in iter(maze_maped.items()) if v is not wall}

    return maze_maped


def count_distances(maze_maped, gxy=(5, 0), pxy=(0, 5)):
    def prepare_maze_map(maze_maped):
        for k in maze_maped.keys():
            maze_maped[k] = {"distance": 0, "father": None}
        return maze_maped

    maze = prepare_maze_map(maze_maped)
    maze[gxy] = {"distance": 0, "father": None}
    adjacents = list(maze.keys())
    adjacents.remove(gxy)
    goal = gxy
    queue = [goal]
    exploreds = [goal]
    while queue:
        actual = queue.pop(0)
        # print('>>>>>>>> actual:', actual)
        actual_row, actual_col = actual[0], actual[1]
        for adj in adjacents:
            if adj in exploreds:
                continue
            if adj == pxy:
                maze[adj] = {"distance": PERSON, "father": actual}
                continue
            adj_row, adj_col = adj[0], adj[1]
            if actual_row == 0 and actual_row + 1 == adj_row:
                if actual_col == adj_col:
                    maze[adj] = {"distance": maze[actual]['distance'] + 1,
                                 "father": actual}
                    queue.append(adj)
                    exploreds.append(adj)
            elif actual_row == 7 and actual_row - 1 == adj_row:
                if actual_col == adj_col:
                    maze[adj] = {"distance": maze[actual]['distance'] + 1,
                                 "father": actual}
                    queue.append(adj)
                    exploreds.append(adj)
            elif actual_col == 0 and actual_col + 1 == adj_col:
                if actual_row == adj_row:
                    maze[adj] = {"distance": maze[actual]['distance'] + 1,
                                 "father": actual}
                    queue.append(adj)
                    exploreds.append(adj)
            elif actual_col == 7 and actual_col - 1 == adj_col:
                if actual_row == adj_row:
                    maze[adj] = {"distance": maze[actual]['distance'] + 1,
                                 "father": actual}
                    queue.append(adj)
                    exploreds.append(adj)
            elif actual_row + 1 == adj_row or actual_row - 1 == adj_row:
                if actual_col == adj_col:
                    maze[adj] = {"distance": maze[actual]['distance'] + 1,
                                 "father": actual}
                    queue.append(adj)
                    exploreds.append(adj)
            elif actual_col + 1 == adj_col or actual_col - 1 == adj_col:
                if actual_row == adj_row:
                    maze[adj] = {"distance": maze[actual]['distance'] + 1,
                                 "father": actual}
                    queue.append(adj)
                    exploreds.append(adj)
    maze[pxy] = {"distance": PERSON, "father": actual}
    # for k in maze.keys():
    #     for j in maze.keys():
    #         if k == maze[j]['father']:
    #             print(k, maze[k], '===>', j, maze[j])
    return maze


def label_distances(maze, maze_distances):
    for key in maze_distances.keys():
        maze[key[0]][key[1]] = maze_distances[key]['distance']
    return maze


if __name__ == "__main__":
    lab, g_coord, p_coord = insert_G_P(LABYRINTH, GOAL, PERSON)
    print_maze_coordinates(lab)
    maze_distances = count_distances(map_maze(lab, WALL))
    print_maze_coordinates(label_distances(lab, maze_distances))
