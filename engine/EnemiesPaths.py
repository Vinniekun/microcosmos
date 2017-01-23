
class EnemiesPaths:

    def getPath(id):

        # rectangle
        if id == 0:
            return [[0, - 100], [-100, -100], [-100, 0], [0, 0]]
        # triangle
        elif id == 1:
            return [[-160, -120], [-320, 0], [0, 0]]
        elif id == 2:
            return [[0, -50], [0, 0]]
        else:
            return []

    def getSteps(id):

        if id == 0:
            return [[0, -4], [-4, 0], [0, 4], [4, 0]]
        elif id == 1:
            return [[-4, -3], [-4, 3], [4, 0]]
        elif id == 2:
            return [[0, -5], [0, 5]]
        else:
            return []

    def getEnemyPath(id):
        return EnemiesPaths.getPath(id), EnemiesPaths.getSteps(id)
