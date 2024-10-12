from typing import List, Optional, Set, Tuple
from version2.puzzle_state import PuzzleState

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
            for move in state.get_successors():
                state.apply_move_inplace(move)
                if state not in visited:
                    result, succ_nodes_expanded = self.dls(state, limit - 1, visited)
                    nodes_expanded += succ_nodes_expanded
                    
                    if result is not None:
                        state.undo_move_inplace(move)  
                        return [move] + result, nodes_expanded
                    
                state.undo_move_inplace(move)  
            
            visited.remove(state)
            return None, nodes_expanded        

    def solve(self) -> Tuple[List[str], int, int]:
        result_path, nodes_expanded = self.iddfs()
        return result_path, len(result_path), nodes_expanded