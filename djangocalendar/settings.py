from django.conf import settings

DEFAULTS = {
    'FILL': '-',
    'MODEL': None,
    'LF': None,  # LOOKUP FIELD
    'TF': None,  # TITLE FIELD
    'SF': None,  # SLUG FIELD
    'CACHE': 0,
}

conf = getattr(settings, 'DJANGOCALENDAR_CONFIG', {})
conf.update({k: v for k, v in DEFAULTS.items() if k not in conf})
