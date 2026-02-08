import os
from infrastructure.copy_static_to_public import copy_directory


def main():
    copy_directory("static", "public")        


main()
