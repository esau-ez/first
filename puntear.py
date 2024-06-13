import flet as ft
import json
class Puntear(ft.Container):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.expand=True
        self.name="punteo.txt"
        with open(self.name, "r") as archivo:
            texto = archivo.read()
        self.codes = json.loads(texto)
        self.current_code=""
        self.list_view = ft.ListView(expand=True, spacing=10)
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
        selected_index=0
    )
        self.no_code = ft.AlertDialog(
            modal=True,
            content=ft.Text("Debe introducir un código de barras"),
            actions=[
                ft.TextButton("Entendido",on_click=self.close_dlg)
            ],
        )
        self.bar_code=ft.TextField(
            width=200,
            hint_text="Código de Barras",
            hint_style=ft.TextStyle(
                font_family="Poppins"
            ),
            on_change=self.on_code_change,
        )
        self.content=ft.SafeArea(
            content = ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            self.bar_code,
                            ft.ElevatedButton(
                                "Añadir",
                                on_click=self.add_product
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Container(height=20),
                    self.list_view,

                    self.nav
                ],
                expand=True
            )
        )
    def on_code_change(self, e):
        self.current_code = e.control.value

    def add_product(self, e):
        if self.current_code != "":
            if self.current_code in self.codes:
                self.codes[self.current_code] += 1
            else:
                self.codes[self.current_code] = 1
        else:
            self.no_code.open = True
            self.page.dialog = self.no_code
            self.page.update()
        self.bar_code.value=""
        self.current_code=""
        self.update_list_view()
    def close_dlg(self,e):
        self.no_code.open = False
        self.page.update()
    def remove_product(self, code):
        if code in self.codes:
            self.codes[code] -= 1
            if self.codes[code] == 0:
                del self.codes[code]
            self.update_list_view()
    def update_list_view(self):
        self.list_view.controls.clear()
        for code, quantity in self.codes.items():
            self.list_view.controls.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text(f"Nombre: {code}", color=ft.colors.BLACK, font_family="Poppins"),  # Assuming you have a way to get the name from the code
                                    ft.Text(f"Código: {code}",color=ft.colors.BLACK, font_family="Poppins"),
                                    ft.Text(f"Cantidad: {quantity}",color=ft.colors.BLACK, font_family="Poppins"),
                                ]
                            ),
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color=ft.colors.BLACK,
                                on_click=lambda e, c=code: self.remove_product(c)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    padding=10,
                    border_radius=ft.border_radius.all(5),
                    bgcolor="#B0B0B0",  # Color de fondo
                    border=ft.BorderSide(color="#B0B0B0", width=1),
                )
            )
        formated = json.dumps(self.codes)
        with open(self.name, "w") as archivo:
            archivo.write(formated)
        self.update()
    def change_page(self,e):
        print(e.control.selected_index)
        if e.control.selected_index == 0:
            self.update_list_view()
        elif e.control.selected_index == 1:
            self.app.route_to("/comprobar")