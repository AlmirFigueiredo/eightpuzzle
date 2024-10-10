from __future__ import annotations
from typing import List, Tuple, Optional

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

    def get_successors(self) -> List[Tuple[PuzzleState, str]]:
        successors: List[Tuple[PuzzleState, str]] = []
        i, j = self.find_empty_space()
        directions: List[Tuple[int, int, str]] = [
            (-1, 0, 'Up'),
            (1, 0, 'Down'),
            (0, -1, 'Left'),
            (0, 1, 'Right')
        ]
        for delta_i, delta_j, move in directions:
            new_i, new_j = i + delta_i, j + delta_j
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_tiles: List[List[int]] = [row[:] for row in self.tiles] #copy tiles to new_tiles
                new_tiles[i][j], new_tiles[new_i][new_j] = new_tiles[new_i][new_j], new_tiles[i][j] #shift
                successor_state: PuzzleState = PuzzleState(new_tiles)
                successors.append((successor_state, move))
        return successors

    def apply_move(self, move: str) -> PuzzleState:
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
            new_tiles: List[List[int]] = [row[:] for row in self.tiles]   
            new_tiles[i][j], new_tiles[new_i][new_j] = new_tiles[new_i][new_j], new_tiles[i][j] #shift
            return PuzzleState(new_tiles)
        else:
            raise ValueError("Invalid State.")

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
