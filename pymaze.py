import random
import sys
sys.setrecursionlimit(100000)
class PyMaze:
    def __init__(self, size=(100,100), entrance=(1,1)):
        self.__gen_maze__(size,entrance)
        pass
    def __is_wall__(self, pt=(1,1)):
        return ((pt[0] == 0) or (pt[0] == (self.__size__[0]-1)) or (pt[1] == 0) or (pt[1] == (self.__size__[1] - 1)))

    def __is_neighbour_of_visited__(self,pt = (1,1)):
        neighbout_count = 0
        #邻居列表，上下左右
        pt_neighbour_list = [(pt[0]-1, pt[1]),(pt[0]+1, pt[1]),(pt[0], pt[1]-1), (pt[0], pt[1]+1)]
        for obj in pt_neighbour_list:
            if (not self.__is_wall__(obj)):
                if (self.__visited__[obj[0]][obj[1]] == True):
                    neighbout_count += 1
                pass

        return (neighbout_count == 1)

    # 上下左右进行遍历
    # 1、首先判断是否是墙
    # 2、如果不是墙，则判断是否访问过
    # 3、如果没有访问过，再判断该点是否和已经访问过的节点有相邻
    # 4、如果没有相邻的四邻节点，则对该节点执行dfs
    def __dfs_condition__(self, pt):
        if (self.__is_wall__(pt)):
            return False
            pass
        else:
            if (self.__visited__[pt[0]][pt[1]] == True):
                return False
                pass
            else:
                if (self.__is_neighbour_of_visited__(pt)):
                    return True
            pass
        pass

    def __make_neighbour_randow__(self, pt = (1,1)):
        rand_num = random.randint(1,4)
        up =  (pt[0] - 1, pt[1])
        down =  (pt[0] + 1, pt[1])
        left = (pt[0], pt[1] - 1)
        right = (pt[0], pt[1] + 1)
        if (rand_num %4 == 0):
            return [up,down,left,right]
            pass
        if (rand_num %4 == 1):
            return [down, left, right,up]
            pass
        if (rand_num %4 == 2):
            return [left, right,up, down]
            pass
        if (rand_num %4 == 3):
            return [right,up,down,left]
            pass

        pass
    def __dfs__(self, entrance = (1,1)):
        self.__visited__[entrance[0]][entrance[1]] = True
        self.__maze__[entrance[0]][entrance[1]] = 1
        neighbour_list = self.__make_neighbour_randow__(entrance)
        for obj in neighbour_list:
            if (self.__dfs_condition__(obj)):
                self.__dfs__(obj)
                pass
            pass

        pass
    def __gen_maze__(self, size=(100,100), entrance=(1,1)):
        self.__maze__ = [[0 for x in range(0,size[1])] for y in range (0,size[0])]
        self.__maze__[entrance[0]][entrance[1]] = 1
        self.__visited__ =  [[False for x in range(0,size[1] - 1)] for y in range (0,size[0] - 1)]
        print(len(self.__visited__), len(self.__visited__[0]))
        #self.__maze__[exist[0]][exist[1]] = 0
        self.__main_path__ = []
        self.__entrance__ = entrance
        self.__size__ = size
        self.__visited_count__ = 0
        self.__dfs__((1,1))
        pass

    def update_maze(self, size=(100,100), entrance=(1,1)):
        self.__gen_maze__(size, entrance)
        pass
    def output_maze(self):
        for row in self.__maze__:
            print(row)
            pass
        pass
    def get_maze(self):
        return self.__maze__
    def get_maze_str(self):
        return
    def output_maze_str(self):
        for row in self.__maze__:
            row_str = ''
            for i in row:
                if (i == 1):
                    row_str += '0'
                else:
                    row_str += '1'
                pass
            print(row_str)
            pass

    pass


