from django.forms.widgets import Textarea
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.encoding import force_text


class BootstrapMarkdownWidget(Textarea):
    class Media:
        css = {
            'all': (
                'cmsplugin_markdown/bootstrap-markdown/css/bootstrap.min.css',
                'cmsplugin_markdown/bootstrap-markdown/css/bootstrap-markdown.min.css',
            )
        }
        js = (
            'cmsplugin_markdown/bootstrap-markdown/js/jqnoconflict.js',
            'cmsplugin_markdown/bootstrap-markdown/js/bootstrap.min.js',
            'cmsplugin_markdown/bootstrap-markdown/js/markdown.js',
            'cmsplugin_markdown/bootstrap-markdown/js/to-markdown.js',
            'cmsplugin_markdown/bootstrap-markdown/js/bootstrap-markdown.js',
        )

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        # first argument of format_html converted to unicode
        return format_html(u'<textarea{0}>\r\n{1}</textarea>',
                           flatatt(final_attrs),
                           force_text(value))
