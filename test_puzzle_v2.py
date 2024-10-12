import unittest
from typing import List

from version2.puzzle_solver import PuzzleSolver
from version2.puzzle_state import PuzzleState

goal_state: List[List[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

class TestPuzzleSolver(unittest.TestCase):

    def test_initial_state_645_321_780(self):
        initial_tiles: List[List[int]] = [
            [6, 4, 5],
            [3, 2, 1],
            [7, 8, 0]
        ]

        initial_state = PuzzleState(initial_tiles)
        
        solver = PuzzleSolver(initial_state)
        
        result_path, depth, nodes_expanded = solver.solve()
        
        expected_result_path = ['Up', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Down', 'Left', 'Up', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Down', 'Right']
        expected_depth = 24
        self.assertEqual(depth, expected_depth, f"Erro: Profundidade esperada {expected_depth}, mas foi {depth}.")
        self.assertEqual(result_path, expected_result_path, f"Erro: O result path esperado {expected_result_path}, mas foi {result_path}.")
        current_state = initial_state
        for move in result_path:
            current_state.apply_move_inplace(move)  
        
        self.assertEqual(current_state.tiles, goal_state, "Erro: O estado final não corresponde ao estado objetivo.")

    def test_initial_state_153_246_780(self):
        initial_tiles: List[List[int]] = [
            [1, 5, 3],
            [2, 4, 6],
            [7, 8, 0]
        ]

        initial_state = PuzzleState(initial_tiles)
        
        solver = PuzzleSolver(initial_state)
        
        result_path, depth, nodes_expanded = solver.solve()
        
        expected_result_path = ['Up', 'Left', 'Left', 'Up', 'Right', 'Down', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Up', 'Right', 'Down', 'Down']
        expected_depth = 16
        self.assertEqual(depth, expected_depth, f"Erro: Profundidade esperada {expected_depth}, mas foi {depth}.")
        self.assertEqual(result_path, expected_result_path, f"Erro: O result path esperado {expected_result_path}, mas foi {result_path}.")
        current_state = initial_state
        for move in result_path:
            current_state.apply_move_inplace(move)  
        
        self.assertEqual(current_state.tiles, goal_state, "Erro: O estado final não corresponde ao estado objetivo.")

    def test_initial_state_216_543_870(self):
        initial_tiles: List[List[int]] = [
            [2, 1, 6],
            [5, 4, 3],
            [8, 7, 0]
        ]

        initial_state = PuzzleState(initial_tiles)
        
        solver = PuzzleSolver(initial_state)
        
        result_path, depth, nodes_expanded = solver.solve()
        
        expected_result_path = ['Up', 'Up', 'Left', 'Down', 'Down', 'Left', 'Up', 'Right', 'Right', 'Down', 'Left', 'Left', 'Up', 'Up', 'Right', 'Right', 'Down', 'Left', 'Left', 'Up', 'Right', 'Down', 'Down', 'Right']
        expected_depth = 24
        expected_nodes_expanded = 18792
        
        self.assertEqual(depth, expected_depth, f"Erro: Profundidade esperada {expected_depth}, mas foi {depth}.")
        self.assertEqual(result_path, expected_result_path, f"Erro: O result path esperado {expected_result_path}, mas foi {result_path}.")
        self.assertEqual(nodes_expanded, expected_nodes_expanded, f"Erro: O Node Expanded esperado {expected_nodes_expanded}, mas foi {nodes_expanded}.")
        current_state = initial_state
        for move in result_path:
            current_state.apply_move_inplace(move)  
        
        self.assertEqual(current_state.tiles, goal_state, "Erro: O estado final não corresponde ao estado objetivo.")

    def test_initial_state_658_427_130(self):
        initial_tiles: List[List[int]] = [
            [6, 5, 8],
            [4, 2, 7],
            [1, 3, 0]
        ]

        initial_state = PuzzleState(initial_tiles)
        
        solver = PuzzleSolver(initial_state)
        
        result_path, depth, nodes_expanded = solver.solve()
        
        expected_result_path = ['Up', 'Up', 'Left', 'Left', 'Down', 'Right', 'Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Up', 'Left', 'Left', 'Down', 'Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Right']
        expected_depth = 26
        expected_nodes_expanded = 463534
        
        self.assertEqual(depth, expected_depth, f"Erro: Profundidade esperada {expected_depth}, mas foi {depth}.")
        self.assertEqual(result_path, expected_result_path, f"Erro: O result path esperado {expected_result_path}, mas foi {result_path}.")
        self.assertEqual(nodes_expanded, expected_nodes_expanded, f"Erro: O Node Expanded esperado {expected_nodes_expanded}, mas foi {nodes_expanded}.")
        current_state = initial_state
        for move in result_path:
            current_state.apply_move_inplace(move)  
        
        self.assertEqual(current_state.tiles, goal_state, "Erro: O estado final não corresponde ao estado objetivo.")

    def test_initial_state_172_803_546(self):
        initial_tiles: List[List[int]] = [
            [1, 7, 2],
            [8, 0, 3],
            [5, 4, 6]
        ]

        initial_state = PuzzleState(initial_tiles)
        
        solver = PuzzleSolver(initial_state)
        
        result_path, depth, nodes_expanded = solver.solve()
        
        expected_result_path = ['Left', 'Down', 'Right', 'Up', 'Up', 'Right', 'Down', 'Down', 'Left', 'Up', 'Left', 'Down', 'Right', 'Right']
        expected_depth = 14
        expected_nodes_expanded = 3723
        
        self.assertEqual(depth, expected_depth, f"Erro: Profundidade esperada {expected_depth}, mas foi {depth}.")
        self.assertEqual(result_path, expected_result_path, f"Erro: O result path esperado {expected_result_path}, mas foi {result_path}.")
        self.assertEqual(nodes_expanded, expected_nodes_expanded, f"Erro: O Node Expanded esperado {expected_nodes_expanded}, mas foi {nodes_expanded}.")
        current_state = initial_state
        for move in result_path:
            current_state.apply_move_inplace(move)  
        
        self.assertEqual(current_state.tiles, goal_state, "Erro: O estado final não corresponde ao estado objetivo.")

if __name__ == '__main__':
    unittest.main()
