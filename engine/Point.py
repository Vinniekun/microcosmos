class Point:
    def __init__(self, x=0, y=0):
        if type(x) is list:
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    def xy(self):
        return [self.x, self.y]

    def ixy(self):
        return [int(self.x), int(self.y)]

    def translate(self, vec):
        self.x += vec.x
        self.y += vec.y

    def rotate(self, alfa, root=None):
        if root is None:
            root = Point()
        x, y = self.x - root.x, self.y - root.y
        self.x = x * cos(alfa) - y * sin(alfa) + root.x
        self.y = x * sin(alfa) + y * cos(alfa) + root.y

    def scale(self, rate):
        if rate.__class__ != Point:
            rate = Point(rate, rate)
        self.x *= rate.x
        self.y *= rate.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return '<Point (' + str(self.x) + ', ' + str(self.y) + ')>'
