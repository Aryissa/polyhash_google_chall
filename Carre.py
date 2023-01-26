
class Carre:
    """
    Classe Carré
    Permet la création de carré
    """
    
    def __init__(self, point_origine, point_final):
        """
        constructeur de la classe Carre
        point d'origine: point situé en haut à gauche
        point_final: point situé en bas à droite
        """
        self.point_origine = point_origine
        self.point_final = point_final

    
    def in_scale(self, x_gift, y_gift):
        """
        Retourne si et seulement si un point se situe dans le carre
        x_gift: position sur l'axe x du point
        y_gift: position sur l'axe des y du point
        """
        x_origine, y_origine = self.point_origine
        x_final, y_final = self.point_final
        if (x_origine <= x_gift <= x_final) and (y_origine >= y_gift >= y_final):
            return True
        return False
