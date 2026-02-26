# test_graphpulse.py
"""
Tests for GraphPulse module.
"""

import unittest
from graphpulse import GraphPulse

class TestGraphPulse(unittest.TestCase):
    """Test cases for GraphPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GraphPulse()
        self.assertIsInstance(instance, GraphPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GraphPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
