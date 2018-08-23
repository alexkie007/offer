import re


class Maze:
    def render(self, command):
        """
        :param command:  the input data with two line
        :return:
        """
        isvalid = self.check_data_valid(command)
        if isvalid:
            return 0, isvalid
        dimension, maze_road = self.init_params(command)
        if not self.check_maze_connection(maze_road):
            return 0, "Maze format error."
        maze_row = self.converse_rule(dimension[0])
        maze_column = self.converse_rule(dimension[1])
        maze = [(["[W]"] * maze_column) for i in range(maze_row)]
        maze_road = self.mapping_dot(maze_road)
        robot_pos = []
        robot_move = []
        if command[2] != "":
            print(command[2])
            if len(command[2].split(" ")) ==2:
                robot_pos, robot_move = self.conver_robot(command[2].split(" "))
        maze = self.converse_maze(maze_road, maze, robot_pos, robot_move)
        return 1, maze

    def  check_data_valid(self, command):
        """
        :param command: the input with two line
        :return: return error type if data is invalid
        """
        # checkout whether the first line data of command is valid
        dimension = command[0].split(" ")
        if len(dimension) != 2 or dimension.__contains__(""):
            return "Incorrect command format​."
        for number in dimension:
            if not re.match("^[-\sa-zA-Z0-9]+$", number):
                return "Incorrect command format​."
            if not number.isdigit():
                return "Invalid number format​.​"
            if int(number) <= 0:
                return "Number out of range​."
        dimension = [int(x) for x in dimension]
        # checkout whether the second line data of command is valid
        maze_dots = command[1]
        if not re.match("^[-\sa-zA-Z0-9,;]+$", maze_dots):
            return "Incorrect command format​."
        for dot_pair in maze_dots.split(";"):
            dot_pair = dot_pair.split(" ")
            if len(dot_pair) != 2:
                return "Incorrect command format​."
            for dot in dot_pair:
                dot = dot.split(",")
                if len(dot) != 2 or dot.__contains__(""):
                    return "Incorrect command format​."
                for number in dot:
                    if not number.isdigit():
                        return "Invalid number format​.​"
                    if int(number) < 0 or int(number) > min(dimension) - 1:
                        return "Number out of range​."
        if command[2] != "":
            robot_pos = command[2].split(" ")
            robot_pos, robot_move = self.conver_robot(robot_pos)
            print(command[2])
            if robot_pos[0] > dimension[0] or robot_pos[0] < 0:
                return "Number out of range​"
            if robot_pos[1] > dimension[1] or robot_pos[1] < 0:
                return "Number out of range​"

    def init_params(self, command):
        """
        :param command:
        :return: the maze dimension and maze_road data
        """
        dimension = command[0].split(" ")
        dimension = [int(x) for x in dimension]
        maze_dots = command[1]
        maze_road = []
        for dot_pair in maze_dots.split(";"):
            maze_dot_pair = []
            for dot in dot_pair.split(" "):
                dot = dot.split(",")
                maze_dot = [int(x) for x in dot]
                maze_dot_pair.append(maze_dot)
            maze_road.append(maze_dot_pair)

        return dimension, maze_road

    def check_maze_connection(self, maze_road):
        """
        :param maze_road:
        :return: the result whether the maze can connect
        """
        connection = True
        for dot_pair in maze_road:
            dot_pair.sort()
            dot1_x = dot_pair[0][0]
            dot1_y = dot_pair[0][1]
            dot2_x = dot_pair[1][0]
            dot2_y = dot_pair[1][1]
            if dot1_x == dot2_x and abs(dot1_y - dot2_y) == 1:
                pass
            elif dot1_y == dot2_y and abs(dot1_x - dot2_x) == 1:
                pass
            elif dot2_x == dot1_x and dot2_y == dot1_y:
                pass
            else:
                connection = False
        return connection

    def mapping_dot(self, maze_road):
        """
        :param maze_road:
        :return: return maze_road in big maze
        """
        for index, dot_pair in enumerate(maze_road):
            dot_pair[0][0] = self.converse_rule(dot_pair[0][0])
            dot_pair[0][1] = self.converse_rule(dot_pair[0][1])
            dot_pair[1][0] = self.converse_rule(dot_pair[1][0])
            dot_pair[1][1] = self.converse_rule(dot_pair[1][1])
            maze_road[index] = dot_pair
        return maze_road

    def conver_robot(self, robot_pos):
        print(robot_pos[0])
        robot_poss = [int(x) for x in robot_pos[0].split(",")]

        robot_move = [x for x in robot_pos[1]]
        # robot_poss = [int(x) for x in robot_pos.split(",")]
        robot_poss[0] = self.converse_rule(robot_poss[0])
        robot_poss[1] = self.converse_rule(robot_poss[1])
        robot_moves = [x for x in robot_move]
        print(robot_poss,robot_moves)
        return robot_poss, robot_moves

    def converse_rule(self, num):
        """
        :param num: num should be conversed
        :return:
        """
        return 2 * num + 1

    def converse_maze(self, maze_road, maze, robot_pos, robot_move):
        """
        :param maze_road: initial maze_road
        :param maze: initial maze
        :return: return the maze with replace [W] to [R]
        """
        for dot_pair in maze_road:
            dot_pair.sort()
            dot1_x = dot_pair[0][0]
            dot1_y = dot_pair[0][1]
            dot2_x = dot_pair[1][0]
            dot2_y = dot_pair[1][1]
            if dot1_x == dot2_x:
                for col in range(dot1_y, dot2_y + 1):
                    maze[dot1_x][col] = "[R]"
            else:
                for row in range(dot1_x, dot2_x + 1):
                    maze[row][dot1_y] = "[R]"
        if len(robot_move) >=1:
            for move in robot_move:
                if move == "W":
                    robot_pos[1] -= 1
                if move == "S":
                    robot_pos[1] += 1
                if move == "A":
                    robot_pos[0] -= 1
                if move == "D":
                    robot_pos[0] += 1
        if len(robot_pos) != 0:
            maze[robot_pos[0]][robot_pos[1]] = "[*]"
        return maze

    def show_maze(self, maze):
        """
        :param maze: the conversed maze
        :param dimension: the dimension of maze
        :return:
        """
        maze_row = len(maze)
        maze_column = len(maze[0])
        for row in range(maze_row):
            for column in range(maze_column):
                if column == maze_column - 1:
                    print(maze[row][column])
                else:
                    print(maze[row][column], end=" ")


if __name__ == "__main__":
    maze = Maze()
    command = []
    print("请输入迷宫规格")
    command.append(input())
    print("请输入迷宫道路网格")
    command.append((input()))
    print(("请输入机器位置"))
    command.append(input())
    code, msg = maze.render(command)
    if code == 0:
        print(msg)
    else:
        maze.show_maze(msg)
    print("\n")
    # with open("/Users/yujie/Nustore Files/Workspaces/Python/offer/thoughtswork/test1.txt") as f:
    #     lines = f.readlines()
    #     line_num = 1
    #     command = []
    #     for line in lines:
    #         if line == "\n":
    #             continue
    #         print(line.strip())
    #         if line_num % 3 == 1:
    #             command.append(line.strip())
    #         elif line_num % 3 == 2:
    #             command.append(line.strip())
    #         else:
    #             command.append(line.strip())
    #             code, msg = maze.render(command)
    #             if code == 0:
    #                 print(msg)
    #             else:
    #                 maze.show_maze(msg)
    #             print("\n")
    #             command = []
    #         line_num += 1
