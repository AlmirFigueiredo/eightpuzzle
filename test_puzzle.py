import unittest
from typing import List

from version1.puzzle_solver import PuzzleSolver
from version1.puzzle_state import PuzzleState


class TestPuzzleSolver(unittest.TestCase):

    def test_initial_state_645_321_780(self):
        initial_tiles: List[List[int]] = [
            [6, 4, 5],
            [3, 2, 1],
            [7, 8, 0]
        ]
        
        goal_state: List[List[int]] = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
 
        initial_state = PuzzleState(initial_tiles)
        
        solver = PuzzleSolver(initial_state)
        
        result_path, depth, nodes_expanded = solver.solve()

        expected_depth = 24
        self.assertEqual(len(result_path), expected_depth, f"Erro: Profundidade esperada {expected_depth}, mas foi {len(result_path)}.")

        current_state = initial_state
        for move in result_path:
            current_state = current_state.apply_move(move)
        
        self.assertEqual(current_state.tiles, goal_state, "Erro: O estado final não corresponde ao estado objetivo.")

if __name__ == '__main__':
    unittest.main()
