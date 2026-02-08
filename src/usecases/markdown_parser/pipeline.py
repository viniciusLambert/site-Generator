from usecases.markdown_parser.splitter import split_nodes_delimiter, split_nodes_image, split_nodes_links
from domain.text_node import TextNode
from domain.text_type import TextType

def text_to_textnodes(text):
    node = [TextNode(text, TextType.PLAIN)]
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    node = split_nodes_image(node)
    node = split_nodes_links(node)
    return node
