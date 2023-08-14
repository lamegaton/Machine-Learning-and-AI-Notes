import numpy as np

class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.done = False
        return self.board.flatten()

    def step(self, action):
        row, col = divmod(action, 3)
        if self.board[row, col] != 0 or self.done:
            return self.board.flatten(), -10, True  # Invalid move

        self.board[row, col] = self.current_player
        winner = self.check_winner()

        if winner != 0:
            return self.board.flatten(), 10 if winner == 1 else -10, True

        if 0 not in self.board:
            return self.board.flatten(), 0, True  # Draw

        self.current_player = 3 - self.current_player
        return self.board.flatten(), 0, False

    def check_winner(self):
        for i in range(3):
            if self.board[i, :].sum() == 3 or self.board[:, i].sum() == 3:
                return 1
            if self.board[i, :].sum() == -3 or self.board[:, i].sum() == -3:
                return -1

        diag_sum1 = self.board.diagonal().sum()
        diag_sum2 = self.board[::-1].diagonal().sum()
        if diag_sum1 == 3 or diag_sum2 == 3:
            return 1
        if diag_sum1 == -3 or diag_sum2 == -3:
            return -1

        return 0

    def render(self):
        print(self.board)
