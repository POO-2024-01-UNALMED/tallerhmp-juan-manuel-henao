import Persona
import Deportista

class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil,):
        super().__init__(nombre,edad,altura,sexo)
        super().__init__("Futbol",añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista.listaFutbolistas.append(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados=golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil=piernaHabil
    
    def __str__(self):
        return (
            f"Mi nombre es {self.nombre}, soy profesional en el deporte "
            f"{self.deporte}. Tengo {self.edad} años de edad y llevo "
            f"{self.añosParticipando} años en el deporte."
        )