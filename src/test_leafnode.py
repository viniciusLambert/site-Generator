import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_different(self):
        node = LeafNode("p", "This is a paragraph of text.").to_html()
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertNotEqual(node, node2)
    
    def test_leaf_with_props_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())