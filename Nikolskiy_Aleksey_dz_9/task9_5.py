class Stationery:
    title = 'No_name'

    def draw(self):
        print("Starting rendering")


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print("Rendering by Pen")


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print("Rendering by Pencil")


class Marker(Stationery):
    title = 'Marker'

    def draw(self):
        print("Rendering by Marker")


default = Stationery()
pen1 = Pen()
pencil1 = Pencil()
marker1 = Marker()

list_of_st = [default, pen1, pencil1, marker1]

for i in list_of_st:
    i.draw()
