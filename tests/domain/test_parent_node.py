import unittest

from domain.parent_node import ParentNode
from domain.leaf_node import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_node_to_html_without_tag(self):
        child_node = LeafNode('b', "child")
        with self.assertRaises(ValueError):
            node = ParentNode("", [child_node])
            node.to_html()

    def test_node_to_html_without_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", [])
            node.to_html()
