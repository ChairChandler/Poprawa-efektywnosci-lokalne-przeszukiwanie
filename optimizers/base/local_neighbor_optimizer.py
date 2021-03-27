from abc import abstractmethod, ABC
from typing import List
from itertools import chain

from optimizers.base.base import Route, Solution, InnerOuterVertexOptimizer


class LocalNeighborOptimizer(InnerOuterVertexOptimizer, ABC):
    def _search(self) -> Solution:
        best_solution = Solution(self.init_cost, self.route)
        no_new_solution = True

        while no_new_solution:
            solutions = [
                self._find_solutions(best_solution.route),
                self._find_swap_inner_outer_vertices_solutions(best_solution.route)
            ]

            for solution in chain.from_iterable(solutions):
                cost = self._calculate_score(solution.route)

                if cost < best_solution.cost:
                    best_solution = Solution(cost, solution.route)
                    no_new_solution = False

        return best_solution

    @abstractmethod
    def _find_solutions(self, route: Route) -> List[Solution]:
        pass


