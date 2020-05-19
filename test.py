from tictactoe import *
import unittest

class Test(unittest.TestCase):

    def test_player(self):
        board = [[None, None, None], 
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(player(board), "X")

        board = [["X", None, None], 
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(player(board), "O")

        board = [["X", None, None], 
                 [None, "O", None],
                 [None, None, None]]
        self.assertEqual(player(board), "X")


    def test_actions(self):
        board = [[None, None, None], 
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(len(actions(board)), 9)

        board = [["X", None, None], 
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(len(actions(board)), 8)

        board = [["X", None, None], 
                 [None, "O", None],
                 [None, None, None]]
        self.assertEqual(len(actions(board)), 7)

        board = [["X", "O", "X"], 
                 ["O", "O", "X"],
                 ["X", "X", "O"]]
        self.assertEqual(len(actions(board)), 0)


    def test_result(self):
        board = [[None, None, None], 
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(result(board, (0, 0)), [["X", None, None], 
                                                 [None, None, None],
                                                 [None, None, None]])

        board = [["X", None, None], 
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(result(board, (1, 1)), [["X", None, None], 
                                                 [None, "O", None],
                                                 [None, None, None]])

        
        with self.assertRaises(Exception):
            result(board, (0, 0))


    def test_winner(self):
        board = [[None, None, None], 
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(winner(board), None)

        board = [["X", "O", "X"], 
                 ["O", "O", "X"],
                 ["X", "X", "O"]]
        self.assertEqual(winner(board), None)
        
        board = [["X", "O", "X"], 
                 ["O", "X", None],
                 ["X", None, "O"]]
        self.assertEqual(winner(board), "X")

        board = [["X", "O", "O"], 
                 ["X", "X", None],
                 ["X", None, "O"]]
        self.assertEqual(winner(board), "X")

        board = [[None, "X", "O"], 
                 ["X", "O", "X"],
                 ["O", None, None]]
        self.assertEqual(winner(board), "O")

        board = [["X", None, None], 
                 [None, "X", None],
                 [None, None, "X"]]
        self.assertEqual(winner(board), "X")
        

    def test_terminal(self):
        board = [[None, None, None], 
                 [None, None, None],
                 [None, None, None]]
        self.assertEqual(terminal(board), False)

        board = [["X", "O", "X"], 
                 ["O", "O", "X"],
                 ["X", "X", "O"]]
        self.assertEqual(terminal(board), True)

        board = [["X", None, None], 
                 [None, "O", None],
                 [None, None, None]]
        self.assertEqual(terminal(board), False)

        board = [["X", "O", "O"], 
                 ["X", "X", None],
                 ["X", None, "O"]]
        self.assertEqual(terminal(board), True)


    def test_utility(self):
        board = [["X", "O", "X"], 
                 ["O", "O", "X"],
                 ["X", "X", "O"]]
        self.assertEqual(utility(board), 0)

        board = [["X", "O", "X"], 
                 ["O", "X", None],
                 ["X", None, "O"]]
        self.assertEqual(utility(board), 1)

        board = [[None, "X", "O"], 
                 ["X", "O", "X"],
                 ["O", None, None]]
        self.assertEqual(utility(board), -1)


    def test_minimax(self):
        board = [["X", "O", "X"], 
                 ["O", "X", None],
                 [None, None, "O"]]
        self.assertEqual(minimax(board), (2, 0))

if __name__ == '__main__':
    unittest.main()