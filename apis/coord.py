from math import *

class Lamcproj():
    def __init__(self):
        self.degrad = pi / 180.0

        grid = 5.0
        self.re = 6371.00877 / grid
        
        self.olon = 126.0 * self.degrad
        self.olat = 38.0 * self.degrad

        self.xo = 210 / grid
        self.yo = 675 / grid

        slat1 = 30.0 * self.degrad
        slat2 = 60.0 * self.degrad

        self.sn = tan(pi/4 + slat2/2) / tan(pi/4 + slat1/2)
        self.sn = log(cos(slat1) / cos(slat2)) / log(self.sn)

        self.sf = tan(pi/4 + slat1/2)
        self.sf = pow(self.sf, self.sn) * cos(slat1) / self.sn

        self.ro = tan(pi/4 + self.olat/2)
        self.ro = self.re * self.sf / pow(self.ro, self.sn)

    def conv(self, lon, lat):
        ra = tan(pi/4 + lat*self.degrad/2)
        ra = self.re * self.sf / pow(ra, self.sn)

        theta = lon * self.degrad - self.olon
        if (theta > pi):
            theta -= 2.0*pi
        elif (theta < -pi):
            theta += 2.0*pi
        theta *= self.sn        
        
        x = self.xo + ra * sin(theta)
        y = self.yo - ra * cos(theta) + self.ro

        x = int(x+1.5)
        y = int(y+1.5)

        return x, y


# test
if __name__ == '__main__':
    lon = 126.98000833333333
    lat = 37.56356944444444

    proj = Lamcproj()

    X, Y = proj.conv(lon, lat)
    print(X, Y)