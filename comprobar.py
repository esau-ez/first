import flet as ft
class Comprobar(ft.Container):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.expand=True
        self.alignment=ft.alignment.center
        self.nav = ft.NavigationBar(
        on_change= self.change_page,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME, 
                label="Puntear",
            ),
            ft.NavigationDestination(
                icon=ft.icons.BOOK, 
                label="Comprobar",
            ),
            ft.NavigationDestination(
                icon=ft.icons.DOWNLOAD,
                label="Cargar",
            ),
        ],
        selected_index=1
    )
        self.content=ft.Column(
            controls=[
                ft.Text("Hola Mundo"),
                self.nav
            ]
        )
    def change_page(self,e):
        print(e.control.selected_index)
        if e.control.selected_index == 0:
            self.app.route_to("/puntear")
        elif e.control.selected_index == 1:
            self.app.route_to("/comprobar")