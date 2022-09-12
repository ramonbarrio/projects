class Knot:
    def __init__(self, id, mass, address, coord, fixed=False, connected_bridges=[]):
        self.id = id
        self.mass = mass
        self.address = address.copy()
        self.coord = coord.copy()

    def __str__(self):
        return 'id:{id}, mass:{mass}, address:{address}, coord:{coord}'.format(id=self.id, mass=self.mass, address=self.address, coord=self.coord)


class Bridge:
    def __init__(self, id, k, l, start, end):
        self.id = id
        self.k = k
        self.l = l
        self.start = start
        self.end = end
        self.connection = [start, end]
        self.live = True

    def __str__(self):
        return 'id:{id}, start:{start}, end:{end}'.format(id=self.id, start=self.start, end=self.end)


class Cloth:
    def __init__(self, knots_list, bridges_list):
        self.knots_dict = self.build_knots_dict(knots_list)
        self.bridges_dict = self.build_bridges_dict(bridges_list)
        #self.knot_bridge_connection_matrix = self.build_knot_bridge_connection_matrix()

    def build_knots_dict(self, knots_list):
        knots_dict = {}
        for knot in knots_list:
            knots_dict[knot.id] = knot
        return knots_dict

    def build_bridges_dict(self, bridges_list):
        bridges_dict = {}
        for bridge in bridges_list:
            bridges_dict[bridge.id] = bridge
        return bridges_dict

    def build_knot_bridge_connection_matrix(self):
        connection_matrix = [
            [0 for i in range(len(self.knots_dict))] for j in range(len(self.bridges_dict))]
        for bridge_id in self.bridges_dict:
            connection_matrix[bridge_id][self.bridges_dict[bridge_id].start] = 1
            connection_matrix[bridge_id][self.bridges_dict[bridge_id].end] = 1

    def get_lines_to_render(self):
        lines_to_render = [0]*len(self.bridges_dict)
        for id, bridge in self.bridges_dict.items():
            lines_to_render[id] = self.knots_dict[bridge.start].coord + \
                self.knots_dict[bridge.end].coord

        return lines_to_render


class ClothMesh:
    def __init__(self, vertices, polygons):
        self.vertices = vertices
        self.polygons = polygons
