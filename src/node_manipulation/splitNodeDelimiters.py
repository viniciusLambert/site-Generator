from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN: 
            new_nodes.append(node)    
        
        splitted_text = node.text.split(delimiter)
        if len(splitted_text) != 3:
            raise Exception('Invalid Markdown syntax')
        
        new_nodes.extend([
            TextNode(splitted_text[0], TextType.PLAIN),
            TextNode(splitted_text[1], text_type),
            TextNode(splitted_text[2], TextType.PLAIN),
        ])
    
    return new_nodes

