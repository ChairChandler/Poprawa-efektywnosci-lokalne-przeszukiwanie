from abc import ABC
from typing import Generator, List
from optimizers.base import Route, Optimizer, Solution, GlobalNeighborOptimizer, LocalNeighborOptimizer


class InnerEdgeOptimizer(Optimizer, ABC):
    def _generate_solutions(self, route: Route) -> Generator[Solution]:
        pass


class GlobalInnerEdgeOptimizer(GlobalNeighborOptimizer, InnerEdgeOptimizer):
    def _find_best_solution(self, route: Route) -> Solution:
        return min([*self._generate_solutions(route)], key=lambda x: x.cost)


class LocalInnerEdgeOptimizer(LocalNeighborOptimizer, InnerEdgeOptimizer):
    def _find_solutions(self, route: Route) -> List[Solution]:
        return [*self._generate_solutions(route)]
