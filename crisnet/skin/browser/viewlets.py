# -*- coding: utf-8 -*-
"""
crsinet.skin

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: viewlets.py 4587 2009-02-22 22:32:37Z alain
"""
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from zope.component import getMultiAdapter


class CrisnetHeaderViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/header_crisnet.pt')

    def logo_tag(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_portal_state')
        portal = portal_state.portal()
        logoName = portal.restrictedTraverse('base_properties').logoName
        return portal.restrictedTraverse(logoName).tag()

class CrisnetFooterViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/footer_crisnet.pt')
