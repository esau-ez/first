import flet as ft
class SplashScreen(ft.Container):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.expand=True
        self.alignment=ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Image(
                    src="assets/scan.png"
                ),
                ft.Text(
                    "H O L A !",
                    font_family="Poppins-SB",
                    size=23
                ),
                ft.Text(
                    "Conozca el extraordinario potencial de ScanHub y ahorre tiempo y dinero",
                    text_align=ft.TextAlign.CENTER,
                    font_family="Poppins",
                    size=13,
                    color="#7F7F7F"
                ),
                ft.ElevatedButton(
                    "Iniciar Sesion", 
                    on_click=self.go_to_login,
                    width=250
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def go_to_login(self, e):
        self.app.route_to('/login')
