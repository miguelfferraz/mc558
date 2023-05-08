# -*- coding: utf-8 -*-

GREEN = 0
YELLOW = 1
RED = 2


def regression(adjacency_matrix, result, i, last_color):
    for j in range(len(adjacency_matrix[i])):
        current_color = adjacency_matrix[i][j]
        if current_color is None:
            continue
        elif current_color is GREEN or \
             (current_color is RED and last_color is GREEN) or \
             (current_color is YELLOW and last_color is not RED):
            result[j] += 1
            result = regression(adjacency_matrix, result, j, current_color)

    return result


def main():
    n, m, start, target = map(int, input().strip().split(' '))

    adjacency_matrix = [[None] * n for _ in range(n)]
    result = [0] * n

    for _ in range(m):
        i, j, c = map(int, input().strip().split(' '))   
        adjacency_matrix[i][j] = c

    if start == target:
        print(1)
        return
    
    result = regression(adjacency_matrix, result, start, GREEN)
    print(result[target])


if __name__ == '__main__':
    main()
