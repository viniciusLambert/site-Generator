import unittest

from textnode import TextNode, TextType
from .splitNode import split_nodes_delimiter

class TestSplitNodeDelimiters(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("This is text with a **BOLD** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD) 
        self.assertEqual(new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("BOLD", TextType.BOLD),
                TextNode(" word", TextType.PLAIN),
            ]       
        )

    def test_split_italic(self):
        node = TextNode("This is text with a _Ittalicx_ word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC) 
        self.assertEqual(new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("Ittalicx", TextType.ITALIC),
                TextNode(" word", TextType.PLAIN),
            ]       
        )

    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE) 
        self.assertEqual(new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.PLAIN),
            ]       
        )

