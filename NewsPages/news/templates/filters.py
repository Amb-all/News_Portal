from django import template
import re

register = template.Library()

BAD_WORDS = ['дурак', 'тупой', 'глупость']  # можно расширять


@register.filter(name='censor')
def censor(text):
    def replace(match):
        word = match.group()
        return word[0] + '*' * (len(word) - 1)

    for bad_word in BAD_WORDS:
        pattern = re.compile(rf'\b{bad_word}\w*\b', re.IGNORECASE)
        text = pattern.sub(replace, text)
    return text
