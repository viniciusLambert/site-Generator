import re

def extract_markdown_images(text:str) -> list[list[str]]:
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def extract_markdown_links(text:str) -> list[list[str]]:
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def extract_title(markdown):
    if markdown[:2] != "# ":
        raise Exception("markdown has no title")
    markdown = markdown.split("\n")[0]
    markdown = " ".join(markdown.split(" ")[1:])
    return markdown

