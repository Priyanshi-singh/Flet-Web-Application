
import flet
from flet import (
    Page,
    Text,
    View,
    Column,
    Container,
    LinearGradient,
    alignment,
    border_radius,
    padding,
    Row,
    Card,
    TextField,
    FilledButton,
    SnackBar,
)
import requests


def main(page: Page):
    page.title = "Routes Example"
    snack = SnackBar(
        Text("Registration successfull!"),
    )

    def GradientGenerator(start, end):
        ColorGradient = LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=[
                start,
                end,
            ],
        )

        return ColorGradient

    def req_register(e, email, password):
        data = {
            "email": email,
            "password": password,
        }

        # call a POST request and route our data to the server URL and at the same time we pass in our data
        res = requests.post("http://127.0.0.1:5000/register", json=data)
        if res.status_code == 201:
            snack.open = True
            page.update()
        else:
            snack.content.value = "You were not registered! Try again."
            snack.open = True
            page.update()

    def req_login(e, email, password):
        data = {
            "email": email,
            "password": password,
        }
        #login request post
        res = requests.post("http://127.0.0.1:5000/login", json=data)
        if res.status_code == 201:
            page.views.append(
                View(
                    f"/{email}",
                    horizontal_alignment="center",
                    vertical_alignment="center",
                    controls=[
                        Column(
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                Text(
                                    "Succssesfuly Logged in!",
                                    size=44,
                                    weight="w700",
                                    text_align="center",
                                ),
                                Text(
                                    f"Login Information:\nEmail: {email}\nPassword: {password}",
                                    size=32,
                                    weight="w500",
                                    text_align="center",
                                ),
                            ],
                        ),
                    ],
                )
            )

        else:
            snack.content.value = "Could not log in! Try again."
            snack.open = True
            page.update()

        page.update()

    def route_change(route):
        email = TextField(
            label="Email",
            border="underline",
            width=320,
            text_size=14,
        )

        password = TextField(
            label="Password",
            border="underline",
            width=320,
            text_size=14,
            password=True,
            can_reveal_password=True,
        )

        page.views.clear()
        # registration page
        page.views.append(
            View(
                "/register",
                horizontal_alignment="end",
                vertical_alignment="center",
                padding=padding.only(right=160),
                controls=[
                    Column(
                        alignment="center",
                        controls=[
                            Card(
                                elevation=15,
                                content=Container(
                                    width=550,
                                    height=550,
                                    padding=padding.all(30),
                                    gradient=GradientGenerator("#1f2937", "#111827"),
                                    border_radius=border_radius.all(12),
                                    content=Column(
                                        horizontal_alignment="center",
                                        alignment="start",
                                        controls=[
                                            Text(
                                                "REGISTRATION FORM ",
                                                size=32,
                                                weight="w700",
                                                text_align="center",
                                            ),
                                            Text(
                                                "This Flet web-app/registration page is routed to a python (Flask-based) API. Registering sends a request to the API-specific rout and performs several functions.",
                                                size=14,
                                                weight="w700",
                                                text_align="center",
                                                color="#64748b",
                                            ),
                                            Container(padding=padding.only(bottom=20)),
                                            email,
                                            Container(padding=padding.only(bottom=10)),
                                            password,
                                            Container(padding=padding.only(bottom=20)),
                                            Row(
                                                alignment="center",
                                                spacing=20,
                                                controls=[
                                                    FilledButton(
                                                        content=Text(
                                                            "Register",
                                                            weight="w700",
                                                        ),
                                                        width=160,
                                                        height=40,
                                                        # pass the input values to the function that sends HTTP requests
                                                        on_click=lambda e: req_register(
                                                            e,
                                                            email.value,
                                                            password.value,
                                                        ),
                                                    ),
                                                    FilledButton(
                                                        content=Text(
                                                            "Login",
                                                            weight="w700",
                                                        ),
                                                        width=160,
                                                        height=40,
                                                        on_click=lambda __: page.go(
                                                            "/login"
                                                        ),
                                                    ),
                                                    snack,
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            )
                        ],
                    )
                ],
            )
        )

        if page.route == "/login":
            page.views.append(
                View(
                    "/login",
                    horizontal_alignment="center",
                    vertical_alignment="center",
                    controls=[
                        Column(
                            alignment="center",
                            controls=[
                                Card(
                                    elevation=15,
                                    content=Container(
                                        width=550,
                                        height=550,
                                        padding=padding.all(30),
                                        gradient=GradientGenerator(
                                            "#2f2937", "#251867"
                                        ),
                                        border_radius=border_radius.all(12),
                                        content=Column(
                                            horizontal_alignment="center",
                                            alignment="start",
                                            controls=[
                                                Text(
                                                    "LOGIN FORM ",
                                                    size=32,
                                                    weight="w700",
                                                    text_align="center",
                                                ),
                                                Text(
                                                    "This Flet web-app/registration page is routed to a python (Flask-based) API. Registering sends a request to the API-specific rout and performs several functions.",
                                                    size=14,
                                                    weight="w700",
                                                    text_align="center",
                                                    color="#64748b",
                                                ),
                                                Container(
                                                    padding=padding.only(bottom=20)
                                                ),
                                                email,
                                                Container(
                                                    padding=padding.only(bottom=10)
                                                ),
                                                password,
                                                Container(
                                                    padding=padding.only(bottom=20)
                                                ),
                                                Row(
                                                    alignment="center",
                                                    spacing=20,
                                                    controls=[
                                                        FilledButton(
                                                            content=Text(
                                                                "Login",
                                                                weight="w700",
                                                            ),
                                                            width=160,
                                                            height=40,
                                                            on_click=lambda e: req_login(
                                                                e,
                                                                email.value,
                                                                password.value,
                                                            ),
                                                        ),
                                                        FilledButton(
                                                            content=Text(
                                                                "Create acount",
                                                                weight="w700",
                                                            ),
                                                            width=160,
                                                            height=40,
                                                            on_click=lambda __: page.go(
                                                                "/register"
                                                            ),
                                                        ),
                                                        snack,
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                )
                            ],
                        )
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


#flet.app(target=main, host="localhost", port=9999,view=flet.WEB_BROWSER )
flet.app(target=main)