from .inner_vertex_optimizer import GlobalInnerVertexOptimizer, LocalInnerVertexOptimizer

# unused_vertices = self.get_unused_points()
# route = self.randomize_rotation(self.route)
# route = self.randomize_direction(route)

# for index_point, point in enumerate(route):
#     prev_point, next_point = route[index_point-1], route[index_point+1]
#
#     meta = self.find_nearest(next_point, point, prev_point, unused_vertices)
#     if meta['index_unused']:
#         self.swap_vertices(route, unused_vertices, index_point, meta)

#
# @staticmethod
# def randomize_rotation(route: Route) -> Route:
#     pos = random.randint(0, len(route))
#     route = deque(route)
#     route.rotate(-pos)
#     return route
#
# @staticmethod
# def randomize_direction(route: Route) -> Route:
#     return [*reversed(route)] if random.randint(0, 1) else route
#
