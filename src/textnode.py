from enum import Enum

class TextType(Enum):
    PLAIN = "plain text",
    BOLD = "bold text",
    ITALIC = "italic text",
    CODE = "code text",
    LINK = "links",
    IMAGE = "images" 

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        if(text_type == TextType.LINK and url == None):
            raise Exception("TextNode Link type needs url to be Not None")
        self.url = url


    def __eq__(self, other):
        if(self.text != other.text):
            return False
        if(self.text_type != other.text_type):
            return False
        if(self.url != other.url):
            return False
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value[0]}, {self.url})"




