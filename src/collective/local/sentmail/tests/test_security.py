import unittest2 as unittest

from plone import api

from ecreall.helpers.testing.workflow import BaseWorkflowTest

from collective.local.sentmail.testing import INTEGRATION, USERDEFS

admins = ('admin', 'manager')
members = ('bart', 'lisa', 'homer', 'marge', 'milhouse')
SENT_MAIL_PERMISSIONS = {'Access contents information': members + admins,
                         'Modify portal content': ('admin', 'manager'),
                         'View': members + admins,
                         }


class TestSecurity(unittest.TestCase, BaseWorkflowTest):
    """We test the security (workflows)."""

    layer = INTEGRATION

    def setUp(self):
        super(TestSecurity, self).setUp()
        self.portal = self.layer['portal']
        self.mails_folder = api.content.create(type="Folder",
                                               title=u"Sent mails",
                                               container=self.portal)
        self.sent_mail = api.content.create(type='sent_mail',
                                            title=u'The email I have sent',
                                            body=u'Hey guys, How are you?',
                                            recipients=['lisa', 'bart'],
                                            container=self.mails_folder)

    def test_permissions_doc(self):
        sent_mail = self.sent_mail

        # test sent mail permissions mapping
        self.assertCheckPermissions(sent_mail, SENT_MAIL_PERMISSIONS, USERDEFS)
