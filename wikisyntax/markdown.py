try:
    from django.contrib.markup.templatetags.markup import markdown # Django 1.4
except ImportError:
    from django_markdown.templatetags.django_markdown import markdown # Django >= 1.6
from django.utils.safestring import mark_safe
from .constants import LEFTBRACKET, RIGHTBRACKET

def wikisafe_markdown(value, lsafety=None, rsafety=None):
    lsafety = lsafety or 'LBRACK666' # Some unlikely nonsense
    rsafety = rsafety or 'RBRACK666' # Some unlikely nonsense
    value = value.replace(LEFTBRACKET, lsafety).replace(RIGHTBRACKET, rsafety)
    value = markdown(value)
    value = value.replace(lsafety, LEFTBRACKET).replace(rsafety, RIGHTBRACKET)
    return mark_safe(value)
