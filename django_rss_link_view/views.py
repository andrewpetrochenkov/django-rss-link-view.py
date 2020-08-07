__all__ = ['RssLinkMixin']

from django.utils.safestring import mark_safe


def gethtml(**kwargs):
    return mark_safe("""
<link rel="alternate" type="{type}" title="{title}" href="{url}" />
    """.format(**kwargs).strip())


class RssLinkMixin:
    atom_title = None
    atom_url = None
    rss_title = None
    rss_url = None

    def get_atom_title(self):
        return self.atom_title

    def get_atom_url(self):
        return self.atom_url

    def get_rss_title(self):
        return self.rss_title

    def get_rss_url(self):
        return self.rss_url

    def get_atom_link_html(self):
        title = self.get_atom_title()
        url = self.get_atom_url()
        if not url:
            return ''
        return gethtml(type="application/atom+xml", title=title, url=url)

    def get_rss_link_html(self):
        title = self.get_rss_title()
        url = self.get_rss_url()
        if not url:
            return ''
        return gethtml(type="application/rss+xml", title=title, url=url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(
            atom_link=mark_safe(self.get_atom_link_html()),
            rss_link=mark_safe(self.get_rss_link_html()),
        ))
        return context
