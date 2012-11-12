# Build a dict of attributes (properties, instancemthods, ...)
# starting with a certain prefix, from a given instance of a class.

import re

def list_attributes(cls, prefix):
    return set([k for scls in cls.__mro__
                for k in scls.__dict__.iterkeys()
                if re.search('^' + prefix, k)])


def list_attributes_trunc(cls, prefix):
    return set([k[len(prefix):] for k in list_attributes(cls, prefix)


def dictionarize_attributes(inst, prefix):
    keys = list_attributes(inst.__class__, prefix)
    return dict([(k[len(prefix):], inst.__getattribute__(k))
                 for k in keys])


# Example
if __name__ == '__main__':

    class A(object):

        def ff_0(self, a):
            print a

        def ff_1(self, a):
            print a + 1

        @property
        def ff(self):
            return dictionarize_attributes(self, 'ff_')


    class B(A):

        pass

    b = B()
    print 'ff_0, 4'
    b.ff['0'](4)
    print 'ff_1, 5'
    b.ff['1'](5)

