class animal():
    def __init__(self):
        pass
    def hablar(self):
        print("el animal hablass")

class perro(animal):

    def __init__(self):
        pass

    def muger(self):
        print("el perro muge")


ejecucion1 = animal()
ejecucion1.hablar()

ejecucion2=perro()
ejecucion2.hablar()
ejecucion2.muger()