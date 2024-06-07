import reflex as rx
from Form.styles import styles
from Form.styles.styles import EmSize as EmSize

@rx.page(
    
    title= "formulario",
    description= "formulario de contacto",
    image = "favicon.ico",
)

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.vstack(
                rx.heading(
                    "Formulario de contacto", 
                    size="5",
                    margin_y=EmSize.BIG.value),
                    rx.form(
                        rx.hstack(
                            rx.input(
                                placeholder="Nombre",
                                name="nombre",
                                color_scheme="teal",
                                width="50%"
                                ),
                            rx.input(
                                placeholder="Apellidos",
                                name="apellidos",
                                color_scheme="teal",
                                width="50%"
                                ),
                            width="100%",
                            margin_y=EmSize.DEFAULT.value
                            ),
                        rx.hstack(
                            rx.select(
                                ["DNI","NIE","PASSAPORTE"],
                                default_value="DNI",
                                color_scheme="teal",
                                width=EmSize.VERY_BIG.value
                                ),
                            rx.input(
                                placeholder="Ingrese documento", 
                                color_scheme="teal",
                                margin_left=EmSize.SMALL.value,
                                min_length=4,
                                max_length=20,
                                ), 
                            margin_y=EmSize.DEFAULT.value,
                            width="100%",
                            ),
                        rx.hstack(
                            rx.select(
                                ["MOVIL","CASA"],
                                default_value="MOVIL",
                                color_scheme="teal",
                                width=EmSize.VERY_BIG.value,
                                ),                         
                            rx.input(
                                placeholder="Ingrese telefono", 
                                color_scheme="teal",
                                margin_left=EmSize.SMALL.value,
                                min_length=4,
                                max_length=20
                                ), 
                            margin_y=EmSize.DEFAULT.value,
                            width="100%"
                            ),
                        rx.input(
                            placeholder="Correo electronico",
                            color_scheme="teal",
                            margin_y=EmSize.DEFAULT.value,
                            width="100%"
                            ),
                        rx.accordion.root(
                            rx.accordion.item(
                                header="Agregar dirección",
                                    content=rx.form(
                                        rx.input(placeholder="Calle"),
                                        rx.hstack(
                                            rx.input(
                                                placeholder="Número",
                                                width="40%"
                                                ),
                                            rx.spacer(),
                                            rx.divider(
                                                orientation="vertical", 
                                                size="2", 
                                                color_scheme="teal"
                                                ),
                                            rx.spacer(),
                                            rx.input(
                                                placeholder="Codigo Postal", 
                                                width="40%"
                                                ),
                                            width="100%",
                                            margin_y=EmSize.DEFAULT.value
                                        ),
                                        rx.hstack(
                                            rx.input(
                                                placeholder="Ciudad", 
                                                width="50%"
                                                ),
                                            rx.input(
                                                placeholder="País", 
                                                width="50%"
                                                )
                                            )
                                        )
                                    ),
                                    color_scheme="teal",
                                    variant="ghost",
                                    collapsible=True,
                                    width="100%",
                                    margin_y=EmSize.DEFAULT.value
                                ),
                        rx.checkbox(
                            "Aceptar termino y codinciones",
                            default_checked=True,
                            spacing="2",
                            color_scheme="teal"                
                            ),
                         rx.center(
                            rx.button(
                                "Registrar",
                                color_scheme="teal"
                                ), 
                            width="100%",
                            margin_y=EmSize.BIG.value
                            )
                        ),
                        border = "3px solid #B0B0B0" ,
                        padding="3em" ,
                        width="100%",
                        justify="center",
                        max_width="500px",        
        ),
        min_height="85vh",
    ),
    rx.logo(),
    width="100%"
)

