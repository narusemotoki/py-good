""" Misc utilities """

import six


__type_names = direct = {
    None:             _(u'None'),
    type(None):       _(u'None'),
    bool:       _(u'Boolean'),
    float:      _(u'Fractional number'),
    complex:    _(u'Complex number'),
    six.text_type:    _(u'String'),
    six.binary_type:  _(u'Binary String'),
    tuple:      _(u'Tuple'),
    list:       _(u'List'),
    set:        _(u'Set'),
    frozenset:  _(u'Frozen Set'),
    dict:       _(u'Dictionary'),
}


def register_type_name(t, name):
    """ Register a human-friendly name for the given type. This will be used in Invalid errors

    :param t: The type to register
    :type t: type
    :param name: Name for the type
    :type name: unicode
    """
    assert isinstance(t, type)
    assert isinstance(name, unicode)
    __type_names[t] = name


def get_type_name(t):
    """ Get a human-friendly name for the given type.

    :type t: type
    :rtype: unicode
    """
    # Lookup in the mapping
    try:
        return __type_names[t]
    except:
        # Specific types
        if issubclass(t, six.integer_types):
            return _(u'Integer number')

        # Get name from the Type itself
        return unicode(t.__name__).capitalize()
