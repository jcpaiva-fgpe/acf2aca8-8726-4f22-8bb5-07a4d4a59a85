class Sprendimas(object):
    def paskutinis(self, n):
        poz, zingsnis, likutis = 1, 1, n
        liko = True
        while likutis > 1:
            if liko or likutis % 2 == 1:
                poz += zingsnis
            zingsnis *= 2
            likutis /= 2
            liko = not liko
        return poz
sp = Sprendimas()
print(sp.paskutinis(9))
