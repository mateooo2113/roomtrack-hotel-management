import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from Roomtrack_login import login
from Roomtrack_Reservas import mostrar_reservas
from Roomtrack_Habitaciones import mostrar_habitaciones
from RoomTrack_Reportes import mostrar_reportes
from PIL import Image, ImageTk

Roomtrack = ctk.CTk()
Roomtrack.title("Roomtrack")
Roomtrack.geometry("1300x720")
AzulRoomtrack= "#1E293B"
AzulBarra = "#1C2B4A"
Borde = "#E5E7EB"
Texto = "#F1F5F9"
subtexto = "#CBD5E1"

#Frame princiapal
frame_p = ctk.CTkFrame(Roomtrack, fg_color="#FFFFFF")
frame_p.grid_rowconfigure(0, weight=1)
frame_p.grid_columnconfigure(0, weight=0)
frame_p.grid_columnconfigure(1, weight=1)

#Frame/wrapped barra
barra_wrap = ctk.CTkFrame(frame_p, fg_color="transparent", width=270, height=684)
barra_wrap.grid(row=0, column=0, sticky="nsw", padx=18, pady=18)
barra_wrap.grid_propagate(False)

#Barra
Barra = ctk.CTkFrame(
    barra_wrap, fg_color=AzulBarra, corner_radius=24,
    border_width=1, border_color=Borde, width=260, height=600
)
Barra.place(x=10, y=28, relheight=0.85, relwidth=0.96)

titulo = ctk.CTkLabel(Barra, text="ROOMTRACK", font=("Times New Roman", 20, "bold"), text_color=Texto)
titulo.pack(pady=(18, 10))
ctk.CTkButton(Barra, text="Reservas", command=lambda: mostrar_reservas(contenido)).pack(fill="x", padx=20, pady=6)
ctk.CTkButton(Barra, text="Habitaciones", command=lambda: mostrar_habitaciones(contenido)).pack(fill="x", padx=20, pady=6)
ctk.CTkButton(Barra, text="Proyecciones", command=lambda: mostrar_reportes(contenido)).pack(fill="x", padx=20, pady=6)

#Frame contenido
contenido = ctk.CTkFrame(frame_p, fg_color="#F6F7FB")
contenido.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

def mostrar_inicio():
    for w in contenido.winfo_children():
        w.destroy()
    frame_img = ctk.CTkFrame(contenido, fg_color="transparent")
    frame_img.pack(fill="x", padx=20, pady=20)

    ctk.CTkLabel(frame_img,text="Tipos de habitaciones",font=("Arial", 20, "bold"),text_color=AzulBarra).pack(anchor="w", padx=6, pady=(0, 12))

  
    cards_wrap = ctk.CTkFrame(frame_img, fg_color="transparent")
    cards_wrap.pack(anchor="w")

    
    cards_wrap.grid_columnconfigure(0, weight=1)
    cards_wrap.grid_columnconfigure(1, weight=1)


    card1 = ctk.CTkFrame(cards_wrap, fg_color="#FFFFFF", corner_radius=18, border_width=1, border_color=Borde,width=300,height=260)
    card1.grid(row=0, column=0, padx=20, pady=20)
    card1.grid_propagate(False)
    
    ctk.CTkLabel(card1, text="HABITACION SIMPLE", font=("Arial", 12, "bold"), text_color=AzulBarra).pack(anchor="w", padx=12, pady=(12, 8))

    img1 = Image.open("hab simple.webp").resize((260, 170))
    img1_tk = ImageTk.PhotoImage(img1)
    lbl1 = ctk.CTkLabel(card1, image=img1_tk, text="")
    lbl1.image = img1_tk
    lbl1.pack(padx=12, pady=(0, 12))

    

    card2 = ctk.CTkFrame(cards_wrap, fg_color="#FFFFFF", corner_radius=18, border_width=1, border_color=Borde, width=300,height=260)
    card2.grid(row=0, column=1, padx=20, pady=20)
    card2.grid_propagate(False)
    ctk.CTkLabel(card2, text="HABITACION DOBLE", font=("Arial", 12, "bold"), text_color=AzulBarra).pack(anchor="w", padx=12, pady=(12, 8))

    img2 = Image.open("hab doble.jpg").resize((260, 170))
    img2_tk = ImageTk.PhotoImage(img2)
    lbl2 = ctk.CTkLabel(card2, image=img2_tk, text="")
    lbl2.image = img2_tk
    lbl2.pack(padx=12, pady=(0, 12))

   
    card3 = ctk.CTkFrame(cards_wrap, fg_color="#FFFFFF", corner_radius=18, border_width=1, border_color=Borde, width=300,height=260)
    card3.grid(row=1, column=0, padx=20, pady=20)
    card3.grid_propagate(False)
    
    ctk.CTkLabel(card3, text="HABITACION SUITE", font=("Arial", 12, "bold"), text_color=AzulBarra).pack(anchor="w", padx=12, pady=(12, 8))

    img3 = Image.open("hab suite.jpg").resize((260, 170))
    img3_tk = ImageTk.PhotoImage(img3)
    lbl3 = ctk.CTkLabel(card3, image=img3_tk, text="")
    lbl3.image = img3_tk
    lbl3.pack(padx=12, pady=(0, 12))

  
    card4 = ctk.CTkFrame(cards_wrap, fg_color="#FFFFFF", corner_radius=18, border_width=1, border_color=Borde, width=300,height=260)
    card4.grid(row=1, column=1, padx=20, pady=20)
    card4.grid_propagate(False)
    ctk.CTkLabel(card4, text="HABITACION FAMILIAR", font=("Arial", 12, "bold"), text_color=AzulBarra).pack(anchor="w", padx=12, pady=(12, 8))

    img4 = Image.open("hab familiar.webp").resize((260, 170))
    img4_tk = ImageTk.PhotoImage(img4)
    lbl4 = ctk.CTkLabel(card4, image=img4_tk, text="")
    lbl4.image = img4_tk
    lbl4.pack(padx=12, pady=(0, 12))

    

contenido.mostrar_inicio = mostrar_inicio

def mostrar_principal(login_frame):
    login_frame.pack_forget()
    frame_p.pack(fill="both", expand=True)
    contenido.mostrar_inicio()

login(Roomtrack, mostrar_principal)

Roomtrack.mainloop()