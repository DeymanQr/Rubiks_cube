class ThreeD:
    @staticmethod
    def getfake2d(poly):
        return [(x, y) for x, y, z in poly]

    @staticmethod
    def get2d(camera, poly):
        return [(camera.coords[0] + (x - camera.coords[0]) * (camera.plane - camera.coords[2]) / (z - camera.coords[2]),
                 camera.coords[1] + (y - camera.coords[1]) * (camera.plane - camera.coords[2]) / (z - camera.coords[2]))
                for x, y, z in poly]


class Camera:
    def __init__(self, x, y, z, z1):
        self.coords = [x, y, z]
        self.plane = z1

    def update(self):
        pass
