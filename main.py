#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System
import sys
import os
import platform
import math

# Database
import pymysql

# Loggin
import logging

# Pdf-report
from fpdf import FPDF

# Las dos líneas siguientes son necesaias para hacer
# compatible el interfaz Tkinter con los programas basados
# en versiones anteriores a la 8.5, con las más recientes.
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from PIL import ImageTk, Image



class DataBase_Mysql:

    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.username = "root"
        self.password = "M2racuya"
        self.database_name = 'database="productsControl"'
        self.conn = 0
        self.cursor = 0
        self.Database_tables = ['tb_users', 'tb_groups']

    def create_connection(self):
        self.conn = pymysql.connect(host=self.host, user=self.username ,password=self.password, database= self.database_name)
        self.cursor = self.conn.cursor()
    
    def create_cursor(self):
        self.cursor = self.conn.cursor()

    def commit_changes(self):
        self.conn.commit()


    def query(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchone()


class DataBase_SqlLite:

    def __init__(self):
        self.PORT = 3306
        self.USERNAME = ""
        self.PASSWORD = ""
        self.CONN = ""
        self.CURSOR = ""
        self.DATABASE = 'mydb'
        self.DATABASE_TABLES = ['tb_users', 'tb_groups']

    def create_connection(self):
        #Sino existe la crea.
        self.CONN = sqlite3.connect(self.DATABASE)
    
    def create_cursor(self):
        self.CURSOR = self.CONN.cursor()

    def commit_changes(self):
        self.CONN.commit()


class Aplicacion():
       
    def __init__(self):       
        # VENTANA PRINCIPAL
        raiz = Tk()
        raiz.geometry('1200x700+0+0')
        raiz.title('Client DB example')
        raiz.configure(bg = "#FFFFFF")
        raiz.resizable(False, False)
        ttk.Button(raiz, text='Salir',command=raiz.destroy).pack(side=BOTTOM)

        # PANEL PARA LAS PESTAÑAS
        nb = ttk.Notebook(raiz)
        nb.pack(fill='both',expand = 'yes')

        #PESTAÑAS
        frames=[] 

        p1 =ttk.Frame(nb)
        p2 =ttk.Frame(nb)
        p3 =ttk.Frame(nb)
        p4 =ttk.Frame(nb)
        p5 =ttk.Frame(nb)
        
        frames.append(p1)
        frames.append(p2)
        frames.append(p3)
        frames.append(p4)
        frames.append(p5)

        nb.add(p1,text='Inventario')
        nb.add(p2,text='Opciones')
        nb.add(p3,text='Configuraciones')
        nb.add(p4,text='Informe - Reporte')
        nb.add(p5,text='Salida por consola')
        
        #Variables 
        self.Id_value = StringVar()
        self.Item_value = StringVar()
        self.Brand_value = StringVar()
        self.Model_value = StringVar()
        self.Ref_code_value = StringVar()
        self.Price_value = StringVar()
        self.Discount_value = StringVar()
        self.Description_value = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()

        #<---------------ENCABEZADOS --------------->
        img = Image.open("./1.png")  # PIL solution
        img = img.resize((150, 80), Image.ANTIALIAS) #The (250, 250) is (height, width)
        img = ImageTk.PhotoImage(img) # convert to PhotoImage

        color_fondo ="#ffffff"
        color_back_text_title = "#E8E8E8"
        color_back_text_label = "#D4D4DB"
        
        
        #Load header in all Frame
        for frame in frames :
            tk.Label(frame,text="ABM Control de Productos", font=("Cambria",20,'bold'), bg=color_fondo, fg="#172E64", width="800", height="4").pack()
        #<------------------------------------------>

        #<------------ P1 Inventairo ------------>

        #========= Manage Frame ===============
        Manage_Frame = Frame (p1, relief=RIDGE, bd=4, bg = color_back_text_title)
        Manage_Frame.place(x=5, y=100,width=450, height=550)
        
        Title_label = Label (Manage_Frame, text="Datos Producto", bg=color_back_text_title, font=("Cambria",20,'bold'), fg="#172E64")
        Title_label.place(x=170, y=10)

        Id_label = Label (Manage_Frame, text="ID:",  bg =color_back_text_label)
        Id_label.place(x=90, y=50)
        self.Id_value = StringVar()
        id_entry = Entry(Manage_Frame, textvariable=self.Id_value,justify='center', width="22")
        id_entry.place(x=20, y=75)

        Item_label = Label (Manage_Frame, text="Item:",  bg =color_back_text_label)
        Item_label.place(x=300, y=50)
        self.Item_value = StringVar()
        Item_entry = Entry(Manage_Frame, textvariable=self.Item_value, justify='center', width="22")
        Item_entry.place(x=220, y=75)
        #<------------------------------------>
        Brand_label = Label (Manage_Frame, text="Marca:",  bg =color_back_text_label)
        Brand_label.place(x=90, y=125)
        self.Brand_value = StringVar()
        Brand_entry = Entry(Manage_Frame, textvariable=self.Brand_value, justify='center', width="22")
        Brand_entry.place(x=20, y=150)

        Model_label = Label (Manage_Frame, text="Item:",  bg =color_back_text_label)
        Model_label.place(x=300, y=125)
        self.Model_value = StringVar()
        Model_entry = Entry(Manage_Frame, textvariable=self.Model_value, justify='center', width="22")
        Model_entry.place(x=220, y=150)
        #<------------------------------------>
        Ref_code_label = Label (Manage_Frame, text="Código:",  bg =color_back_text_label)
        Ref_code_label.place(x=180, y=200)
        self.Ref_code_value = StringVar()
        Ref_code_entry = Entry(Manage_Frame, textvariable=self.Ref_code_value, justify='center', width="50")
        Ref_code_entry.place(x=20, y=225)
        #<------------------------------------>
        Price_label = Label (Manage_Frame, text="Precio:",  bg =color_back_text_label)
        Price_label.place(x=90, y=275)
        self.Price_value = StringVar()
        Price_entry = Entry(Manage_Frame, textvariable=self.Price_value, justify='center', width="22")
        Price_entry.place(x=20, y=300)

        Discount_label = Label (Manage_Frame, text="Descuento",  bg =color_back_text_label)
        Discount_label.place(x=280, y=275)
        self.Discount_value = StringVar()
        Discount_entry = Entry(Manage_Frame, textvariable=self.Discount_value,justify='center', width="22")
        Discount_entry.place(x=220, y=300)
        #<------------------------------------>
        Description_label = Label (Manage_Frame, text="Descripción:",  bg =color_back_text_label)
        Description_label.place(x=180, y=350)
        self.Description_value = StringVar()
        Description_entry = Entry(Manage_Frame, textvariable=self.Description_value, justify='center', width="50" )
        Description_entry.place(x=20, y=375, height=75)
        #<------------------------------------>
        btn_Frame = Frame (Manage_Frame, bd = 4, bg=color_back_text_title)
        btn_Frame.place(x=10, y=450, width=430)

        Add_btn = Button(btn_Frame, text="Agregar", width=8, command=self.add_products).grid(row=0,column=0, padx=8, pady=10)
        Update_btn = Button(btn_Frame, text="Actualizar", width=8, command=self.update_products).grid(row=0,column=1, padx=8, pady=10)
        Delete_btn = Button(btn_Frame, text="Eliminar", width=8, command=self.delete_products).grid(row=0,column=2, padx=8, pady=10)
        Clear_btn = Button(btn_Frame, text="Borrar", width=8, command=self.clear_products).grid(row=0,column=3, padx=8, pady=10)
        #========= Detail Frame ===============
        Detail_Frame = Frame (p1, relief=RIDGE, bd=4, bg = color_back_text_title)
        Detail_Frame.place(x=460, y=100, width=670, height=500)

        lbl_search = Label (Detail_Frame, text="Buscar por", bg=color_back_text_title, font=("Cambria",20,'bold'), fg="#172E64")
        lbl_search.grid (row=0, column=0, pady=10, padx=2, sticky="w")

        Combo_Search =ttk.Combobox(Detail_Frame,width="10",textvariable=self.search_by, font=("Cambria",10,''),state='readonly')
        Combo_Search['values']=("Id","Item","Marca","Codigo", "Precio", "Descuento")
        Combo_Search.grid (row=0, column=1, pady=10, padx=20)

        Text_Search = Entry (Detail_Frame,width="20", textvariable=self.search_text, font=("Cambria",10,''), fg="#172E64",state='readonly')
        Text_Search.grid (row=0, column=2, pady=10, padx=20, sticky="w")

        btn_Search = Button(Detail_Frame, text="Buscar", width=10).grid(row=0,column=3, padx=10, pady=10)
        btn_Showall = Button(Detail_Frame, text="Mostrar todos", width=10).grid(row=0,column=4, padx=10, pady=10)
        #========= Table Frame ===============
        Table_Frame = Frame (Detail_Frame, relief=RIDGE, bd=4, bg = color_back_text_title)
        Table_Frame.place(x=10, y=70, width=660, height=400)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Products_table = ttk.Treeview(Table_Frame, columns=("Id", "Item", "Marca", "Modelo", "Codigo", "Precio", "Descuento", "Descripcion"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
        scroll_x.pack (side= BOTTOM, fill =X)
        scroll_y.pack (side= RIGHT, fill =Y)

        scroll_x.config(command=self.Products_table.xview)
        scroll_y.config(command=self.Products_table.yview)

        self.Products_table.heading("Id",text="Id Nro.")
        self.Products_table.heading("Item",text="Item")
        self.Products_table.heading("Marca",text="Marca")
        self.Products_table.heading("Modelo",text="Modelo")
        self.Products_table.heading("Codigo",text="Código")
        self.Products_table.heading("Precio",text="Precio($)")
        self.Products_table.heading("Descuento",text="Descuento(%)")
        self.Products_table.heading("Descripcion",text="Descripcion")

        self.Products_table['show']="headings"
        
        self.Products_table.column("Id",width=100)
        self.Products_table.column("Item",width=100)
        self.Products_table.column("Marca",width=100)
        self.Products_table.column("Modelo",width=100)
        self.Products_table.column("Codigo",width=100)
        self.Products_table.column("Precio",width=100)
        self.Products_table.column("Descuento",width=100)
        self.Products_table.column("Descripcion",width=100)

        self.Products_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        #<------------------------------------>



        #<---------- P2 Parámetros Equipos --------->
        lista_label = Label (p5, text="Debug",font=('​Helvetica', 12, 'bold'), bg = color_back_text_title)
        lista_label.place(x=550, y=120)
                
        # Vincularla con la lista.
        self.debug_list = Listbox(p5, bg="#ffffff", fg="#000", width="140", height="27")
        
        self.debug_list.insert (tk.END, "INFO --> Interface gráfica inicializada")

        self.debug_list.place(x=15, y=180)

        raiz.mainloop()

    def add_products(self):
        conn = pymysql.connect(host="localhost", user="root", password="M2racuya", database="productsControl")
        cursor = conn.cursor()
        cursor.execute ('INSERT INTO products VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(self.Id_value.get(),
                                                                                    self.Item_value.get(),
                                                                                    self.Brand_value.get(),
                                                                                    self.Model_value .get(),
                                                                                    self.Ref_code_value .get(),
                                                                                    self.Price_value.get(),
                                                                                    self.Discount_value.get(),
                                                                                    self.Description_value.get()
                                                                                    ))
        conn.commit()
        conn.close


    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="M2racuya", database="productsControl")
        cursor = conn.cursor()
        cursor.execute ('SELECT * from products')
        rows = cursor.fetchall()

        if(len(rows)):
            self.Products_table.delete(*self.Products_table.get_children())
            for row in rows:
                self.Products_table.insert('',END,values=row)
                conn.commit()
        conn.close()

    def search_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="M2racuya", database="productsControl")
        cursor = conn.cursor()
        cursor.execute ('SELECT * from products where'+str(self.search_by.get() + "Like '%" + str(self.search_text.get()))+"%'")
        rows = cursor.fetchall()

        if(len(rows)):
            self.Products_table.delete(*self.Products_table.get_children())
            for row in rows:
                self.Products_table.insert('',END,values=row)
                conn.commit()
        conn.close()


    def get_cursor(self):

        cursor_row = self.Products_table.focus()
        contents = self.Products_table.item(cursor_row)
        row = contents ['values']

        self.Id_value.set(row[0])
        self.Item_value.set(row[1])
        self.Brand_value.set(row[2])
        self.Model_value.set(row[3])
        self.Ref_code_value.set(row[4])
        self.Price_value.set(row[5])
        self.Discount_value.set(row[6])
        self.Description_value.set(row[7])

    def delete_products(self):
        conn = pymysql.connect(host="localhost", user="root",password="M2racuya" , database="productsControl")
        cursor = conn.cursor()
        cursor.execute ('delete from products where id=%s', self.Id_value.get())
        conn.commit()
        conn.close
        self.fetch_data()
        self.clear_products()
   
    def update_products(self):
        conn = pymysql.connect(host="localhost", user="root", password="M2racuya" , database="productsControl")
        cursor = conn.cursor()
        cursor.execute ('SELECT * from products where id=%s', self.Id_value.get())
        rows = cursor.fetchall()

        conn.commit()
        conn.close

    def clear_products(self):
        self.Id_value.set("")
        self.Item_value.set("")
        self.Brand_value.set("")
        self.Model_value.set("")
        self.Ref_code_value.set("")
        self.Price_value.set("")
        self.Discount_value.set("")
        self.Description_value.set("")



"""
Init loggin Opt
"""
def loggin_init():
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S' )
    

"""
Funcion Principal
"""
def main():
    loggin_init()
    logging.info('Inicio de aplicación')
    App = Aplicacion()
    logging.info('Conexion a Base de datos')
    Db = DataBase_Mysql()
    Db.create_connection()
    Db.create_cursor()
    logging.info('Fin de aplicación')
    return 0


if __name__ == '__main__':
    main()

