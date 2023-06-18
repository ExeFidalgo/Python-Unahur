# Nombre del alumno que entrega: _Ezequiel Horacio Fidalgo_
# parte 1: Se debe egresar el auto marcando la hora de salida 
import numpy as np

def validarTipo(variable, nombre, tipo):
    if isinstance(variable, tipo):
        return variable
    else:
        raise Exception("La variable " + nombre + " debe ser de tipo " + str(tipo) + ".")


class Auto:
    def __init__(self, patente, horaIngreso):
        self._patente = validarTipo(patente, "patente", str)
        self._horaIngreso = validarTipo(horaIngreso, "horaIngreso", int)
        self._horaEgreso = None

    def __repr__(self):
        return str(self._patente) + " " + str(self._horaIngreso) + " " + str(self._horaEgreso)


class Sector:
    def __init__(self, capacidad, valorHora):
        self._capacidad = capacidad
        self._valorHora = valorHora
        self._autos = np.zeros(self._capacidad, dtype=Auto)

    def __repr__(self):
        ret = ""
        for i in range(len(self._autos)):
            if self._autos[i] != 0:
                ret += str(self._autos[i]) + ","
        return ret

    def ingresarAuto(self, auto):
        primerLugarLibre = 0
        while self._autos[primerLugarLibre] != 0 and primerLugarLibre < self._capacidad:
            primerLugarLibre += 1

        if primerLugarLibre == self._capacidad:
            raise Exception("No hay lugar")
        else:
            self._autos[primerLugarLibre] = auto

    def egresarAuto(self, patente, horaSalida):
        for i in range(len(self._autos)):
            if self._autos[i] != 0 and self._autos[i]._patente == patente:
                if self._autos[i]._horaEgreso is None:
                    self._autos[i]._horaEgreso = horaSalida
                    return
                else:
                    raise Exception("El auto ya salió anteriormente")

        raise Exception("El auto no se encuentra en el sector")

    def calcularPlata(self):
        plata = 0
        for i in range(len(self._autos)):
            if self._autos[i] != 0 and self._autos[i]._horaEgreso is not None:
                tiempoEstadia = self._autos[i]._horaEgreso - self._autos[i]._horaIngreso
                plata += tiempoEstadia * self._valorHora
        return plata


class Estacionamiento:
    def __init__(self):
        self._sectorDocente = Sector(50, 10)
        self._sectorAlumno = Sector(50, 5)
        self._sectorGeneral = Sector(100, 20)

    def __repr__(self):
        ret = "Sector Docente: " + str(self._sectorDocente) + "\n"
        ret += "Sector Alumno: " + str(self._sectorAlumno) + "\n"
        ret += "Sector General: " + str(self._sectorGeneral) + "\n"
        return ret

    def ingresarAuto(self, sector, patente, horaIngreso):
        patente = validarTipo(patente, "patente", str)
        sector = validarTipo(sector, "sector", str)
        if sector == "Docente":
            self._sectorDocente.ingresarAuto(Auto(patente, horaIngreso))
        elif sector == "Alumno":
            self._sectorAlumno.ingresarAuto(Auto(patente, horaIngreso))
        elif sector == "General":
            self._sectorGeneral.ingresarAuto(Auto(patente, horaIngreso))
        else:
            raise Exception("El sector ingresado no es válido")

    def egresarAuto(self, sector, patente, horaSalida):
        patente = validarTipo(patente, "patente", str)
        sector = validarTipo(sector, "sector", str)
        if sector == "Docente":
            self._sectorDocente.egresarAuto(patente, horaSalida)
        elif sector == "Alumno":
            self._sectorAlumno.egresarAuto(patente, horaSalida)
        elif sector == "General":
            self._sectorGeneral.egresarAuto(patente, horaSalida)
        else:
            raise Exception("El sector ingresado no es válido")

    def calcularPlata(self):
        ret = 0
        ret += self._sectorDocente.calcularPlata()
        ret += self._sectorAlumno.calcularPlata()
        ret += self._sectorGeneral.calcularPlata()
        return ret


e = Estacionamiento()
e.ingresarAuto("Docente", "AAA111", 11)
e.egresarAuto("Docente", "AAA111", 13)
e.ingresarAuto("Alumno", "BBB111", 12)
e.egresarAuto("Alumno", "BBB111", 15)
e.ingresarAuto("General", "CCC111", 10)
e.egresarAuto("General", "CCC111", 13)
print(e)
print("Total a recaudar:", e.calcularPlata())
