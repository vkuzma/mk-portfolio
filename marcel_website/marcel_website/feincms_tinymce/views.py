
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404, HttpResponseForbidden, HttpResponse
from feincms.module.page.models import Page
from feincms.views.base import Handler


class PageIdFallbackHandler(Handler):
    """ This handler allows for calling a page by its id instead of URL.
        In case a page got moved and the link was hardcoded.
        The URL must be in the form /en/mypage/?p=10
    """
    def __call__(self, request, path=None):
        try:
            page = Page.objects.best_match_for_path(path, raise404=True)
            return self.build_response(request, page)
        except Http404:
            try:
                page = get_object_or_404(Page, pk=request.GET.get('p', None))
            except ValueError:
                raise Http404
            return redirect(page)

handler = PageIdFallbackHandler()


def pageurl(request):
    """ This view is for the raw-id plugin for TinyMCE.
    """
    if not request.is_ajax() or not request.GET.get('pid', None):
        return HttpResponseForbidden()
    page = get_object_or_404(Page, pk=request.GET.get('pid'))
    return HttpResponse(page.get_absolute_url()+'?p=%s' % page.id)