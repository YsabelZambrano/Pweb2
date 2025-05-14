from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = [value[::-1] for value in self.img]
    return Picture(vertical)


  def horizontalMirror(self):
    horizontal = self.img[::-1]
    return Picture(horizontal)


  def negative(self):
    neg = [
        ''.join([self._invColor(c) for c in row])
        for row in self.img
    ]
    return Picture(neg)


  def join(self, p):
    nueva_img = [
        self.img[i] + p.img[i]
        for i in range(len(self.img))
    ]
    return Picture(nueva_img)

  def up(self, p):
    return Picture(p.img + self.img)


  def under(self, p):
    nueva_img = []
    for row1, row2 in zip(self.img, p.img):
        nueva_img.append(''.join([c2 if c2 != ' ' else c1 for c1, c2 in zip(row1, row2)]))
    return Picture(nueva_img)

  
  def horizontalRepeat(self, n):
    nueva_img = [
        line * n for line in self.img
    ]
    return Picture(nueva_img)


  def verticalRepeat(self, n):
    return Picture(self.img * n)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

