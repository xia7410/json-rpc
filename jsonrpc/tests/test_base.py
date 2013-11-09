""" Test base JSON-RPC classes."""
import unittest

from ..base import JSONRPCBaseRequest, JSONRPCBaseResponse


class TestJSONRPCBaseRequest(unittest.TestCase):

    """ Test JSONRPCBaseRequest functionality."""

    def test_data(self):
        request = JSONRPCBaseRequest()
        self.assertEqual(request.data, {})

        with self.assertRaises(ValueError):
            request.data = []

        with self.assertRaises(ValueError):
            request.data = None


class TestJSONRPCBaseResponse(unittest.TestCase):

    """ Test JSONRPCBaseResponse functionality."""

    def test_data(self):
        response = JSONRPCBaseResponse(result="")
        self.assertEqual(response.data, {})

        with self.assertRaises(ValueError):
            response.data = []

        with self.assertRaises(ValueError):
            response.data = None
