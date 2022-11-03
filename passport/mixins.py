class PageTitleMixin(object):
    """
    Mixin class to apply page titles
    Code used is from:
    https://iheanyi.com/journal/2020/04/04/dynamic-page-titles-in-django/
    """
    def get_page_title(self, context):
        return getattr(self, "page_title", "Default Page Title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.get_page_title(context)

        return context
