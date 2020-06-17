from random import randint

class Participant():


    def __init__(self, p, g, participant):
        self.p = p
        self.g = g
        self.a = randint(1,self.p-1)
        self.participant = participant

    def seed(self):
        """
        Generador de la parte propia del intercambio de Diffie-Hellmann
        """
        participant = (self.g**self.a) % self.p
        return participant
        

    def exchange(self):
        """
        Adquiero el número de la otra persona y calculo mi propia llave.
        """
        s = (self.participant.seed()**self.a) % self.p
