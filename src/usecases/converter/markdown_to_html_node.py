from .markdown_to_blocks import markdown_to_blocks
from .block_to_block_type import block_to_block_type
from usecases.markdown_parser.pipeline import text_to_textnodes
from .text_to_html import text_node_to_html_node

from domain.block_type import BlockType
from domain.parent_node import ParentNode
from domain.leaf_node import LeafNode
def markdown_to_html_node(markdown):
    markdown = markdown_to_blocks(markdown)
    block_childs = []
    for block in markdown:
        blocktype = block_to_block_type(block)
        match blocktype:
            case BlockType.PARAGRAPH:    
                block = clean_text(block)
                text_nodes = text_to_textnodes(block)
                html_nodes = map(text_node_to_html_node, text_nodes)
                block_childs.append(ParentNode("p", children=list(html_nodes)))

            case BlockType.HEADING:
                header_level = block.count('#')
                html_node = LeafNode(f"h{header_level}", block.removeprefix(f"{header_level*"#" + " "}") )
                block_childs.append(html_node)

            case BlockType.CODE:
                block = block.split("\n")[1:-1]
                block = list(map(lambda line: " ".join(line.split()), block))
                block = "\n".join(block) + "\n"
                children_node = LeafNode("code", block)
                block_childs.append(ParentNode("pre", children=[children_node]))

            case BlockType.QUOTE:
                block = block.split("\n")
                block = list(map(lambda line: " ".join(line.split()), block))
                block = list(map(lambda line: line[2:], block)) 
                block = "\n".join(block) + "\n"
                block_childs.append(LeafNode("blockquote", block))

            case BlockType.UNORDERED_LIST:
                block = block.split("\n")
                block = list(map(lambda line: " ".join(line.split()), block))
                block = list(map(lambda line: line[2:], block)) 
                unit_list = []
                for unit in block:
                   unit_list.append(LeafNode("li", unit)) 
                block_childs.append(ParentNode("ul", children=unit_list))

            case BlockType.ORDERED_LIST:
                block = block.split("\n")
                block = list(map(lambda line: " ".join(line.split()), block))
                block = list(map(lambda line: line[3:], block)) 
                unit_list = []
                for unit in block:
                   unit_list.append(LeafNode("li", unit)) 
                block_childs.append(ParentNode("ol", children=unit_list))

            
    return ParentNode("div", children=block_childs)


def clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text

