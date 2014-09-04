from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from ss_cms_dianzi import settings

from django.contrib import admin
admin.autodiscover()

from article.views import show_article

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ss_cms_dianzi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/$', show_article),
    url(r'^list/', include('category.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
