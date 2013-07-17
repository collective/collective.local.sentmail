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
        self.folder = self.portal['folder']
        self.login('milhouse')
        sent_mail = api.content.create(type='sent_mail',
                                       title=u'The email I have sent',
                                       body=u'Hey guys, How are you today?',
                                       container=self.folder)

    def test_sent_mail(self):
        self.assertIn('the-email-i-have-sent', self.folder)
        mymail = self.folder['the-email-i-have-sent']
        self.assertEqual(mymail.Title(), u'The email I have sent')
        self.assertEqual(mymail.Creator(), 'milhouse')
        self.assertEqual(mymail.body, u'Hey guys, How are you today?')
