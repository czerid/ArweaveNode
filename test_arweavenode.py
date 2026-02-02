# test_arweavenode.py
"""
Tests for ArweaveNode module.
"""

import unittest
from arweavenode import ArweaveNode

class TestArweaveNode(unittest.TestCase):
    """Test cases for ArweaveNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArweaveNode()
        self.assertIsInstance(instance, ArweaveNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArweaveNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
