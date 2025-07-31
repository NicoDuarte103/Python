class persona():

    def __init__(self,nombre,edad):
        self.nombre = nombre;
        self.edad  = edad;
    def __str__(self):
        return (f"nombre: {self.nombre} edad: {self.edad}")

class estudiante(persona):
    def __init__(self,nombre,edad,curso):
        super().__init__(nombre,edad);
        self.curso = curso;
    def __str__(self):
        return (f"nombre: {self.nombre} edad: {self.edad} curso: {self.curso}")

ejecucion1 = persona("tito",20);
ejecucion2 = estudiante("tita",21,"tercero")
print(ejecucion1)
print(ejecucion2)

