from sys import argv
from loader import iterate_instances
import random

from optimizers import Route, RandomOptimizer, LocalInnerEdgeOptimizer, GlobalInnerEdgeOptimizer, \
    LocalInnerVertexOptimizer, GlobalInnerVertexOptimizer


def main(instances_path: str, repeat: int):
    for fname, distance_matrix in iterate_instances(instances_path):
        for i in range(repeat):
            vertices = distance_matrix.shape[0]
            route = Route([*range(vertices)])
            random.shuffle(route)
            RandomOptimizer(distance_matrix, route, 100)

            optimizers = [
                GlobalInnerEdgeOptimizer, GlobalInnerVertexOptimizer,
                LocalInnerEdgeOptimizer, LocalInnerVertexOptimizer
            ]

            for Optimizer in optimizers:
                opt = Optimizer(distance_matrix, route)
                delta, route = opt()


if __name__ == '__main__':
    main(argv[1], int(argv[2]))
