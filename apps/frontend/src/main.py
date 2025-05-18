from typing import Optional
import flet as ft
from router import Router


def main(page: ft.Page):
    token: Optional[str] = None

    router = Router.create(page)

    title = ft.TextField(label="Title", data="")
    contents = ft.TextField(label="Contents", data="")

    def submit(e):
        pass

    @router.route("/")
    def Home():
        return [
            ft.SafeArea(
                ft.Container(
                    ft.Column(
                        [
                            ft.Button("Logout"),
                            title,
                            contents,
                            ft.Button(
                                "Submit",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                ),
                expand=True,
            )
        ]

    username = ft.TextField(label="Username", data="")
    password = ft.TextField(label="Password", data="", password=True)

    def login_clear(e):
        username.data = ""
        password.data = ""
        username.value = ""
        password.value = ""
        username.update()
        password.update()

    def login(e):
        pass

    @router.route("/login")
    def Login():
        return [
            ft.SafeArea(
                ft.Container(
                    ft.Column(
                        [
                            username,
                            password,
                            ft.Row(
                                [
                                    ft.Button("Clear", on_click=login_clear),
                                    ft.Button("Login"),
                                ]
                            ),
                            ft.Button(
                                "Signup", on_click=lambda e: router.navigate("/signup")
                            ),
                        ]
                    )
                )
            )
        ]

    @router.route("/signup")
    def Signup():
        return [
            ft.SafeArea(
                ft.Container(
                    ft.Row(
                        [
                            ft.Button(
                                "Login", on_click=lambda e: router.navigate("/login")
                            ),
                            ft.Text("Signup"),
                        ]
                    )
                )
            )
        ]

    router.navigate("/login")


ft.app(main)
