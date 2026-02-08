import os

from usecases.converter.markdown_to_html_node import markdown_to_html_node
from usecases.markdown_parser.extract import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_content = get_file_content(from_path)
    template = get_file_content(template_path)

    nodes = markdown_to_html_node(md_content)
    title = extract_title(md_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", nodes.to_html())

    dir_name = os.path.dirname(dest_path)
    
    print(dir_name)
    os.makedirs(dir_name, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)
    
def get_file_content(path):
    with open(path, "r", encoding="utf-8") as f:
        template = f.read()
        return template


