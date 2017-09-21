from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model

from plone.i18n.normalizer import idnormalizer
#idnormalizer.normalize(entry['filmID'])
from zope import schema
from zope.interface import provider, directlyProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


def repo_vocab(context):
    try:
        voc = []
        local_context = context
        if context.portal_type == 'polklibrary.archives.ohms.models.ohmsfile':
            local_context = context.aq_parent
                    
        subjects = local_context.subject_headings.replace('\n\r','|').replace('\n','|')
        subjects = subjects.split('|')
        
        for subject in subjects:
            csubject = subject.strip()
            voc.append(SimpleVocabulary.createTerm(csubject, csubject))
            
        return SimpleVocabulary(voc)
    except Exception as e:
        print "ERROR: " + str(e)
        return SimpleVocabulary([])
        
directlyProvides(repo_vocab, IContextSourceBinder)


class IOHMSFile(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )

    description = schema.Text(
            title=u"Description",
            required=False,
        )

    subject_headings = schema.List(
            title=u"Subject Headings",
            required=False,
            value_type=schema.Choice(source=repo_vocab,missing_value=''),
            missing_value=[],
        )
        
    file = NamedBlobFile(
            title=u"OHMS XML File",  
            required=False
        )

    
    


    
    

