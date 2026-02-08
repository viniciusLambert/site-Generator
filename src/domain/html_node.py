from __future__ import annotations

class HTMLNode():
    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: list[HTMLNode] | None = None,
            props: dict[str, str] | None = None
        ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return (
            "HTMLNode("
            f"tag: {self.tag},"
            f"value: {self.value},"
            f"children: {self.children},"
            f"props: {self.props})"
        )

    def __eq__(self, other) -> bool:
        if self.tag != other.tag:
            return False
        if self.value != other.value:
            return False
        if self.children != other.children:
            return False
        if self.props != other.props:
            return False
        return True

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result[1:]
