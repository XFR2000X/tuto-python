class player:

    def __init__(self, pseudo,helth,attack):
      self.pseudo=pseudo
      self.health = helth
      self.attack= attack
      print('bienvenue au joueur', self.pseudo, "/poinst de vie:",self.health,"/ Attaque:", self.attack)

    def get_pseudo(self):
        return self.pseudo



player1=player('graven',20,3)

player2 =player('bob',20,5)
