from sympy import mod_inverse
class Curve():

    def __init__(self, A, B, p):
        """
        Construcutor de clase que va a representar a la curva elíptica de la
        forma y^2 = x^3 + Ax + B (mod p).
        :param A: primer coeficiente de la curva.
        :param B: segundo coeficiente de la curva.
        :param p: el tamaño del campo sobre el cual se hace la curva.
        """
        self.A = A
        self.B = B
        self.p = p

    def is_on_curve(self, point):
        """
        Método de clase regresa true si un punto está en la curva, éste punto 
        está representado a manera de tupla, como (x, y).
        :param point: Una tupla de enteros representando a un punto.
        :return: true si el punto está en la curva, false en otro caso.
        """
        if point == None:
            return True
        else:
            x = point[0]
            y = point[1]
            curvaI = pow(y,2)%self.p
            curvaD = (pow(x,3) + (self.A*x) + self.B) % self.p
            if curvaI == curvaD:
                return True
            else:
                return False
        



    def determinant(self):
        """
        Regresa el determinante de una curva, recordando que su determinante
        es calculado de la forma 4A^3 + 27B^2.
        :return: El entero con el valor del determinante.
        """
        determinante = (4*self.A**3) + (27*self.B**2)
        return determinante

def add_points(p, q, curve):
    """
    Dados un par de puntos y una curva elíptica, calcula el punto de la suma
    bajo la curva elíptica recibida como parámetro, se asume que p y q ya 
    forman parte de la curva.
    :param p: una tupla representando un punto de la curva.
    :param q: una tupla representando un punto de la curva.
    :param curve: una instancia de la clase de este script.
    :return: Una tupla que contiene el resultado de la suma o None en caso de
    que haya sido evaluada al punto infinito.
    """
    x1 = p[0] 
    x2 = q[0]
    y1 = p[1]
    y2 = q[1]

    if (x1 == x2 and y1 != y2) or q == (x1,(-y1%curve.p)):
        return None
    else:
        if p == q:
            lam = (3*pow(x1,2) + curve.A) * mod_inverse(2*y1,curve.p)
        else:
            lam = (y1-y2) * mod_inverse((x1-x2),curve.p)
    
        x3 = (pow(lam,2)-x1-x2)%curve.p
        y3 = (lam*(x1-x3)-y1)%curve.p
    return (x3,y3)

def scalar_multiplication(p, k, curve):
    """
    Dado un escalar del campo, k, calcula el punto kP bajo la definición
    de curvas elípticas.
    :param p: una tupla representando un punto de la curva.
    :param k: el escalar a multiplicar por el punto. 
    :param curve: la curva sobre la cual se calculan las operaciones.
    :return: una tupla representando a kP o None si al sumar ese punto cayó 
    en algún momento al punto infinito.
    """
    if k == 1:
        return p
    else:
        return add_points(p,scalar_multiplication(p,k-1,curve),curve)
