from enum import Enum

class TextType(Enum):
    PLAIN = "plain text",
    BOLD = "bold text",
    ITALIC = "italic text",
    CODE = "code text",
    LINK = "links",
    IMAGE = "images"
