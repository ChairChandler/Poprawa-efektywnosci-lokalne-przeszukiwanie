from .base import TimerOptimizer, Route, Solution
import numpy as np
import random


class RandomOptimizer(TimerOptimizer):
    def _find_solution(self):
        best_solution = Solution(np.inf, self.route)
        route: Route = self.route[:]

        while True:
            random.shuffle(route)

            score = self._calculate_score(route)
            if score < best_solution.cost:
                best_solution = Solution(score, route[:])

            yield best_solution
