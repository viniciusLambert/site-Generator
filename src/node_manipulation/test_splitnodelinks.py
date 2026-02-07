import unittest

from textnode import TextNode, TextType
from .splitNode import split_nodes_links 

class TestSplitNodeLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an [url](https://i.imgur.com/zjjcJKZ.png) and another [second url](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("url", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second url", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

