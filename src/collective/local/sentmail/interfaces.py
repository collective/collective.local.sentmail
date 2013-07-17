# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.supermodel import model
from plone.theme.interfaces import IDefaultPloneLayer


class ICollectiveLocalSentmailLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class ISentMail(model.Schema):
    """Schema for sent mail"""
    pass
