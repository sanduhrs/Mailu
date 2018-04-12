# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.alias import Alias  # noqa: E501
from swagger_server.models.alternative import Alternative  # noqa: E501
from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.fetch import Fetch  # noqa: E501
from swagger_server.models.manager import Manager  # noqa: E501
from swagger_server.models.relay import Relay  # noqa: E501
from swagger_server.models.token import Token  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_alias_get(self):
        """Test case for alias_get

        
        """
        response = self.client.open(
            '/alias',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alternative_get(self):
        """Test case for alternative_get

        
        """
        response = self.client.open(
            '/alternative',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_get(self):
        """Test case for domain_get

        
        """
        response = self.client.open(
            '/domain',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_get(self):
        """Test case for fetch_get

        
        """
        response = self.client.open(
            '/fetch',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_manager_get(self):
        """Test case for manager_get

        
        """
        response = self.client.open(
            '/manager',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_relay_get(self):
        """Test case for relay_get

        
        """
        response = self.client.open(
            '/relay',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_token_get(self):
        """Test case for token_get

        
        """
        response = self.client.open(
            '/token',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_get(self):
        """Test case for user_get

        
        """
        response = self.client.open(
            '/user',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
