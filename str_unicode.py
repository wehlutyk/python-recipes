# Forward compatible code (with Python 3) for printing info on objects

import sys

class UnicodeMixin(object):
    if sys.version_info > (3, 0):
        __str__ = lambda x: x.__unicode__()
    else:
        __str__ = lambda x: unicode(x).encode('utf-8')

class Foo(UnicodeMixin):
    def __unicode__(self):
        return u'Hello World'

