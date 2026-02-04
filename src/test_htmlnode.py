import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
                    props={
                        "href": "https://www.google.com",
                        "target": "_blank",
                    }
                )
        node2 = HTMLNode(
                    props={
                        "href": "https://www.google.com",
                        "target": "_blank",
                    }
                )
        self.assertEqual(node, node2)
    
    def test_diff_type(self):
        node = HTMLNode(value="normal text") 
        node2 = HTMLNode(value="different text") 
        self.assertNotEqual(node, node2)
    
    def test_different_tag(self):
        node = HTMLNode("<small>", "TextType.LINK")
        node2 = HTMLNode("<large>", "TextType.LINK")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()