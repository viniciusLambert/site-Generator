import os

from usecases.converter.markdown_to_html_node import markdown_to_html_node
from usecases.markdown_parser.extract import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    if not os.path.exists(dir_path_content):
        raise Exception(f"source directory {dir_path_content} don't exist")
    
    if not os.path.exists(dest_dir_path):
        raise Exception(f"destination directory {dest_dir_path} don't exist")
    
    files_to_migrate = os.listdir(dir_path_content)
    for file in files_to_migrate:
        source_file_path = os.path.join(dir_path_content, file)
        destination_file_path = os.path.join(dest_dir_path, file)
        if(os.path.isfile(source_file_path)):
            destination_file_path = destination_file_path.removesuffix(".md") + ".html"
            generate_page(source_file_path, template_path, destination_file_path, base_path)
        else:
            os.makedirs(destination_file_path, exist_ok=True)
            generate_pages_recursive(source_file_path, template_path, destination_file_path, base_path) 

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_content = get_file_content(from_path)
    template = get_file_content(template_path)

    nodes = markdown_to_html_node(md_content)
    title = extract_title(md_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", nodes.to_html())
    template = template.replace('href="/', f'href="{base_path}')
    template = template.replace('src="/', f'src="{base_path}')

    dir_name = os.path.dirname(dest_path)
    
    print(dir_name)
    os.makedirs(dir_name, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)
    
def get_file_content(path):
    with open(path, "r", encoding="utf-8") as f:
        template = f.read()
        return template
