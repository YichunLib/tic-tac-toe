class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def check_win(self):
        # 检查行
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]

        # 检查列
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        # 检查对角线
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def change_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def play(self):
        while True:
            self.print_board()
            move = input(f"玩家 {self.current_player}, 请输入你的行和列 (例如: 0 0): ")
            row, col = map(int, move.split())

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("无效的输入，请输入在 0 到 2 之间的数字。")
                continue

            if not self.make_move(row, col):
                print("该位置已被占用，请重新选择。")
                continue

            result = self.check_win()
            if result:
                self.print_board()
                print(f"玩家 {result} 获胜!")
                break

            if ' ' not in [cell for row in self.board for cell in row]:
                self.print_board()
                print("平局!")
                break

            self.change_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
