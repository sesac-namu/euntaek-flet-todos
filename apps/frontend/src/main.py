import flet as ft

from router import Router


def main(page: ft.Page):
    router = Router.create(page)

    counter = ft.Text("0", size=50, data=0)
    page_text = ft.Text(f"Page: {page.route}")

    def increment(e):
        counter.data += 1
        counter.value = str(counter.data)
        page.route = f"/{counter.data}"
        page_text.value = f"Page: {page.route}"
        # counter.update()
        # page.update()
        # page_text.update()
        page.update()

    router.add_route(
        "/",
        [
            ft.SafeArea(
                ft.Container(
                    ft.Column(
                        [
                            page_text,
                            counter,
                            ft.Button("increment", on_click=increment),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                ),
                expand=True,
            )
        ],
    )

    router.navigate("/")

    # page.add(
    #     ft.SafeArea(
    #         ft.Container(
    #             ft.Column(
    #                 [
    #                     page_text,
    #                     counter,
    #                     ft.Button("increment", on_click=increment),
    #                 ],
    #                 alignment=ft.MainAxisAlignment.CENTER,
    #             ),
    #             alignment=ft.alignment.center,
    #         ),
    #         expand=True,
    #     )
    # )


ft.app(main)
