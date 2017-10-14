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

LABYRINTH_2 = [
['x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
['x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', '-', '-', 'x', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', 'x', 'x', '-', 'x', 'x', '-', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', '-', 'x', 'x', '-', 'x', '-', 'x', '-', '-', '-', '-', 'x', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', '-', '-', '-', '-', 'x', '-', 'x', '-', 'x', 'x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x', '-', 'x', 'x', '-', 'x', '-', 'x', '-', '-', '-', '-', 'x'],
['x', '-', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', '-', 'x', '-', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', '-', '-', 'x', '-', 'x', '-', '-', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', 'x', '-', '-', 'x', '-', '-', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', '-', '-', '-', '-', '-', '-', 'x', 'x', 'x', 'x', '-', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', '-', '-', '-', 'x', 'x', 'x', 'x', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', '-', '-', '-', '-', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', '-', 'x'],
['x', 'x', 'x', 'x', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]

LAB_CLEAN = [
['x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
['x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', '-', '-', 'x', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', 'x', 'x', '-', 'x', 'x', '-', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', '-', 'x', 'x', '-', 'x', '-', 'x', '-', '-', '-', '-', 'x', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', '-', '-', '-', '-', 'x', '-', 'x', '-', 'x', 'x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x', '-', 'x', 'x', '-', 'x', '-', 'x', '-', '-', '-', '-', 'x'],
['x', '-', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', '-', 'x', '-', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', '-', '-', 'x', '-', 'x', '-', '-', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', 'x', '-', '-', 'x', '-', '-', 'x', 'x', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', '-', '-', '-', '-', '-', '-', 'x', 'x', 'x', 'x', '-', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', '-', '-', '-', 'x', 'x', 'x', 'x', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', '-', 'x', 'x', 'x', '-', 'x', '-', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', '-', 'x'],
['x', '-', '-', '-', '-', '-', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x', 'x', '-', 'x'],
['x', 'x', 'x', 'x', 'x', '-', 'x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'x'],
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]
GOAL = 'G'
PERSON = '☺'
WALL = 'x'
MSG1 = ''

def print_maze_coordinates(maze):
    print('\n{:^68}'.format('L A B Y R I N T H'))
    print('--------------------------------------------------------------------')
    print('   01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22')
    for i in range(22):
        print('{:0>2}'.format(i + 1), end=' ')
        for j in maze[i]:
            print('{:' '<2}'.format(j), end=' ')
        print()


def input_print(*msg):
    pass


def true_coord(x, y):
    coord = (x, y)
    coord = tuple(i - 1 for i in coord)
    return coord


def insert_G_P(maze, goal, person, gxy=(21, 6), pxy=(21, 21)):
    gxy = true_coord(gxy[0], gxy[1])
    pxy = true_coord(pxy[0], pxy[1])
    maze[gxy[0]][gxy[1]] = goal
    maze[pxy[0]][pxy[1]] = person
    return maze, gxy, pxy


def map_maze(maze, wall):
    maze_keys = [(x, y) for x in range(len(maze)) for y in range(len(maze))]
    maze_maped = dict(zip(maze_keys,
                      [j for i in range(len(maze)) for j in maze[i]]))
    # for k in maze_maped.copy():
    #     if maze_maped[k] == 'x':
    #         maze_maped.pop(k)
    # the for above works too
    maze_maped = {k : v for k, v in iter(maze_maped.items()) if v is not wall}

    return maze_maped


def count_distances(maze_maped, gxy, pxy):
    '''
    Marca todos os passos do labirinto com um número que vai crescendo desde
    de GOAL até  preencher todo o laririnto. O menor caminho a ser percorrido
    é aquele que chega até PERSON com o mínimo de passos.
    Usa-se uma estrutura dict para marcar a "distância" (número inteiro) e o
    antecessor ("pai")
    Percorrendo o labirinto de PERSON até GOAL de pai em pai vai-se chegar a
    GOAL pelo menor caminho.

    '''
    def prepare_maze_map(maze_maped):
        for k in maze_maped.keys():
            maze_maped[k] = {"distance": 0, "father": (0, 0)}
        return maze_maped

    maze = prepare_maze_map(maze_maped)
    maze[gxy] = {"distance": 0, "father": gxy}
    adjacents = list(maze.keys())
    adjacents.remove(gxy)
    goal = gxy
    queue = [goal]
    exploreds = [goal]
    while queue:
        actual = queue.pop(0)
        actual_row, actual_col = actual[0], actual[1]
        for adj in adjacents:
            if adj in exploreds:
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
    maze[pxy]['distance'] = PERSON
    maze[gxy]['distance'] = GOAL
    return maze


def label_distances(maze, maze_distances):
    for key in maze_distances.keys():
        maze[key[0]][key[1]] = maze_distances[key]['distance']
    return maze


def walking_to_goal(maze, maze_distances, gxy, pxy):
    father = (0, 0)
    actual = pxy
    distance = maze_distances[maze_distances[actual]['father']]['distance']
    for _ in range(distance + 1):
        father = maze_distances[actual]['father']
        # maze[actual[0]][actual[1]] = '-'
        # print('actual:', actual,'====> father:', father)
        maze[father[0]][father[1]] = PERSON
        actual = father
    return maze



if __name__ == "__main__":
    lab, g_coord, p_coord = insert_G_P(LABYRINTH_2, GOAL, PERSON)
    lab_clean, x, y = insert_G_P(LAB_CLEAN, GOAL, PERSON)
    print_maze_coordinates(lab)
    maze_distances = count_distances(map_maze(lab, WALL), g_coord, p_coord)
    print_maze_coordinates(label_distances(lab, maze_distances))
    print_maze_coordinates(walking_to_goal(lab_clean, maze_distances, g_coord,
                                                                      p_coord))
