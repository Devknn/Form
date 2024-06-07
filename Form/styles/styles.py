from enum import Enum
import reflex as rx



class EmSize(Enum):
    SMALL = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    VERY_BIG = "8em"
    

BASE_STYLE = {
    rx.input:{
        "color_scheme":"teal"
    },
    rx.button: {
    
        "--cursor-button": "pointer",
        #"_hover": {
         #   "background_color": Color.SECONDARY.value
        #}
    },
}