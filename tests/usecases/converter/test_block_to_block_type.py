import unittest

from usecases.converter.block_to_block_type import block_to_block_type
from domain.block_type import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_head(self):
        text = "### HEADLINE"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING) 
    
    def test_block_to_block_type_quote(self):
        text = "> This is a quote"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE) 

    def test_block_to_block_type_code(self):
        text = """
                ```
                code lines
                ccccccccc
                ```
        """
        self.assertEqual(block_to_block_type(text), BlockType.CODE) 
    
    def test_block_to_block_type_unordered_list(self):
        text = """  - This is a list
                    - with items    """
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST) 

    def test_block_to_block_type_ordered_list(self):
        text = """  1. Or
                    2. de
                    3. red
                    4. list """
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST) 

    
    
    
    
    
    


