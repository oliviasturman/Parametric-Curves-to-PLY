class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Color:
    def __init__(self,r,g,b,name=''):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

RED = Color(255,0,0,'red')
BLUE = Color(0,0,255,'blue')
GREEN = Color(0,255,0,'green')
BLACK = Color(0,0,0,'black')
WHITE = Color(255,255,255,'white')

class PointCloud:
    def __init__(self, points=[]):
        self.points = points

    def add(self, point):
        self.points.append(point)

    def normalize(self):
        xmax = max([p.x for p in self.points])
        xmin = min([p.x for p in self.points])
        xrng = xmax - xmin
        ymax = max([p.y for p in self.points])
        ymin = min([p.y for p in self.points])
        yrng = ymax - ymin
        zmax = max([p.z for p in self.points])
        zmin = min([p.z for p in self.points])
        zrng = zmax - zmin

        maxrng = max([xrng, yrng, zrng])
        
        newpoints = []
        for p in self.points:
            newx = (p.x - xmin) / maxrng
            newy = (p.y - ymin) / maxrng
            newz = (p.z - zmin) / maxrng
            newpoints.append(Point(newx,newy,newz))

        self.points = newpoints

def dist(p1,p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)

class Shape:
    def __init__(self,cloud,color=None,number=3):
        self.vertices = cloud
        self.color = color
        self.faces = []
        self.number = number

    def create_faces_random_number(self,num):
        faces = []
        facecnt = {}

        edgequeue = []
        numv = len(self.vertices.points)
        for i in range(numv):
            e = (i,i+1) if i < numv-1 else (0,i)
            edgequeue.append(e)

        while edgequeue != []:
            e = edgequeue.pop(0)

            try:
                if facecnt[e] == 2:
                    continue
            except KeyError:
                facecnt[e] = 0

            p3 = (e[0] + num) % numv
            i = 0
            while True:
                print(e,edgequeue)
                if p3 == e[0] or p3 == e[1]:
                    p3 = (p3 + i + num) % numv
                    i += 1
                else:
                    srt = sorted([e[0],e[1],p3])
                    a,b,c = srt[0],srt[1],srt[2]
                    failed = False
                    for pr in [(a,b),(a,c),(b,c)]:
                        try:
                            if facecnt[pr] == 2:
                                failed = True
                        except KeyError:
                            facecnt[pr] = 0
                    if failed:
                        p3 = (p3 + i + num) % numv
                        i += 1
                    else:
                        faces.append((a,b,c))
                        for pr in [(b,c),(a,c),(a,b)]:
                            facecnt[pr] += 1
                            if facecnt[pr] < 2:
                                edgequeue.append(pr)
                        break

        self.faces = faces

    def create_faces_number_easy(self,num):
        faces = []
        numv = len(self.vertices.points)
        if numv < 4:
            self.faces = faces

        for i in range(numv):
            for j in range(num):
                v2 = (i + j + 1) % numv
                v3 = (i + j + 2) % numv
                faces.append((i,v2,v3))
        self.faces = faces

    def create_all_faces(self):
        faces = []
        numpts = len(self.vertices.points)
        if numpts < 4:
            self.faces = faces
            return

        for i in range(numpts-2):
            for j in range(i+1,numpts-1):
                for k in range(j+1,numpts):
                    faces.append((i,j,k))
        self.faces = faces

    # current mode: create all faces
    def create_faces(self):
        self.create_faces_number_easy(self.number)
