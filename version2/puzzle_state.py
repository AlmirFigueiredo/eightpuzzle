from __future__ import annotations
from typing import List, Tuple, Optional, Set

class PuzzleState:
    def __init__(self, tiles: List[List[int]]):
        self.tiles: List[List[int]] = tiles  

    def is_goal(self) -> bool:
        goal_tiles: List[List[int]] = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        return self.tiles == goal_tiles

    def find_empty_space(self) -> Tuple[int, int]:
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == 0:
                    return i, j
        raise ValueError("Empty Space Not Found.")

    def get_successors(self) -> List[str]:
        i, j = self.find_empty_space()
        directions: List[Tuple[int, int, str]] = [
            (-1, 0, 'Up'),
            (1, 0, 'Down'),
            (0, -1, 'Left'),
            (0, 1, 'Right')
        ]
        valid_moves: List[str] = []
        for delta_i, delta_j, move in directions:
            new_i, new_j = i + delta_i, j + delta_j
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                valid_moves.append(move)
        return valid_moves

    def apply_move_inplace(self, move: str) -> None:
        i, j = self.find_empty_space()
        possible_moves: dict[str, Tuple[int, int]] = {
            'Up': (-1, 0),
            'Down': (1, 0),
            'Left': (0, -1),
            'Right': (0, 1)
        }
        if move not in possible_moves:
            raise ValueError(f"Invalid move: {move}")
        delta_i, delta_j = possible_moves[move]
        new_i, new_j = i + delta_i, j + delta_j
        if 0 <= new_i < 3 and 0 <= new_j < 3: 
            self.tiles[i][j], self.tiles[new_i][new_j] = self.tiles[new_i][new_j], self.tiles[i][j]
        else:
            raise ValueError("Invalid State.")

    def undo_move_inplace(self, move: str) -> None:
        reverse_moves: dict[str, str] = {
            'Up': 'Down',
            'Down': 'Up',
            'Left': 'Right',
            'Right': 'Left'
        }
        reverse_move = reverse_moves[move]
        self.apply_move_inplace(reverse_move)
        
    def print_state(self) -> None:
        print('-------------')
        for row in self.tiles:
            for num in row:
                print(f'| {num} ', end='')
            print('|')
        print('-------------')

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PuzzleState):
            return NotImplemented
        return self.tiles == other.tiles

    def __hash__(self) -> int:
        return hash(tuple(tuple(row) for row in self.tiles))
