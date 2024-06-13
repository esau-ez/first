import flet as ft
from dotenv import load_dotenv
import mysql.connector
import os
class LoginScreen(ft.Container):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.expand=True
        self.alignment = ft.alignment.center
        self.password = ft.TextField(
            hint_text="Ingrese su contraseña",
            hint_style=ft.TextStyle(
                font_family="Poppins",
                color="#7F7F7F"
            ),
            password=True,
            can_reveal_password=True
        )
        self.username = ft.TextField(
            hint_text="Ingrese su usuario",
            hint_style=ft.TextStyle(
                font_family="Poppins",
                color="#7F7F7F"
            ),
        )
        self.content = ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=self.go_back
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                "B i e n v e n i d o !",
                                size=23,
                                font_family="Poppins-SB",
                                height=60
                            ),
                            self.username,
                            self.password,
                            ft.ElevatedButton(
                                "Iniciar sesión",
                                on_click=self.login,
                                width=400,
                                height=50
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=20
                    ),
                ],
            )
        )

    def consulta(self,query):
        load_dotenv()
        DBHost = os.getenv("MYSQL_HOST")
        DBUser = os.getenv("MYSQL_USER")
        DBPassword = os.getenv("MYSQL_PASSWORD")
        DB=os.getenv("MYSQL_DB")
        PORT = os.getenv("MYSQL_PORT")
        conexion = mysql.connector.connect(
            host=DBHost,
            user=DBUser,
            password=DBPassword,
            database=DB,
            port=PORT
        )
        cursor = conexion.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado
    def login(self, e):
        #Declaración de un widget Dialog para informar sobre el inicio de sesión
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Error al iniciar sesión"),
            content=ft.Text("El usuario o la contraseña son incorrectos"),
            actions=[
                ft.TextButton("Entendido",on_click=self.close_dlg)
            ]
        )
        self.unexpected_error = ft.AlertDialog(
            modal=True,
            title=ft.Text("Error inesperado"),
            content=ft.Text("No se ha podido conectar correctamente con la base de datos"),
            actions=[
                ft.TextButton("Entendido",on_click=self.close_dlg)
            ],
        )
        input_username = self.username.value
        input_password = self.password.value
        self.username.value = ""
        self.password.value = ""
        self.update()
        try:
            query=f"SELECT password FROM usuarios_64706 WHERE username='{input_username}'"
            response_1 = self.consulta(query)
        except:
            self.unexpected_error.open = True
            self.page.dialog = self.unexpected_error
            self.page.update()
        if response_1:
            password=response_1[0][0]
            if (input_password == password):
                self.app.route_to('/puntear')
            else:
                self.dlg_modal.open = True
                self.page.dialog = self.dlg_modal
                self.page.update()
        else:
            self.dlg_modal.open = True
            self.page.dialog = self.dlg_modal
            self.page.update()
    def close_dlg(self,e):
        self.dlg_modal.open = False
        self.unexpected_error.open = False
        self.page.update()
    def go_back(self, e):
        self.app.route_to('/')
