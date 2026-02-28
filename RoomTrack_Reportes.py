
import customtkinter as ctk
from tkinter import messagebox
import calculos


def limpiar_contenido(contenido):
    for widget in contenido.winfo_children():
        widget.destroy()

def fecha_existe(fecha_texto):
    partes = fecha_texto.split("-")
    if len(partes) != 3:
        return False

    texto_año, texto_mes, texto_dia = partes

    if not (texto_año.isdigit() and texto_mes.isdigit() and texto_dia.isdigit()):
        return False

    if len(texto_año) != 4 or len(texto_mes) != 2 or len(texto_dia) != 2:
        return False

    año = int(texto_año)
    mes = int(texto_mes)
    dia = int(texto_dia)

  
    if año < 2026:
        return False

    if mes < 1 or mes > 12:
        return False

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    es_bisiesto = (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))
    if es_bisiesto:
        dias_por_mes[1] = 29

    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True
def separar_fecha(fecha_texto):
   
    texto_año, texto_mes, texto_dia = fecha_texto.split("-")
    return int(texto_año), int(texto_mes), int(texto_dia)
def fecha_mas_meses(fecha_texto, cantidad_meses):
    año, mes, dia = separar_fecha(fecha_texto)

    mes = mes + cantidad_meses
    año = año + (mes - 1) // 12
    mes = ((mes - 1) % 12) + 1

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    es_bisiesto = (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))
    if es_bisiesto:
        dias_por_mes[1] = 29

    max_dia = dias_por_mes[mes - 1]
    if dia > max_dia:
        dia = max_dia

    return f"{año:04d}-{mes:02d}-{dia:02d}"

def es_numero_simple(texto):
    texto = texto.strip()
    if texto == "":
        return False
    return texto.replace(".", "", 1).isdigit()


def mostrar_reportes(contenido):
    limpiar_contenido(contenido)

    panel = ctk.CTkFrame(contenido, fg_color="#FFFFFF", corner_radius=18)
    panel.pack(fill="both", expand=True)

    titulo = ctk.CTkLabel(panel,text="Proyecciones",font=("Arial", 22, "bold"),text_color="#111827")
    titulo.pack(anchor="w", padx=24, pady=(20, 6))

    subtitulo = ctk.CTkLabel(panel,text="Genera proyecciones de ocupación por periodo.",font=("Arial", 13),text_color="#6B7280")
    subtitulo.pack(anchor="w", padx=24, pady=(0, 16))

    controles = ctk.CTkFrame(panel, fg_color="#F9FAFB", corner_radius=14)
    controles.pack(fill="x", padx=24, pady=(0, 16))

    ctk.CTkLabel(controles, text="Desde", text_color="#111827").grid(row=0, column=0, sticky="w", padx=16, pady=(14, 6))
    entrada_desde = ctk.CTkEntry(controles, placeholder_text="YYYY-MM-DD", width=160)
    entrada_desde.grid(row=1, column=0, sticky="w", padx=16, pady=(0, 14))

    ctk.CTkLabel(controles, text="Hasta", text_color="#111827").grid(row=0, column=1, sticky="w", padx=16, pady=(14, 6))
    entrada_hasta = ctk.CTkEntry(controles, placeholder_text="YYYY-MM-DD", width=160)
    entrada_hasta.grid(row=1, column=1, sticky="w", padx=16, pady=(0, 14))

    ctk.CTkLabel(controles, text="Temporada", text_color="#111827").grid(row=0, column=2, sticky="w", padx=16, pady=(14, 6))

    temporada_seleccionada = ctk.StringVar(value="alta")
    opcion_alta = ctk.CTkRadioButton(controles, text="Alta", variable=temporada_seleccionada, value="alta")
    opcion_baja = ctk.CTkRadioButton(controles, text="Baja", variable=temporada_seleccionada, value="baja")
    opcion_alta.grid(row=1, column=2, sticky="w", padx=16, pady=(0, 0))
    opcion_baja.grid(row=2, column=2, sticky="w", padx=16, pady=(0, 14))

    ctk.CTkLabel(controles, text="Ocupación inicial", text_color="#111827").grid(row=2, column=0, sticky="w", padx=16, pady=(0, 6))
    entrada_ocupacion_inicial = ctk.CTkEntry(controles, placeholder_text="Ej: 18", width=160)
    entrada_ocupacion_inicial.grid(row=3, column=0, sticky="w", padx=16, pady=(0, 14))

    ctk.CTkLabel(controles, text="Total habitaciones", text_color="#111827").grid(row=2, column=1, sticky="w", padx=16, pady=(0, 6))
    entrada_total_habitaciones = ctk.CTkEntry(controles, placeholder_text="Ej: 60", width=160)
    entrada_total_habitaciones.grid(row=3, column=1, sticky="w", padx=16, pady=(0, 14))

    controles.grid_columnconfigure(3, weight=1)
    resumen = ctk.CTkFrame(panel, fg_color="transparent")
    resumen.pack(fill="x", padx=24, pady=(0, 16))
    resumen.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def cuadro_resumen(parent, columna, titulo_cuadro, valor_inicial):
        cuadro = ctk.CTkFrame(parent,fg_color="#FFFFFF",corner_radius=16,border_width=1,border_color="#E5E7EB")
        cuadro.grid(row=0, column=columna, sticky="nsew", padx=8)

        ctk.CTkLabel(cuadro, text=titulo_cuadro, text_color="#6B7280").pack(anchor="w", padx=16, pady=(12, 0))

        etiqueta_valor = ctk.CTkLabel(cuadro,text=valor_inicial,font=("Arial", 22, "bold"),text_color="#111827")
        etiqueta_valor.pack(anchor="w", padx=16, pady=(0, 12))
        return etiqueta_valor

    etiqueta_ocupacion = cuadro_resumen(resumen, 0, "Ocupación", "— habs")
    etiqueta_porcentaje = cuadro_resumen(resumen, 1, "Porcentaje de ocupación", "— %")
    etiqueta_libres = cuadro_resumen(resumen, 2, "Hab. libres", "—")

    resultados = ctk.CTkFrame(panel, fg_color="#FFFFFF", corner_radius=14, border_width=1, border_color="#E5E7EB")
    resultados.pack(fill="both", expand=True, padx=24, pady=(0, 24))

    ctk.CTkLabel(resultados,text="Resultados del reporte",text_color="#111827",font=("Arial", 14, "bold")).pack(anchor="w", padx=16, pady=(14, 8))

    contenedor_filas = ctk.CTkFrame(resultados, fg_color="transparent")
    contenedor_filas.pack(fill="both", expand=True, padx=12, pady=(0, 12))

    def limpiar_filas_resultados():
        for widget in contenedor_filas.winfo_children():
            widget.destroy()

    def agregar_fila_resultado(fecha, tipo, valor):
        fila = ctk.CTkFrame(contenedor_filas, fg_color="transparent")
        fila.pack(fill="x", pady=2)

        ctk.CTkLabel(fila, text=fecha, width=140, anchor="w", text_color="#111827").pack(side="left", padx=(12, 0), pady=10)
        ctk.CTkLabel(fila, text=tipo, width=180, anchor="w", text_color="#111827").pack(side="left", pady=10)
        ctk.CTkLabel(fila, text=valor, anchor="w", text_color="#111827").pack(side="left", pady=10)

    def generar_reporte():
        fecha_inicio = entrada_desde.get().strip()
        fecha_fin = entrada_hasta.get().strip()
        texto_ocupacion = entrada_ocupacion_inicial.get().strip()
        texto_total = entrada_total_habitaciones.get().strip()
        temporada = temporada_seleccionada.get()
        
        if fecha_inicio == "" or fecha_fin == "" or texto_ocupacion == "" or texto_total == "":
            messagebox.showerror("Error", "Completa todos los campos.")
            return


        if not fecha_existe(fecha_inicio) or not fecha_existe(fecha_fin):
            messagebox.showerror("Error", "Fecha inválida. Usa YYYY-MM-DD y un día real (ej: 2026-02-28).")
            return

   
        fecha_minima = "2026-02-02"
        if separar_fecha(fecha_inicio) < separar_fecha(fecha_minima):
            messagebox.showerror("Error", "La fecha inicial debe ser desde 2026-02-02 en adelante.")
            return


        if separar_fecha(fecha_fin) < separar_fecha(fecha_inicio):
            messagebox.showerror("Error", "La fecha final no puede ser anterior a la fecha inicial.")
            return


        fecha_maxima = fecha_mas_meses(fecha_inicio, 2)
        if separar_fecha(fecha_fin) > separar_fecha(fecha_maxima):
            messagebox.showerror("Error", "El rango máximo permitido es de 2 meses.")
            return


        if not es_numero_simple(texto_ocupacion):
            messagebox.showerror("Error", "La ocupación inicial debe ser un número.")
            return

        if not es_numero_simple(texto_total):
            messagebox.showerror("Error", "El total de habitaciones debe ser un número.")
            return

        ocupacion_inicial = float(texto_ocupacion)
        total_habitaciones = float(texto_total)

        if total_habitaciones <= 0:
            messagebox.showerror("Error", "El total de habitaciones debe ser mayor a 0.")
            return

        resultado = calculos.calculo_f(fecha_inicio, fecha_fin, ocupacion_inicial, total_habitaciones, temporada)

        if resultado is None:
            messagebox.showerror("Error", "No se pudo calcular el reporte con las fechas ingresadas.")
            return

        promedio, porcentaje = resultado
        etiqueta_porcentaje.configure(text=f"{round(porcentaje, 2)}%")

        if porcentaje > 100:
            messagebox.showwarning("Aviso", "La ocupación supera el 100%. Revisa la ocupación inicial o el total de habitaciones.")


        etiqueta_ocupacion.configure(text=f"{round(promedio, 2)} habs")

        habitaciones_libres = total_habitaciones - promedio
        if habitaciones_libres < 0:
            habitaciones_libres = 0
        etiqueta_libres.configure(text=str(round(habitaciones_libres, 2)))


        limpiar_filas_resultados()
        agregar_fila_resultado(fecha_inicio, "Temporada", "Alta" if temporada == "alta" else "Baja")
        agregar_fila_resultado(fecha_inicio, "Ocupación prom.", f"{promedio} habs")
        agregar_fila_resultado(fecha_inicio, "Ocupación (%)", f"{porcentaje}%")

        messagebox.showinfo("Listo", "Reporte generado correctamente.")

    boton_generar = ctk.CTkButton(controles, text="Generar Proyeccion", command=generar_reporte)
    boton_generar.grid(row=3, column=2, sticky="e", padx=16, pady=(0, 14))
    btn_volver= ctk.CTkButton(controles, text="Volver", fg_color="#EA4F4F",command=lambda: contenido.mostrar_inicio() ,text_color="#E5E7EB")
    btn_volver.grid(row=3, column=3, sticky="w", padx=16, pady=(0, 14))