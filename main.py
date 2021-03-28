from sys import argv
from loader import iterate_instances
import random

from optimizers import Route, RandomOptimizer, LocalInnerEdgeOptimizer, GlobalInnerEdgeOptimizer, \
    LocalInnerVertexOptimizer, GlobalInnerVertexOptimizer


def main(instances_path: str, repeat: int):
    for x in iterate_instances(instances_path):
        print()
        fname, distance_matrix = x.name, x.distance_matrix
        for i in range(repeat):
            vertices = distance_matrix.shape[0]
            route = Route([*range(0, 50)])
            random.shuffle(route)
            print('INIT ROUTE', route)
            print(RandomOptimizer.__name__, RandomOptimizer(distance_matrix, route, 0.100)())

            optimizers = [
                GlobalInnerEdgeOptimizer, GlobalInnerVertexOptimizer,
                LocalInnerEdgeOptimizer, LocalInnerVertexOptimizer
            ]

            for Optimizer in optimizers:
                opt = Optimizer(distance_matrix, route)
                print(Optimizer.__name__)
                solution = opt()
                print(solution)


if __name__ == '__main__':
    main(argv[1], int(argv[2]))
