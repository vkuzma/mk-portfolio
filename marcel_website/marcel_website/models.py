from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent

Page.register_templates({
    'title': 'Base',
    'key': 'base',
    'path': 'base.html',
    'regions': (
        ('main', 'Main'),
        ),
    })

Page.create_content_type(RichTextContent)
