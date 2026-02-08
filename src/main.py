import os
from infrastructure.copy_static_to_public import copy_directory
from usecases.generator.generate_pages import generate_pages_recursive

def main():
    copy_directory("static", "public")        

    generate_pages_recursive("content", "template.html", "public")

main()
