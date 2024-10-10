from typing import List, Optional, Set, Tuple
from version1.puzzle_state import PuzzleState


class PuzzleSolver:
    def __init__(self, initial_state: PuzzleState):
        self.initial_state: PuzzleState = initial_state

    def iddfs(self) -> Tuple[Optional[List[str]], int]:
        depth: int = 0
        while True:
            result, nodes_expanded = self.dls(self.initial_state, depth, set())
            if result is not None:
                return result, nodes_expanded
            depth += 1

    def dls(self, state: PuzzleState, limit: int, visited: Set[PuzzleState]) -> Tuple[Optional[List[str]], int]:
        nodes_expanded: int = 0
        if state.is_goal():
            return [], nodes_expanded
        elif limit == 0:
            return None, nodes_expanded
        else:
            visited.add(state)
            nodes_expanded += 1
            for successor, move in state.get_successors():
                if successor not in visited:
                    result, succ_nodes_expanded = self.dls(successor, limit - 1, visited)
                    nodes_expanded += succ_nodes_expanded
                    if result is not None:
                        return [move] + result, nodes_expanded
            visited.remove(state)
            return None, nodes_expanded

    def solve(self) -> Tuple[List[str], int, int]:
        result_path, nodes_expanded = self.iddfs()
        return result_path, len(result_path), nodes_expanded
        
        # print("Initial State:")
        # self.initial_state.print_state()
        # current_state: PuzzleState = self.initial_state
        # print("IDDFS Solution:")
        # if result_path:
        #     for move in result_path:
        #         print(f"Move: {move}")
        #         current_state = current_state.apply_move(move)
        #         current_state.print_state()
        # else:
        #     print("Solution Not Found.")
        # print("Depth:", len(result_path) if result_path else 0)
        # print("Expanded Nodes:", nodes_expanded)

