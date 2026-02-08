import os
from infrastructure.copy_static_to_public import copy_directory
from usecases.generator.generate_pages import generate_page

def main():
    copy_directory("static", "public")        

    generate_page("content/index.md", "template.html", "public/index.html")

main()
