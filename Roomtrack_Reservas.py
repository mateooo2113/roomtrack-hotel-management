import customtkinter as ctk
from tkinter import messagebox
from datetime import date
from Roomtrack_Habitaciones import HABITACIONES, INFO_HAB

RESERVAS = []


def limpiar_contenido(contenido):
    for widgets in contenido.winfo_children():
        widgets.destroy()


def mostrar_reservas(contenido):
    limpiar_contenido(contenido)

    vent = ctk.CTkFrame(contenido, fg_color="#FFFFFF", corner_radius=18)
    vent.pack(fill="both", expand=True)

    titulo = ctk.CTkLabel(vent, text="Reservas", font=("Arial", 22, "bold"), text_color="#111827")
    titulo.pack(anchor="w", padx=24, pady=(20, 8))

    subtitulo = ctk.CTkLabel(
        vent,
        text="Crea y administra reservas de habitaciones.",
        font=("Arial", 13),
        text_color="#6B7280"
    )
    subtitulo.pack(anchor="w", padx=24, pady=(0, 16))

    form = ctk.CTkFrame(vent, fg_color="#F9FAFB", corner_radius=14)
    form.pack(fill="x", padx=24, pady=(0, 18))

    ctk.CTkLabel(form, text="Cliente", text_color="#111827").grid(row=0, column=0, sticky="w", padx=16, pady=(14, 6))
    entry_cliente = ctk.CTkEntry(form, placeholder_text="Nombre del cliente")
    entry_cliente.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 14))

    ctk.CTkLabel(form, text="Habitación", text_color="#111827").grid(row=0, column=1, sticky="w", padx=16, pady=(14, 6))
    entry_hab = ctk.CTkEntry(form, placeholder_text="Ej: 001")
    entry_hab.grid(row=1, column=1, sticky="ew", padx=16, pady=(0, 14))

    ctk.CTkLabel(form, text="Fecha de entrada", text_color="#111827").grid(row=2, column=0, sticky="w", padx=16, pady=(0, 6))
    entry_entrada = ctk.CTkEntry(form, placeholder_text="DD/MM/AAAA")
    entry_entrada.grid(row=3, column=0, sticky="ew", padx=16, pady=(0, 14))

    ctk.CTkLabel(form, text="Fecha de salida", text_color="#111827").grid(row=2, column=1, sticky="w", padx=16, pady=(0, 6))
    entry_salida = ctk.CTkEntry(form, placeholder_text="DD/MM/AAAA")
    entry_salida.grid(row=3, column=1, sticky="ew", padx=16, pady=(0, 14))

    form.grid_columnconfigure(0, weight=1)
    form.grid_columnconfigure(1, weight=1)

    acciones = ctk.CTkFrame(vent, fg_color="transparent")
    acciones.pack(fill="x", padx=24, pady=(0, 18))

    # ---- LISTA ----
    lista = ctk.CTkFrame(vent, fg_color="#FFFFFF", corner_radius=14, border_width=1, border_color="#E5E7EB")
    lista.pack(fill="both", expand=True, padx=24, pady=(0, 24))

    ctk.CTkLabel(lista, text="Reservas recientes", text_color="#111827", font=("Arial", 14, "bold")) \
        .pack(anchor="w", padx=16, pady=(14, 8))

    cont_lista = ctk.CTkFrame(lista, fg_color="transparent")
    cont_lista.pack(fill="both", expand=True, padx=16, pady=(0, 14))


    def limpiar_campos():
        entry_cliente.delete(0, "end")
        entry_hab.delete(0, "end")
        entry_entrada.delete(0, "end")
        entry_salida.delete(0, "end")
        entry_cliente.focus()

    def fecha_valida(txt):
    
        if len(txt) != 10:
            return False
        if txt[2] != "/" or txt[5] != "/":
            return False

        dd = txt[0:2]
        mm = txt[3:5]
        aa = txt[6:10]

        if not (dd.isdigit() and mm.isdigit() and aa.isdigit()):
            return False

        d = int(dd)
        m = int(mm)
        a = int(aa)

        if a < 1900 or a > 2100:
            return False
        if m < 1 or m > 12:
            return False


        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        max_d = dias_mes[m - 1]

        if m == 2:
            if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
                max_d = 29

        if d < 1 or d > max_d:
            return False

        return True

    def texto_a_fecha(txt):
        d = int(txt[0:2])
        m = int(txt[3:5])
        a = int(txt[6:10])
        return date(a, m, d)

    def hay_choque(hab, f_entrada, f_salida):
        for r in RESERVAS:
            if r["habitacion"] == hab:
                e = texto_a_fecha(r["entrada"])
                s = texto_a_fecha(r["salida"])
                if (f_entrada < s) and (f_salida > e):
                    return True
        return False

    def mostrar_lista_reservas():
        for w in cont_lista.winfo_children():
            w.destroy()

        if len(RESERVAS) == 0:
            ctk.CTkLabel(cont_lista, text="Aún no hay reservas guardadas.", text_color="#6B7280") \
                .pack(anchor="w")
            return

        head = ctk.CTkFrame(cont_lista, fg_color="transparent")
        head.pack(fill="x", pady=(0, 8))

        ctk.CTkLabel(head, text="Cliente", text_color="#111827", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(head, text="Hab.", text_color="#111827", font=("Arial", 12, "bold")).grid(row=0, column=1, sticky="w", padx=(20, 0))
        ctk.CTkLabel(head, text="Entrada", text_color="#111827", font=("Arial", 12, "bold")).grid(row=0, column=2, sticky="w", padx=(20, 0))
        ctk.CTkLabel(head, text="Salida", text_color="#111827", font=("Arial", 12, "bold")).grid(row=0, column=3, sticky="w", padx=(20, 0))

        head.grid_columnconfigure(0, weight=3)
        head.grid_columnconfigure(1, weight=1)
        head.grid_columnconfigure(2, weight=2)
        head.grid_columnconfigure(3, weight=2)

        for r in RESERVAS[::-1]:
            fila = ctk.CTkFrame(cont_lista, fg_color="#F9FAFB", corner_radius=10)
            fila.pack(fill="x", pady=6)

            ctk.CTkLabel(fila, text=r["cliente"], text_color="#111827").grid(row=0, column=0, sticky="w", padx=12, pady=10)
            ctk.CTkLabel(fila, text=r["habitacion"], text_color="#111827").grid(row=0, column=1, sticky="w", padx=(20, 0))
            ctk.CTkLabel(fila, text=r["entrada"], text_color="#111827").grid(row=0, column=2, sticky="w", padx=(20, 0))
            ctk.CTkLabel(fila, text=r["salida"], text_color="#111827").grid(row=0, column=3, sticky="w", padx=(20, 0))

            fila.grid_columnconfigure(0, weight=3)
            fila.grid_columnconfigure(1, weight=1)
            fila.grid_columnconfigure(2, weight=2)
            fila.grid_columnconfigure(3, weight=2)

    def guardar_reserva():
        cliente = entry_cliente.get().strip()
        hab = entry_hab.get().strip()
        entrada = entry_entrada.get().strip()
        salida = entry_salida.get().strip()

        if cliente == "" or hab == "" or entrada == "" or salida == "":
            messagebox.showerror("Error", "Completa todos los campos.")
            return


        if not hab.isdigit():
            messagebox.showerror("Error", "La habitación debe ser un número (ej: 001).")
            return
        hab = f"{int(hab):03d}"

        if hab not in HABITACIONES:
            messagebox.showerror("Error", f"La habitación {hab} no existe. Agrégala en Habitaciones.")
            return

        if not fecha_valida(entrada):
            messagebox.showerror("Error", "Fecha de entrada inválida. Usa DD/MM/AAAA.")
            return
        if not fecha_valida(salida):
            messagebox.showerror("Error", "Fecha de salida inválida. Usa DD/MM/AAAA.")
            return

        f_entrada = texto_a_fecha(entrada)
        f_salida = texto_a_fecha(salida)

        if f_salida <= f_entrada:
            messagebox.showerror("Error", "La fecha de salida debe ser después de la entrada.")
            return


        if hay_choque(hab, f_entrada, f_salida):
            messagebox.showerror("Error", f"La habitación {hab} ya está reservada en esas fechas.")
            return


        RESERVAS.append({
            "cliente": cliente,
            "habitacion": hab,
            "entrada": entrada,
            "salida": salida
        })

        if hab in INFO_HAB:
            INFO_HAB[hab]["estado"] = "Ocupada"

        messagebox.showinfo("Listo", "Reserva guardada correctamente.")
        limpiar_campos()
        mostrar_lista_reservas()

    btn_guardar = ctk.CTkButton(acciones, text="Guardar reserva", command=guardar_reserva)
    btn_guardar.pack(side="left")

    btn_limpiar = ctk.CTkButton(acciones, text="Limpiar", fg_color="#E5E7EB", text_color="#111827", command=limpiar_campos)
    btn_limpiar.pack(side="left", padx=12)

    btn_volver = ctk.CTkButton(
        acciones,
        text="Volver",
        fg_color="#EA4F4F",
        command=lambda: contenido.mostrar_inicio(),
        text_color="#E5E7EB"
    )
    btn_volver.pack(side="left", padx=120)
    
    mostrar_lista_reservas()