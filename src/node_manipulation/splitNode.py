from textnode import TextNode, TextType
from .extractMarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN: 
            new_nodes.append(node)    
            continue 

        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception('Invalid Markdown syntax')

        for i, section in enumerate(sections):
            if section == "":
                continue
        
            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.PLAIN))
            else:
                new_nodes.append(TextNode(section, text_type))
    
    return new_nodes

def split_nodes_image(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        markdowns = extract_markdown_images(node.text)        
        if not len(markdowns):
            new_nodes.extend([
                TextNode(node.text, TextType.PLAIN)
            ])
            continue

        remaining_text = node.text 
        for alt, url in markdowns:
            before, after = remaining_text.split(f'![{alt}]({url})')
            if before:
                new_nodes.append(TextNode(before, TextType.PLAIN))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = after
        
        if(len(remaining_text) > 0): 
            new_nodes.append(TextNode(remaining_text, TextType.PLAIN))

    return new_nodes

def split_nodes_links(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes =[]
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        markdowns = extract_markdown_links(node.text)        
        if not len(markdowns):
            new_nodes.extend([
                TextNode(node.text, TextType.PLAIN)
            ])
            continue
        remaining_text = node.text 
        for alt, url in markdowns:
            before, after = remaining_text.split(f'[{alt}]({url})')
            if before:
                new_nodes.append(TextNode(before, TextType.PLAIN))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            remaining_text = after
        
        if(len(remaining_text) > 0): 
            new_nodes.append(TextNode(remaining_text, TextType.PLAIN))


    return new_nodes
        
