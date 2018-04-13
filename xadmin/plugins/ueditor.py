# -*- coding: utf-8 -*-

import xadmin
from django.db.models import TextField
from django.conf import settings

from xadmin.views import BaseAdminPlugin, CreateAdminView, UpdateAdminView, ModelFormAdminView

from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget

class XadminUEditorWidget(UEditorWidget):
	def __init__(self, **kwargs):
		self.ueditor_options = kwargs
		self.Media.js = None
		super(XadminUEditorWidget, self).__init__(kwargs)

class UeditorPlugin(BaseAdminPlugin):
	def get_field_style(self, attrs, db_field, style, **kwargs):
		if style == 'ueditor':
			if isinstance(db_field, UEditorField):
				widget = db_field.formfield().widget
				param = {}
				param.update(widget.ueditor_settings)
				param.update(widget.attrs)
				return {'widget':XadminUEditorWidget(**param)}
		return attrs

	def block_extrahead(self, content, nodes):
		js = '<script type="text/javascript" src="%s"></script>'%(settings.STATIC_URL + "ueditor/ueditor.config.js")
		js += '<script type="text/javascript" src="%s"></script>'%(settings.STATIC_URL + "ueditor/ueditor.all.min.js")
		nodes.append(js)

xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)
xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)