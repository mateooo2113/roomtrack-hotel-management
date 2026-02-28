import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image


ctk.set_default_color_theme("dark-blue")
admins = {
    "admin1" : "123",
    "admin2" : "1234",
    "admin3": "12345"}

def login (Roomtrack, mostrar_principal):
    #VCrear ventana y frame del fondo
    Roomtrack_login= ctk.CTkFrame(Roomtrack)
    Roomtrack_login.pack(fill="both", expand =True)

    
    fondo= ctk.CTkFrame(Roomtrack_login, fg_color="#0F172A" )
    fondo.pack (fill ="both", expand = True)

    #Frame Header
    header= ctk.CTkFrame(fondo, fg_color= "transparent")
    header.pack(side = "top", fill = "x", pady=(90,25))
    #Frame centro
    centro= ctk.CTkFrame(fondo, fg_color= "transparent")
    centro.pack(fill = "both", expand= True)
    #Crear Frame de widgets
    login_widg  = ctk.CTkFrame(centro, width=280, height=220, corner_radius= 15, fg_color="#0B1220" )
    login_widg.pack(expand=True, pady=(0,120))

    #Imagen
    logo_img = ctk.CTkImage(light_image=Image.open("logo.png"),size=(300, 300))
    #Logo
    logo_label = ctk.CTkLabel(header,image=logo_img,text="")
    logo_label.pack(pady=(10, 0))

    #Entrys
    Usuario = ctk.CTkEntry(
    login_widg,
    placeholder_text="Usuario",
    fg_color="#1E293B",
    border_color="#334155",
    text_color="#E5E7EB",
    placeholder_text_color="#94A3B8",
    border_width=1,
    height=36,
    corner_radius=10
    )
    Usuario.pack(pady=(10, 6))


    Contraseña = ctk.CTkEntry(
    login_widg,
    placeholder_text="Contraseña",
    show="*",
    fg_color="#1E293B",
    border_color="#334155",
    text_color="#E5E7EB",
    placeholder_text_color="#94A3B8",
    border_width=1,
    height=36,
    corner_radius=10
    )
    Contraseña.pack(pady=(6, 12))
    
    #Boton
    Ingreso= ctk.CTkButton(
        login_widg,
        width=220,
        height= 38, 
        corner_radius=12, 
        fg_color="#2563EB", 
        hover_color="#3B82F6",  
        text_color="#F8FAFC", 
        command=lambda: valid_login(Usuario , Contraseña, Roomtrack_login, mostrar_principal), 
        text = "Acceder",
        font=("Arial", 14, "bold")
        )
    Ingreso.pack(pady = 15)

    

def valid_login (Usuario , Contraseña, Roomtrack_login, mostrar_principal):
    

    ent_usu = Usuario.get().strip()
    ent_contr = Contraseña.get().strip() 
    if ent_usu in admins and ent_contr == admins[ent_usu] :
        mostrar_principal(Roomtrack_login)

    else: 
        messagebox.showerror("Error",  "Usuario o contraseña Incorrectos")

