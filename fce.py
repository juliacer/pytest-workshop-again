from math import pi


def ellipse_area():
    a = float(input('Zadej polomer a:'))
    b = float(input('Zadej polomer b:'))
    obsah = a * b * pi
    print('Obsah elipsy je', obsah)


#def test_ellipse_area_circle_is_pi():
#    ellipse_area()
