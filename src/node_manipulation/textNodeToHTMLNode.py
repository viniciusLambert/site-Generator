from textnode import TextNode, TextType
from leafnode import LeafNode 

def text_node_to_html_node(node: TextNode):

    match node.text_type:
        case TextType.PLAIN:
            return LeafNode(None, node.text, None)
        case TextType.BOLD:
            return LeafNode("b", node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", node.text, None)
        case TextType.CODE:
            return LeafNode("code", node.text, None)
        case TextType.IMAGE:
            return LeafNode("img", node.text, {"src": node.url}) # type: ignore
        case TextType.LINK:
            return LeafNode("a", node.text, {"href": node.url}) # type:ignore
        case _:
            raise Exception("TextType not Found")
