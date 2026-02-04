import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_diff_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_different_url(self):
        node = TextNode("This is a text node", TextType.LINK, "url.com")
        node2 = TextNode("This is a text node", TextType.LINK, "url.net")
        self.assertNotEqual(node, node2)
    
    def test_missing_url(self):
        with self.assertRaises(Exception):
            node = TextNode("This is a text node", TextType.LINK) 
    
    def test_present_url(self):
        node = TextNode("This is a text node", TextType.LINK, "url.com") 
        self.assertEqual(node.url, "url.com")





if __name__ == "__main__":
    unittest.main()