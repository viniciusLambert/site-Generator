import sys 
from infrastructure.copy_static_to_public import copy_directory
from usecases.generator.generate_pages import generate_pages_recursive

def main():
    base_path = "/" 
    if len(sys.argv) > 1:
        base_path= sys.argv[1]

    print(base_path)
    copy_directory("static", "docs")        
    generate_pages_recursive("content", "template.html", "docs", base_path)

main()
