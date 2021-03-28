from abc import abstractmethod, ABC
from typing import List
import random

from .base import Route, Solution, InnerOuterVertexOptimizer


class LocalNeighborOptimizer(InnerOuterVertexOptimizer, ABC):
    def _search(self) -> Solution:
        best_solution = Solution(self.init_cost, self.route)
        new_solution = True

        while new_solution:
            new_solution = False

            solutions = [
                *self._find_solutions(best_solution.route),
                *self._find_swap_inner_outer_vertices_solutions(best_solution.route)
            ]

            random.shuffle(solutions)
            for solution in solutions:
                cost = self._calculate_score(solution.route)

                if cost < best_solution.cost:
                    best_solution = Solution(cost, solution.route)
                    new_solution = True

        return best_solution

    @abstractmethod
    def _find_solutions(self, route: Route) -> List[Solution]:
        pass


