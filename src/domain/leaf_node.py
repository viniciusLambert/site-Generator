from domain.html_node import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,
            tag: str | None,
            value: str,
            props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if(not self.value):
            raise ValueError("All leaf nodes must have a value")

        if(not self.tag):
            return self.value

        html_string = f"<{self.tag}"
        if(self.props):
            html_string += f" {super().props_to_html()}>"
        else:
            html_string += ">"
        html_string += self.value
        html_string += f"</{self.tag}>"

        return html_string

    def __repr__(self):
        return (
            "HTMLNode("
            f"tag: {self.tag},"
            f"value: {self.value},"
            f"props: {self.props})"
        )
