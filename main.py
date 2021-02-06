from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import ttk
from bs4 import BeautifulSoup
from requests import get

# OLX-----------------------------------------------------------------------------------------------------
def olx():

    # PARSE----------------------------------------------------------------------------------------------------
    conn = sqlite3.connect('baza_olx.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS offers (location TEXT, topic TEXT, price TEXT, link TEXT)''')

    def parce_price(price):
        return int(price.replace(' ', '').replace('zł', ''))

    URL = 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/?'

    def parse_page(page):
        page = get(f'{URL}&page={page}')
        bs = BeautifulSoup(page.content, 'html.parser')
        for offer in bs.find_all('div', class_='offer'):
            footer = offer.find('td', class_='bottom-cell')
            location = footer.find('small', class_='breadcrumb').get_text().strip()
            topic = offer.find('strong').get_text()
            price = parce_price(offer.find('p', class_='price').get_text())
            link = offer.find('a')['href']

            c.execute('INSERT INTO offers VALUES (?, ?, ?, ?)', (location, topic, price, link))
            conn.commit()
        print('...')

        for page in range(1, 2):
            parse_page(page)

    conn.close()

    # EndPARSE----------------------------------------------------------------------------------------------------

    # connect to the database
def View():
    conn = sqlite3.connect('baza_olx.db')
    c = conn.cursor()
    c.execute("SELECT *, oid from offers")

    master = Tk()
    master.geometry('1000x500')
    master.title('Mieszkania')
    color = "#ccf5b8"
    Label1 = Label(master, text="Miasto", width=20, bg=color)
    Label1.grid(row=0, column=1)
    Label2 = Label(master, text="Nazwa ogłoszenia", width=30, bg=color)
    Label2.grid(row=0, column=2)
    Label3 = Label(master, text="Cena", width=20, bg=color)
    Label3.grid(row=0, column=3)
    Label4 = Label(master, text="Link", width=30, bg=color)
    Label4.grid(row=0, column=4)
    for index, dat in enumerate(c):
        Label(master, text=dat[0]).grid(row=index + 1, column=1)
        Label(master, text=dat[1]).grid(row=index + 1, column=2)
        Label(master, text=dat[2]).grid(row=index + 1, column=3)
        Label(master, text=dat[3]).grid(row=index + 1, column=4)
        # Commit Changes
    conn.commit()
        # Close connect
    conn.close()
def ViewPriceASC():
    conn = sqlite3.connect('baza_olx.db')
    c = conn.cursor()
    c.execute("SELECT *, oid from offers ORDER BY PRICE ASC")

    master = Tk()
    master.geometry('1000x500')
    master.title('Mieszkania')
    color = "#ccf5b8"
    Label1 = Label(master, text="Miasto", width=20, bg=color)
    Label1.grid(row=0, column=1)
    Label2 = Label(master, text="Nazwa ogłoszenia", width=30, bg=color)
    Label2.grid(row=0, column=2)
    Label3 = Label(master, text="Cena", width=20, bg=color)
    Label3.grid(row=0, column=3)
    Label4 = Label(master, text="Link", width=30, bg=color)
    Label4.grid(row=0, column=4)
    for index, dat in enumerate(c):
        Label(master, text=dat[0]).grid(row=index + 1, column=1)
        Label(master, text=dat[1]).grid(row=index + 1, column=2)
        Label(master, text=dat[2]).grid(row=index + 1, column=3)
        Label(master, text=dat[3]).grid(row=index + 1, column=4)
        # Commit Changes
    conn.commit()
        # Close connect
    conn.close()
def ViewPriceDESC():
    conn = sqlite3.connect('baza_olx.db')
    c = conn.cursor()
    c.execute("SELECT *, oid from offers ORDER BY PRICE DESC")

    master = Tk()
    master.geometry('1000x500')
    master.title('Mieszkania')
    color = "#ccf5b8"
    Label1 = Label(master, text="Miasto", width=20, bg=color)
    Label1.grid(row=0, column=1)
    Label2 = Label(master, text="Nazwa ogłoszenia", width=30, bg=color)
    Label2.grid(row=0, column=2)
    Label3 = Label(master, text="Cena", width=20, bg=color)
    Label3.grid(row=0, column=3)
    Label4 = Label(master, text="Link", width=30, bg=color)
    Label4.grid(row=0, column=4)
    for index, dat in enumerate(c):
        Label(master, text=dat[0]).grid(row=index + 1, column=1)
        Label(master, text=dat[1]).grid(row=index + 1, column=2)
        Label(master, text=dat[2]).grid(row=index + 1, column=3)
        Label(master, text=dat[3]).grid(row=index + 1, column=4)
        # Commit Changes
    conn.commit()
        # Close connect
    conn.close()




# EndOLX--------------------------------------------------------------------------------------------------

# Menu----------------------------------------------------------------------------------------
root = Tk()
root.title('Zarządzanie baza danych')
root.geometry('500x500')

my_menu = Menu(root)
root.config(menu=my_menu)


def nic():
    pass


def createDB():
    # Connect
    conn = sqlite3.connect('dom.db')
    # Create cursor
    c = conn.cursor()
    # Create table
    c.execute("""CREATE TABLE dom (
        miasto text,
        mieszkanie_dom text,
        wynajem_sprzedaz text, 
        cena text,
        do_kiedy text
        )""")


def deleteDB():
    # Connect
    conn = sqlite3.connect('dom.db')
    # Create cursor
    c = conn.cursor()
    # Create table
    c.execute("DROP DATABASE dom.db")


def help():
    root = tk.Tk()
    root.title('HELP')
    root.geometry('500x350')
    S = tk.Scrollbar(root)
    T = tk.Text(root, height=4, width=100, font=("Georgia", "15"))
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """
                PHONE NUMBER
                -----------
                159-357-987
                87-147-852


                MAIL CONTACT
                -----------
                help@tk.com
                contact@tk.com"""
    T.insert(tk.END, quote)
    tk.mainloop()


def About():
    root = tk.Tk()
    root.title('About')
    root.geometry('700x350')
    S = tk.Scrollbar(root)
    T = tk.Text(root, height=4, width=100, font=("Georgia", "15"))
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """In facilisis tellus pharetra tempus viverra. 
    Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Integer porta tristique risus, eu porttitor urna placerat sit amet. 
    Pellentesque magna ex, mattis quis imperdiet in, venenatis sed nunc. 
    Nullam ex tortor, pharetra id est sed, pulvinar tempus sem. 
    In in tristique sapien. Fusce facilisis auctor mollis. 
    Nunc sit amet rutrum ligula. Mauris non molestie augue.
    Fusce eu mi mollis, vulputate mauris quis, facilisis risus.
    In facilisis tellus pharetra tempus viverra. 
    Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Integer porta tristique risus, eu porttitor urna placerat sit amet. 
    Pellentesque magna ex, mattis quis imperdiet in, venenatis sed nunc. 
    Nullam ex tortor, pharetra id est sed, pulvinar tempus sem. 
    In in tristique sapien. Fusce facilisis auctor mollis. 
    Nunc sit amet rutrum ligula. Mauris non molestie augue.
    Fusce eu mi mollis, vulputate mauris quis, facilisis risus.
    In facilisis tellus pharetra tempus viverra. 
    Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Integer porta tristique risus, eu porttitor urna placerat sit amet. 
    Pellentesque magna ex, mattis quis imperdiet in, venenatis sed nunc. 
    Nullam ex tortor, pharetra id est sed, pulvinar tempus sem. 
    In in tristique sapien. Fusce facilisis auctor mollis. 
    Nunc sit amet rutrum ligula. Mauris non molestie augue.
    Fusce eu mi mollis, vulputate mauris quis, facilisis risus.
    In facilisis tellus pharetra tempus viverra. 
    Interdum et malesuada fames ac ante ipsum primis in faucibus. 
    Integer porta tristique risus, eu porttitor urna placerat sit amet. 
    Pellentesque magna ex, mattis quis imperdiet in, venenatis sed nunc. 
    Nullam ex tortor, pharetra id est sed, pulvinar tempus sem. 
    In in tristique sapien. Fusce facilisis auctor mollis. 
    Nunc sit amet rutrum ligula. Mauris non molestie augue.
    Fusce eu mi mollis, vulputate mauris quis, facilisis risus."""
    T.insert(tk.END, quote)
    tk.mainloop()


# Create a file item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New database", command=createDB)
file_menu.add_command(label="Delete database", command=deleteDB)
file_menu.add_command(label="Exit", command=root.quit)

# Create a help item
help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=About)
help_menu.add_command(label="Help", command=help)


olx_menu = Menu(my_menu)
my_menu.add_cascade(label="OLX", menu=olx_menu)
olx_menu.add_command(label="Wszsytko", command=View)
olx_menu.add_command(label="Cena rosnąco", command=ViewPriceASC)
olx_menu.add_command(label="Cena malejąco", command=ViewPriceDESC)



# EndMenu-----------------------------------------------------------------------------------


# Connect
conn = sqlite3.connect('dom.db')
# Create cursor
c = conn.cursor()


def delete():
    # Connect
    conn = sqlite3.connect('dom.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from dom WHERE oid=" + delete_box.get())

    # Commit Changes
    conn.commit()
    # Close connect
    conn.close()


def submit():
    # Connect
    conn = sqlite3.connect('dom.db')
    # Create cursor
    c = conn.cursor()
    # Insert
    c.execute("INSERT INTO dom VALUES(:miasto, :mieszkanie_dom, :wynajem_sprzedaz, :cena, :do_kiedy)",
              {
                  'miasto': miasto.get(),
                  'mieszkanie_dom': mieszkanie_dom.get(),
                  'wynajem_sprzedaz': wynajem_sprzedaz.get(),
                  'cena': cena.get(),
                  'do_kiedy': do_kiedy.get()
              })
    # Commit Changes
    conn.commit()
    # Close connect
    conn.close()

    miasto.delete(0, END)
    mieszkanie_dom.delete(0, END)
    wynajem_sprzedaz.delete(0, END)
    cena.delete(0, END)
    do_kiedy.delete(0, END)


# Craete query function
def query():
    conn = sqlite3.connect('dom.db')
    c = conn.cursor()
    c.execute("SELECT *, oid from dom")

    master = Tk()
    master.geometry('650x500')
    master.title('Mieszkania')
    color = "#ccf5b8"
    Label6 = Label(master, text="ID", width=10, bg=color)
    Label6.grid(row=0, column=0)
    Label1 = Label(master, text="Miasto", width=10, bg=color)
    Label1.grid(row=0, column=1)
    Label2 = Label(master, text="Mieszkanie/Dom", width=20, bg=color)
    Label2.grid(row=0, column=2)
    Label3 = Label(master, text="Wynajem/Sprzedaż", width=20, bg=color)
    Label3.grid(row=0, column=3)
    Label4 = Label(master, text="Cena", width=10, bg=color)
    Label4.grid(row=0, column=4)
    Label5 = Label(master, text="Termin", width=10, bg=color)
    Label5.grid(row=0, column=5)
    for index, dat in enumerate(c):
        Label(master, text=dat[0]).grid(row=index + 1, column=1)
        Label(master, text=dat[1]).grid(row=index + 1, column=2)
        Label(master, text=dat[2]).grid(row=index + 1, column=3)
        Label(master, text=dat[3]).grid(row=index + 1, column=4)
        Label(master, text=dat[4]).grid(row=index + 1, column=5)
        Label(master, text=dat[5]).grid(row=index + 1, column=0)
    # Commit Changes
    conn.commit()
    # Close connect
    conn.close()


def save_update():
    conn = sqlite3.connect('dom.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE dom SET 
        miasto = :first,
        mieszkanie_dom = :last,
        wynajem_sprzedaz = :wynajem_sprzedaz,
        cena = :cena,
        do_kiedy = :do_kiedy

        WHERE oid = :oid""",
              {
                  'first': miasto_update.get(),
                  'last': mieszkanie_dom_update.get(),
                  'wynajem_sprzedaz': wynajem_sprzedaz_update.get(),
                  'cena': cena_update.get(),
                  'do_kiedy': do_kiedy_update.get(),
                  'oid': record_id
              })
    # Commit Changes
    conn.commit()
    # Close connect
    conn.close()


# Create update function
def update():
    update = Tk()
    update.title('Update records')
    update.geometry('400x400')
    conn = sqlite3.connect('dom.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM dom WHERE oid=" + record_id)
    records = c.fetchall()

    # Global
    global miasto_update
    global mieszkanie_dom_update
    global wynajem_sprzedaz_update
    global cena_update
    global do_kiedy_update

    # Text Boxes
    miasto_update = Entry(update, width=30)
    miasto_update.grid(row=0, column=1, padx=20, pady=(10, 0))
    mieszkanie_dom_update = Entry(update, width=30)
    mieszkanie_dom_update.grid(row=1, column=1, padx=20)
    wynajem_sprzedaz_update = Entry(update, width=30)
    wynajem_sprzedaz_update.grid(row=2, column=1, padx=20)
    cena_update = Entry(update, width=30)
    cena_update.grid(row=3, column=1, padx=20)
    do_kiedy_update = Entry(update, width=30)
    do_kiedy_update.grid(row=4, column=1, padx=20)

    # Text Labels
    miasto_label = Label(update, text="Miasto")
    miasto_label.grid(row=0, column=0, pady=(10, 0))
    mieszkanie_dom_label = Label(update, text="Mieszkanie/Dom")
    mieszkanie_dom_label.grid(row=1, column=0)
    wynajem_sprzedaz_label = Label(update, text="Wynajem/Sprzedaż")
    wynajem_sprzedaz_label.grid(row=2, column=0)
    cena_label = Label(update, text="Cena")
    cena_label.grid(row=3, column=0)
    do_kiedy_label = Label(update, text="Termin")
    do_kiedy_label.grid(row=4, column=0)

    for record in records:
        miasto_update.insert(0, record[0])
        mieszkanie_dom_update.insert(0, record[1])
        wynajem_sprzedaz_update.insert(0, record[2])
        cena_update.insert(0, record[3])
        do_kiedy_update.insert(0, record[4])
    # Create a update button
    update_btn = Button(update, text="Update records", command=save_update)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Commit Changes
    conn.commit()
    # Close connect
    conn.close()


# Text Boxes
miasto = Entry(root, width=30)
miasto.grid(row=0, column=1, padx=20, pady=(10, 0))
mieszkanie_dom = Entry(root, width=30)
mieszkanie_dom.grid(row=1, column=1, padx=20)
wynajem_sprzedaz = Entry(root, width=30)
wynajem_sprzedaz.grid(row=2, column=1, padx=20)
cena = Entry(root, width=30)
cena.grid(row=3, column=1, padx=20)
do_kiedy = Entry(root, width=30)
do_kiedy.grid(row=4, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Text Labels
miasto_label = Label(root, text="Miasto")
miasto_label.grid(row=0, column=0, pady=(10, 0))
mieszkanie_dom_label = Label(root, text="Mieszkanie/Dom")
mieszkanie_dom_label.grid(row=1, column=0)
wynajem_sprzedaz_label = Label(root, text="Wynajem/Sprzedaz")
wynajem_sprzedaz_label.grid(row=2, column=0)
cena_label = Label(root, text="Cena")
cena_label.grid(row=3, column=0)
do_kiedy_label = Label(root, text="Termin")
do_kiedy_label.grid(row=4, column=0)
delete_box_label = Label(root, text="ID Numer")
delete_box_label.grid(row=9, column=0)

# Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
# Create a query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a delete button
delete_btn = Button(root, text="Delete records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a update button
update_btn = Button(root, text="Update records", command=update)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Commit Changes
conn.commit()
# Close connect
conn.close()

root.mainloop()
