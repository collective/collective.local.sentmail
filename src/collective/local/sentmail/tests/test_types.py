# -*- coding: utf8 -*-

import unittest2 as unittest

from plone import api

from ecreall.helpers.testing.base import BaseTest

from collective.local.sentmail.testing import INTEGRATION


class TestTypes(unittest.TestCase, BaseTest):
    """Test new content types"""

    layer = INTEGRATION

    def setUp(self):
        super(TestTypes, self).setUp()
        self.portal = self.layer['portal']
        self.sent_mail = api.content.create(type='sent_mail',
                                            title=u'The email I have sent',
                                            container=self.portal)

    def test_sent_mail(self):
        self.assertIn('the-email-i-have-sent', self.portal)
