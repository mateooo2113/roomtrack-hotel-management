import customtkinter as ctk
from tkinter import messagebox


HABITACIONES = ["001","002","003","004","005","006","007","008","009","010"]
INFO_HAB = {
    "001": {"tipo": "Simple", "estado": "Libre"},
    "002": {"tipo": "Doble",  "estado": "Libre"},
    "003": {"tipo": "Suite",  "estado": "Libre"},
    "004": {"tipo": "Doble",  "estado": "Libre"},
    "005": {"tipo": "Simple", "estado": "Libre"},
    "006": {"tipo": "Simple", "estado": "Libre"},
    "007": {"tipo": "Doble",  "estado": "Libre"},
    "008": {"tipo": "Suite",  "estado": "Libre"},
    "009": {"tipo": "Simple", "estado": "Libre"},
    "010": {"tipo": "Doble",  "estado": "Libre"},
}




def limpiar_contenido(contenido):
    for widget in contenido.winfo_children():
        widget.destroy()


def mostrar_habitaciones(contenido):
    limpiar_contenido(contenido)

    panel = ctk.CTkFrame(contenido, fg_color="#FFFFFF", corner_radius=18)
    panel.pack(fill="both", expand=True)

    titulo = ctk.CTkLabel(panel, text="Habitaciones y disponibilidad",font=("Arial", 22, "bold"), text_color="#111827")
    titulo.pack(anchor="w", padx=24, pady=(20, 6))

    subtitulo = ctk.CTkLabel(panel, text="Consulta el estado de habitaciones y gestiona su disponibilidad.",font=("Arial", 13), text_color="#6B7280")
    subtitulo.pack(anchor="w", padx=24, pady=(0, 16))

    resumen = ctk.CTkFrame(panel, fg_color="transparent")
    resumen.pack(fill="x", padx=24, pady=(0, 16))
    resumen.grid_columnconfigure((0, 1, 2), weight=1)

    total_box = ctk.CTkFrame(resumen, fg_color="#F9FAFB", corner_radius=16)
    total_box.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
    lbl_total_num = ctk.CTkLabel(total_box, text="0", font=("Arial", 22, "bold"), text_color="#111827")
    ctk.CTkLabel(total_box, text="Total", text_color="#6B7280").pack(anchor="w", padx=16, pady=(12, 0))
    lbl_total_num.pack(anchor="w", padx=16, pady=(0, 12))

    libres_box = ctk.CTkFrame(resumen, fg_color="#F9FAFB", corner_radius=16)
    libres_box.grid(row=0, column=1, sticky="nsew", padx=12)
    lbl_libres_num = ctk.CTkLabel(libres_box, text="0", font=("Arial", 22, "bold"), text_color="#111827")
    ctk.CTkLabel(libres_box, text="Libres", text_color="#6B7280").pack(anchor="w", padx=16, pady=(12, 0))
    lbl_libres_num.pack(anchor="w", padx=16, pady=(0, 12))

    ocup_box = ctk.CTkFrame(resumen, fg_color="#F9FAFB", corner_radius=16)
    ocup_box.grid(row=0, column=2, sticky="nsew", padx=(12, 0))
    lbl_ocup_num = ctk.CTkLabel(ocup_box, text="0", font=("Arial", 22, "bold"), text_color="#111827")
    ctk.CTkLabel(ocup_box, text="Ocupadas", text_color="#6B7280").pack(anchor="w", padx=16, pady=(12, 0))
    lbl_ocup_num.pack(anchor="w", padx=16, pady=(0, 12))

    controles = ctk.CTkFrame(panel, fg_color="transparent")
    controles.pack(fill="x", padx=24, pady=(0, 12))

    filtro = ctk.CTkOptionMenu(controles, values=["Todas", "Libres", "Ocupadas"], width=160)
    filtro.pack(side="left")

    buscar = ctk.CTkEntry(controles, placeholder_text="Buscar habitación (ej: 001)", width=240)
    buscar.pack(side="left", padx=12)

    nueva = ctk.CTkEntry(controles, placeholder_text="Agregar (ej: 011)", width=180)
    nueva.pack(side="left", padx=12)
    tipo_nuevo = ctk.CTkOptionMenu(controles, values=["Simple", "Doble", "Suite"], width=140)
    tipo_nuevo.set("Simple")
    tipo_nuevo.pack(side="left", padx=12)

    lista = ctk.CTkFrame(panel, fg_color="#FFFFFF", corner_radius=14,border_width=1, border_color="#E5E7EB")
    lista.pack(fill="both", expand=True, padx=24, pady=(0, 24))

    header = ctk.CTkFrame(lista, fg_color="#F9FAFB", corner_radius=12)
    header.pack(fill="x", padx=12, pady=(12, 6))

    ctk.CTkLabel(header, text="Habitación", text_color="#6B7280", width=120, anchor="w")\
        .pack(side="left", padx=(12, 0), pady=10)
    ctk.CTkLabel(header, text="Tipo", text_color="#6B7280", width=160, anchor="w")\
        .pack(side="left", pady=10)
    ctk.CTkLabel(header, text="Estado", text_color="#6B7280", width=120, anchor="w")\
        .pack(side="left", pady=10)

    cont_filas = ctk.CTkFrame(lista, fg_color="transparent")
    cont_filas.pack(fill="both", expand=True, padx=12, pady=(0, 12))


    def actualizar_resumen():
        total = len(HABITACIONES)
        libres = 0
        ocupadas = 0

        for h in HABITACIONES:
            estado = INFO_HAB.get(h, {}).get("estado", "Libre")
            if estado.lower() == "libre":
                libres += 1
            else:
                ocupadas += 1

        lbl_total_num.configure(text=str(total))
        lbl_libres_num.configure(text=str(libres))
        lbl_ocup_num.configure(text=str(ocupadas))

        
    def dibujar_tabla():
        for w in cont_filas.winfo_children():
            w.destroy()

        texto_buscar = buscar.get().strip()
        estado_filtro = filtro.get()
        
        habs = sorted(HABITACIONES)

        if texto_buscar != "":
            habs = [h for h in habs if texto_buscar in h]

        if estado_filtro != "Todas":
            habs = [h for h in habs if INFO_HAB.get(h, {}).get("estado", "Libre").lower() == estado_filtro.lower()]


        if len(habs) == 0:
            ctk.CTkLabel(cont_filas, text="No hay resultados.", text_color="#6B7280")\
                .pack(anchor="w", padx=12, pady=10)
            return

        for hab in habs:
            tipo = INFO_HAB.get(hab, {}).get("tipo", "Simple")
            estado = INFO_HAB.get(hab, {}).get("estado", "Libre")

            fila = ctk.CTkFrame(cont_filas, fg_color="transparent")
            fila.pack(fill="x", pady=2)

            ctk.CTkLabel(fila, text=hab, text_color="#111827", width=120, anchor="w")\
                .pack(side="left", padx=(12, 0), pady=10)
            ctk.CTkLabel(fila, text=tipo, text_color="#111827", width=160, anchor="w")\
                .pack(side="left", pady=10)

            estado_color = "#111827"
            if estado.lower() == "libre":
                estado_color = "#16A34A"
            elif estado.lower() == "ocupada":
                estado_color = "#DC2626"

            ctk.CTkLabel(fila, text=estado, text_color=estado_color, width=120, anchor="w")\
                .pack(side="left", pady=10)

    def agregar_habitacion():
        hab = nueva.get().strip()
        tipo = tipo_nuevo.get()

        if hab == "":
            messagebox.showerror("Error", "Escribe el número de la habitación a agregar.")
            return

        if not hab.isdigit():
            messagebox.showerror("Error", "La habitación debe ser un número (ej: 011).")
            return

        hab = f"{int(hab):03d}"

        if hab in HABITACIONES:
            messagebox.showwarning("Aviso", f"La habitación {hab} ya existe.")
            return

   
        HABITACIONES.append(hab)
        INFO_HAB[hab] = {"tipo": tipo, "estado": "Libre"}

        nueva.delete(0, "end")
        tipo_nuevo.set("Simple")

        messagebox.showinfo("Listo", f"Habitación {hab} agregada como {tipo}.")
        actualizar_resumen()
        dibujar_tabla()
        

    def actualizar():

        for h in HABITACIONES:
            if h not in INFO_HAB:
                INFO_HAB[h] = {"tipo": "Simple", "estado": "Libre"}
        actualizar_resumen()
        dibujar_tabla()


    btn_agregar = ctk.CTkButton(controles, text="Agregar", command=agregar_habitacion)
    btn_agregar.pack(side="left", padx=12)

    btn_actualizar = ctk.CTkButton(controles, text="Buscar", command=actualizar)
    btn_actualizar.pack(side="left", padx=12)

    btn_volver = ctk.CTkButton(
        controles, text="Volver", fg_color="#EA4F4F",
        command=lambda: contenido.mostrar_inicio(), text_color="#E5E7EB"
    )
    btn_volver.pack(side="left", padx=12)


    actualizar()
    