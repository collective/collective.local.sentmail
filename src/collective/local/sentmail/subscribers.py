from five import grok

from plone import api

from collective.local.sendto.interfaces import IMailSentEvent


@grok.subscribe(IMailSentEvent)
def mail_sent(event):
    sent_mails_folder = api.portal.get()['sent-mails']
    recipients = [recipient.getId() for recipient in event.recipients]
    api.content.create(type='sent_mail',
                       title=event.subject,
                       body=event.body,
                       recipients=recipients,
                       container=sent_mails_folder)
