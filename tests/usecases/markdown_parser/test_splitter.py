import unittest

from domain.text_node import TextNode
from domain.text_type import TextType
from usecases.markdown_parser.splitter import split_nodes_delimiter, split_nodes_image, split_nodes_links

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

class TestSplitNodeImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

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
