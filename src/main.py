from domain.text_node import TextNode
from domain.text_type import TextType
from usecases.markdown_parser.splitter import split_nodes_links

def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(text_node)

main()
