# doc: https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/
from django import template

# register tag and filter library
register = template.Library()


# custom tags and filters here:

@register.filter
def duration_or_default(value: int, default: str) -> str:
    if value is None:
        return default
    else:
        hours = value // 60
        minutes = value % 60
        return f"{hours:02d}H{minutes:02d}mn"