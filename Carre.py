class Carre:
    """
    Classe Carré
    Split la map en carré
    """

    def __init__(self, point_origine, point_final):
        self.point_origine = point_origine
        self.point_final = point_final

    """
    Définit si un cadeau aux coordonnés x_gift, y_gift est dans le carré
    """
    def in_scale(self, x_gift, y_gift):
        x_origine, y_origine = self.point_origine
        x_final, y_final = self.point_final
        if (x_origine <= x_gift <= x_final) and (y_origine >= y_gift >= y_final):
            return True
        return False
