##Primera clase Trabajador
from datetime import time, date, datetime, timedelta

entrada1 = "08:30:00"
salida1 = "16:30:00"
entrada2 = "10:00:00"
salida2 = "18:30:00"
entrada3 = "13:00:00"
salida3 = "21:00:00"

hora_entrada1 = time.fromisoformat(entrada1)
hora_salida1 = time.fromisoformat(salida1)
hora_entrada2 = time.fromisoformat(entrada2)
hora_salida2 = time.fromisoformat(salida2)
hora_entrada3 = time.fromisoformat(entrada3)
hora_salida3 = time.fromisoformat(salida3)

turnos = [(hora_entrada1, hora_salida1),
          (hora_entrada2, hora_salida2),
          (hora_entrada3, hora_salida3)]

def diferencia(hora1, hora2):
    dt1 = datetime.combine(date.today(), hora1)
    dt2 = datetime.combine(date.today(), hora2)
    return abs(dt1 - dt2)

def horario_mas_cercano(hora, horarios, tolerancia = timedelta(minutes=30)):
    mejor = None
    menor = tolerancia
    for entrada, salida in horarios:
        dif = diferencia(hora, entrada)
        if dif <= menor:
            menor = dif
            mejor = (entrada, salida)
    return mejor

class Trabajador:
    def __init__(self, nombre, edad, area_trabajo, horario_trabajo):
        self.nombre = nombre
        self.edad = edad
        self.area_trabajo = area_trabajo
        self.horario_trabajo = horario_trabajo
        self.historial_asistencia = []

    ##registro del trabajador con nombre, edad y area de trabajo

    def registro_trabajador(self):
        return f"nombre trabajador:\n-{self.nombre}\nedad trabajador:\n-{self.edad}\narea de trabajo:\n-{self.area_trabajo}\n"

    ##funcion para marcar asistencia donde se registrara la hora donde se marco asistencia

    def horario_trabajador(self, entrada):
        turno = horario_mas_cercano(entrada, [self.horario_trabajo])
        if turno:
            hora_entrada, hora_salida = turno
            return f"el horario del trabajador es de:\n-{hora_entrada} - {hora_salida}"
        return f"horario del trabajador {self.nombre} no registrado en el sistema."


    def agregar_asistencia(self, asistencia):
        registro = asistencia.registro_asistencia()
        if registro:
            self.historial_asistencia.append(registro)
            return True
        return False
            

    ##funcion que almacene el historial de asistencia
    def historial(self):
        return [r for r in self.historial_asistencia if r["asistio"]]
        

## clase asistencia contendra datos de la asistencia del trabajador como asistencia 
##fecha de la marca de asistencia, hora de entrada, hora de salida

class Asistencia:
    def __init__(self,trabajador, fecha, hora_entrada, hora_salida,  asistio_si_no):
        self.trabajador = trabajador
        self.fecha = fecha
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.asistio_si_no = asistio_si_no

## se registra el horario de entrada y la fecha de asistencia

    def fecha_hora_entrada(self):
        dia_fecha = date.fromisoformat(self.fecha)
        entrada = time.fromisoformat(self.hora_entrada)
        return f"\nFecha de registro:\n-{dia_fecha}\nHora de entrada:\n-{entrada}"

##se registra el horario de salida

    def marca_de_salida(self):
        hora_salida = time.fromisoformat(self.hora_salida)
        return f"Hora en que el trabajador marco salida:\n-{hora_salida}"

##registro de asistencia diaria

    def registro_asistencia(self):
        if self.asistio_si_no:
            return {"trabajador": self.trabajador,
                                    "fecha": self.fecha,
                                    "horario de entrada": self.hora_entrada,
                                    "horario de salida": self.hora_salida,
                                    "asistio": self.asistio_si_no
                                    }
        return None




dia_hoy= "2026-10-03"


instancia_trabajador1 = Trabajador("alexis sanchez", 27, "informatica", (hora_entrada1, hora_salida1))
instancia_trabajador2 = Trabajador("jose lopez", 30, "call center", (hora_entrada3, hora_salida3))
instancia1 = Asistencia("vicente ramirez", dia_hoy, "08:45:30", "16:20:38", True)
instancia2 = Asistencia("jose lopez", dia_hoy, "00:00:00", "00:00:00", False)

print("------------Datos del trabajador------------")
print(instancia_trabajador1.registro_trabajador())
print(instancia_trabajador1.horario_trabajador(time.fromisoformat(instancia1.hora_entrada)))
print("------------Registro de entrada-------------")
print(instancia1.fecha_hora_entrada())
print(instancia1.marca_de_salida())
print("------------Registro salida-------------")
instancia_trabajador1.agregar_asistencia(instancia1)
if not instancia_trabajador2.agregar_asistencia(instancia2):
    print(f"el trabajador {instancia_trabajador2.nombre} no asistio el dia {instancia2.fecha}")
print(instancia_trabajador1.historial())
