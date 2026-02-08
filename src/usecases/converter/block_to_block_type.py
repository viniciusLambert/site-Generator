from domain.block_type import BlockType
import re

def block_to_block_type(text):
    
    if(re.findall("^#* ([A-z])\w+", text)):
        return BlockType.HEADING
    if(len(re.findall("```", text)) == 2):
        return BlockType.CODE
    if(len(re.findall(">\s*([A-z])\w+", text)) == len(text.split("\n"))):
        return BlockType.QUOTE
    if(len(re.findall("-\s([A-z])\w+", text)) == len(text.split("\n"))):
        return BlockType.UNORDERED_LIST
    if(len(re.findall("[0-9]+.\s([A-z])\w+", text)) == len(text.split("\n"))):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    

