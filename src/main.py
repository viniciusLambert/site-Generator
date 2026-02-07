from textnode import TextType, TextNode
from node_manipulation.splitNode import split_nodes_links

def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(text_node)

main()