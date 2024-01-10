class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def withinbounds(a, b):
            if (a>=0 and a<=len(board)-1) and (b>=0 and b<=len(board[0])-1):
                return True
            return False

        def neighbours(i, j):
            # use offset to generate neighbours
            # check if neighbour is within matrix, and not the same element again
            n = []
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if a == 0 and b == 0:
                        continue
                    if withinbounds(i+a, j+b):
                        n.append(board[i+a][j+b])
            return n

        # create auxiliary matrix with same size as board
        aux = [[0 for i in range(len(board[0]))]for j in range(len(board))]

        # fill aux with number of live neighbours
        for i in range(len(aux)):
            for j in range(len(aux[0])):
                n = sum(neighbours(i, j))
                aux[i][j] = n

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    live = aux[i][j]
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    live = aux[i][j]
                    if live == 3:
                        board[i][j] = 1