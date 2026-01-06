AUTHOR = 'Satya S Kada'
SITENAME = 'NANITA TECH'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("facebook", "https://www.facebook.com/"),
    ("Python.org", "https://www.python.org/"),
    ("huggingface", "https://huggingface.co/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# ... existing config above ...

# THEME SETTINGS
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'

# HIDE BLOG FEATURES (Corporate Look)
DISPLAY_ARTICLE_INFO_ON_INDEX = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# HOMEPAGE SETTINGS (Crucial)
# This moves the blog list away so your Home Page takes over
INDEX_SAVE_AS = 'blog_index.html'

# FIX FOR TRANSLATION ERRORS
import jinja2
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
def gettext(text): return text
JINJA_GLOBALS = {'gettext': gettext, '_': gettext}