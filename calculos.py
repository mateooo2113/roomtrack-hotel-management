from datetime import datetime



def calc_dias(fecha_inicio, fecha_fin):
    fecha1 = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha2 = datetime.strptime(fecha_fin, "%Y-%m-%d")
    return (fecha2 - fecha1).days + 1 


def r_temp(temporada):
    if temporada == "alta":
        return 1.05
    else:
        return 0.97


def limitar_valor(valor, minimo, maximo):
    if valor < minimo:
        return minimo
    elif valor > maximo:
        return maximo
    else: 
        return valor


def calculo_f(fecha_inicio, fecha_fin, ocupacion_inicial, total_habitaciones, temporada):

    if total_habitaciones <= 0:
        return None

    dias = calc_dias(fecha_inicio, fecha_fin)
    if dias <= 0:
        return None

    ocupacion_inicial = limitar_valor(ocupacion_inicial, 0, total_habitaciones)
    razon = r_temp(temporada)

    if razon == 1:
        suma_ocupacion = ocupacion_inicial * dias
    else:
        suma_ocupacion = ocupacion_inicial * ((razon ** dias) - 1) / (razon - 1)

    promedio = suma_ocupacion / dias
    promedio = limitar_valor(promedio, 0, total_habitaciones)

    porcentaje = (promedio / total_habitaciones) * 100

    return round(promedio, 2), round(porcentaje, 2)
