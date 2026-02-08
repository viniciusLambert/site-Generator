from domain.block_type import BlockType
import re

def block_to_block_type(text):
    
    if(re.findall(r"^#* ([A-z])\w+", text)):
        return BlockType.HEADING
    if(len(re.findall("```", text)) == 2):
        return BlockType.CODE
    
    number_of_lines = len(text.split("\n"))
    non_empty = [line for line in text.split('\n') if line.strip() != ""]
    
    if(non_empty and all(line.lstrip().startswith(">") for line in non_empty)):
        return BlockType.QUOTE
    
    if(len(re.findall(r"-\s([A-z])\w+", text)) == number_of_lines):
        return BlockType.UNORDERED_LIST
    
    if(len(re.findall(r"[0-9]+.\s([A-z])\w+", text)) == number_of_lines):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    

