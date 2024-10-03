import flet as ft
import mariadb
from conection import Connection
from welcome import Welcome
from clase import clase
from login import Login_page

def main(page: ft.Page):
    Login_page(page)
    
ft.app(target=main)
