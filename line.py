class PPMGen(object):
    def __init__(self,width,height):
        self.filename = "line.ppm"
        self.contents = '''P3
500 500
255
'''
        self.grid = []
        for row in range(rows):
            self.grid.append([])
            for col in range(cols):
                self.grid[-1].append((0,0,0))

    def draw(self):
        line(120,240,3,4,360)

    def line(self,x0,y0,a,b,x1):
        (x, y) = (x0, y0)
        d = 2*a + b
        while ( x <= x1 ):
        

if (__name__ == "__main__"):
    gen = PPMGen(500,500)
    gen.draw()
