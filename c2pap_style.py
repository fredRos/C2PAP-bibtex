from pybtex.style.formatting import toplevel
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.richtext import String, Tag, Text

from pybtex.style.template import (
    join, words, field, optional, first_of,
    names, sentence, tag, optional_field, href
)

class C2PAP(UnsrtStyle):

    def newline(self):
        """<br> added twice, need nonempty string else it gets eaten before it's written out"""
        return tag("br") [String(" ")]

    def format_web_refs(self, e):
        """New line after each entry"""
        return words [
            optional [words [self.format_url(e), self.newline() ]],
            optional [words [self.format_eprint(e), self.newline() ]],
            optional [words [self.format_doi(e), self.newline() ]],
            ]

    def format_article(self, entry):
        """
        Output:

        A. Firstauthor, B. Secondauthor, and C. Thirdauthor. <br> </br>
        <b>Title</b> <br> </br>
        <a href="http://arxiv.org/abs/1603.05981">arXiv:1603.05981</a> <br> </br>
        <a href="http://dx.doi.org/10.1093/mnras/stw1649">doi:10.1093/mnras/stw1649</a> <br> </br>

        Remove extra line breaks with `sed -i 's| </br>||g'`
        """

        template = toplevel [
             self.format_names('author'), self.newline(),
             tag('b') [field('title')], self.newline(),
             self.format_web_refs(entry)
        ]

        return template.format_data(entry)


# the rests belongs into a separate file but then the setup script complained
# about the module not existing

from pybtex.backends.html import Backend as HTML
PROLOGUE = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head><meta name="generator" content="Pybtex">
<meta http-equiv="Content-Type" content="text/html; charset=%s">
<title>Bibliography</title>
</head>
<body>
"""

class Backend(HTML):
    def format_tag(self, tag, text):
        # line break should only be output once
        if tag == 'br':
            return r'<br>'
        else:
            return super(Backend, self).format_tag(tag, text)

    def write_prologue(self):
        encoding = self.encoding or pybtex.io.get_default_encoding()
        self.output(PROLOGUE % encoding)

    def write_epilogue(self):
        self.output(u'</body></html>\n')

    def write_entry(self, key, label, text):
        self.output(u'%s<br>\n\n' % text)
