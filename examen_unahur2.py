# parte 2:  se debe agregar un auto eliminandolo del arreglo

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
                self._autos[i]._horaEgreso = horaSalida
                break

    def calcularPlata(self):
        plata = 0
        for auto in self._autos:
            if auto != 0 and auto._horaEgreso is not None:
                horas_estadia = auto._horaEgreso - auto._horaIngreso
                plata += horas_estadia * self._valorHora
        return plata


class Estacionamiento:
    def __init__(self):
        valorHoraDocente = 10  # Asigna el valor correspondiente
        self._sectorDocente = Sector(50, valorHoraDocente)
        self._sectorAlumno = Sector(50, 5)
        self._sectorGeneral = Sector(100, 20)

    def __repr__(self):
        ret = "Sector Docente " + str(self._sectorDocente) + "\n"
        ret += "Sector Alumno " + str(self._sectorAlumno) + "\n"
        ret += "Sector General " + str(self._sectorGeneral)
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

    def egresarAuto(self, sector, patente, horaSalida):
        patente = validarTipo(patente, "patente", str)
        sector = validarTipo(sector, "sector", str)
        if sector == "Docente":
            self._sectorDocente.egresarAuto(patente, horaSalida)
        elif sector == "Alumno":
            self._sectorAlumno.egresarAuto(patente, horaSalida)
        elif sector == "General":
            self._sectorGeneral.egresarAuto(patente, horaSalida)

    def calcularPlataTotal(self):
        return (
            self._sectorDocente.calcularPlata()
            + self._sectorAlumno.calcularPlata()
            + self._sectorGeneral.calcularPlata()
        )


# Crear una instancia de Estacionamiento
estacionamiento = Estacionamiento()

# Ingresar autos
estacionamiento.ingresarAuto("Docente", "aaa", 1)
estacionamiento.ingresarAuto("Docente", "bbb", 2)
estacionamiento.ingresarAuto("Alumno", "ccc", 3)
estacionamiento.ingresarAuto("General", "ddd", 3)
estacionamiento.ingresarAuto("General", "eee", 3)

# Egresar autos
estacionamiento.egresarAuto("Docente", "bbb", 4)
estacionamiento.egresarAuto("Alumno", "ccc", 5)
estacionamiento.egresarAuto("General", "ddd", 5)

# Calcular plata total
plata_total = estacionamiento.calcularPlataTotal()

# Imprimir resultados
print(estacionamiento)
print(plata_total)
