"""
一张NxM的地图上每个点的海拔高度不同，从当前点只能访问上、下、左、右四个点中还没有到达过的点,且下一步选的点的海高度必须高于当的点,求从地中的点A到点B总的路径条数除以10°的余数,地坡图左上角坐标为（0,0），右下角坐标为(N-1.M-1)
输入描述：第一行输入两个整数,M(0<N≤600,0<M≤600)用空格隔开:接下来行输入,每行M个整数用空格隔开,代表对应位置的海拔高度(0≤海拔高度≤360000):最后一行四个整数X,Y,Z,W:前两个代表A的坐标为(x,y):后两个代表的坐标为(Z,w);输入保证A、B坐标不同,且坐标合法
输出描述：输出一个整数并换行,整数表示从A到B总的路径条数除以10^9的余数
思路：与走迷宫相同，使用DFS来进行递归搜索。先定义一个book数组用来记录这个点是否走过。使用DFS进行搜索时，每次先判断一下是不是到达了终点，然后不是终点的点，上下左右四个选项都走一遍，每次走一步的时候需要判断我当前的坐标是不是合法，不合法则跳过，合法的话还要判断当前坐标和下一个坐标对应在输入数组里的元素是否满足小于的关系，即下一步的海拔是否比当前的高，如果满足，将下一步置为走过，递归调用DFS，调用完，再置为未走过，因为要回溯。
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
book = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
path = []

def dfs(book, start_x, start_y, end_x, end_y, array):
    '''
    :param start_x: 起始横坐标
    :param start_y: 起始纵坐标
    :param end_x: 终点横坐标
    :param end_y: 终点纵坐标
    :param array: 数组
    :return:
    '''
    next_step = [[0, 1],  # 向右走
                 [1, 0],  # 向下走
                 [0, -1],  # 向左走
                 [-1, 0]  # 向上走
                 ]
    if (start_x == end_x and start_y == end_y):
        path.append(1)
        return

    for i in range(len(next_step)):
        next_x = start_x + next_step[i][0]
        next_y = start_y + next_step[i][1]
        if (next_x < 0 or next_y < 0 or next_x >= len(migong_array) or next_y >= len(migong_array[0])):
            continue
        if (array[next_x][next_y] > array[start_x][start_y] and book[next_x][next_y] == 0):
            book[next_x][next_y] = 1
            dfs(book, next_x, next_y, end_x, end_y, migong_array)
            book[next_x][next_y] = 0
    return


if __name__ == '__main__':
    start_x = 0
    start_y = 1
    end_x = 3
    end_y = 2
    array = [[0, 1, 0, 0, 0], [0, 2, 3, 0, 0], [0, 0, 4, 5, 0], [0, 0, 7, 6, 0]]  # 初始化迷宫
    book[start_x][start_y] = 1  # 将第一步标记为1，证明走过了。避免重复走
    dfs(book, start_x, start_y, end_x, end_y, array)
    print(' path num is : {}'.format(sum(path)))
