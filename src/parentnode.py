
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, 
            tag: str,
            children: list[HTMLNode],
            props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if(not self.tag):
            raise ValueError("All parent nodes must have a tag")
        
        if(not self.children):
            raise ValueError("All parent nodes must have childrens")
        
        html_string = f"<{self.tag}"
        if(self.props):
            html_string += f" {super().props_to_html()}"
        html_string += ">"

        for child in self.children:
            html_string += child.to_html()

        html_string += f"</{self.tag}>"

        return html_string

    def __repr__(self):
        return (
            "HTMLNode("
            f"tag: {self.tag},"
            f"value: {self.value},"
            f"props: {self.props})"
        )