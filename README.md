<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-rss-link-view.svg?maxAge=3600)](https://pypi.org/project/django-rss-link-view/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-rss-link-view.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-rss-link-view.py/actions)

### Installation
```bash
$ [sudo] pip install django-rss-link-view
```

##### `views.py`
```python
from django_rss_link_view.views import RssLinkMixin

class MyView(RssLinkMixin,...):
    def get_atom_title(self):
        return 'atom title'

    def get_atom_url(self):
        return 'path/to/atom.xml'

    def get_rss_title(self):
        return 'rss title'

    def get_rss_url(self):
        return 'path/to/rss.xml'
```

```python
class MyView(RssLinkMixin,...):
    atom_title = 'atom title'
    atom_url = 'path/to/atom.xml'
    rss_title = 'rss title'
    rss_url = 'path/to/rss.xml'
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
