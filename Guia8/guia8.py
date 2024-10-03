from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dic = {key: value for key, value in iterable}
            data.append(country_dic)
        return data

def display_data(select_country):
    data = read_csv('world_population.csv')
    select_data = [country for country in data if country['Country/Territory'] == select_country]

    if not select_data:
        result_var.set("No se encuentra dato del país")
        return 
    select_data = select_data[0]
    tree = ttk.Treeview(root, style="Custom.Treeview")
    tree["columns"] = ("key", "value")
    tree.column("key", width=150)
    tree.column("value", width=150)
    tree.heading("key", text="Atributo")
    tree.heading("value", text="Valor")
    
    for key, value in select_data.items():
        tree.insert("", "end", values=(key, value))
    tree.pack(padx=20, pady=20)
    
    figure, ax = plt.subplots(figsize=(8,6))
    years = [year for year in select_data if year.endswith('Population')]
    populations = [int(select_data[year]) for year in years]
    years = [int(year.split()[0]) for year in years]
    ax.plot(years, populations, marker='o', linestyle='-')
    ax.set_xlabel('Año')
    ax.set_ylabel('Poblacion')
    ax.set_title(f'Evolución de la población para {select_country}')
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

def mayor_poblacion():
    print("hola")

root = Tk()
root.title("Datos población mundial")
root.geometry('800x700')
root.config(bg='blue')

# Definir estilo para Treeview
style = ttk.Style()
style.configure("Custom.Treeview", background="blue")

# Label para mostrar el mensaje de resultado
result_var = StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Helvetica", 18), foreground="Black", background='blue')
result_label.pack(fill='x', padx=10, pady=10)

countries = sorted(set(row['Country/Territory'] for row in read_csv('world_population.csv')))
select_country_var = StringVar()
select_country_var.set("Seleccionar país")
country_combobox = ttk.Combobox(root, textvariable=select_country_var, values=countries, style="Custom.TCombobox")
country_combobox.pack(side=LEFT, padx=(10, 5))

button = ttk.Button(root, text="Mostrar datos", command=lambda: display_data(select_country_var.get()), style="Custom.TButton")
button.pack(side=LEFT, padx=(0, 10))
button2=ttk.Button(root, text="Mayor poblacion")
button2.pack()

root.mainloop()
    