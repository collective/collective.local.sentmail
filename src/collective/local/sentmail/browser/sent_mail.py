from plone import api
from email.utils import formataddr
from Products.Five import BrowserView

class SentMailView(BrowserView):

    def __call__(self):
        creator = api.user.get(username=self.context.Creator())
        sender_fullname = creator.getProperty('fullname', None) or creator.getId()
        sender_email = creator.getProperty('email')
        if sender_email:
            self.mfrom = formataddr((sender_fullname, sender_email))
        else:
            self.mfrom = sender_fullname

        self.mto = []
        for userid in self.context.recipients:
            recipient = api.user.get(userid=userid)
            if recipient is None:
                recipient = userid
            else:
                recipient_fullname = recipient.getProperty('fullname', None) or \
                                    userid
                recipient_email = recipient.getProperty('email')

                if recipient_email:
                    recipient = formataddr((recipient_fullname, recipient_email))
                else:
                    recipient = recipient_fullname

            self.mto.append(recipient)

        return super(SentMailView, self).__call__()
