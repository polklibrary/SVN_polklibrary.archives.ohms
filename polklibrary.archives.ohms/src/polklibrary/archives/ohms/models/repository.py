from plone.supermodel import model
from zope import schema
from plone.app.textfield import RichText


class IRepository(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )

    description = schema.Text(
            title=u"Description",
            required=False,
        )

    subject_headings = schema.Text(
        title=u'Subject Headings',
        description=u'One entry per line',
        required=False,
        missing_value='',
    )
    
    body = RichText(
            title=u"Page",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
        