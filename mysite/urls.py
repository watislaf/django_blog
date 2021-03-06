from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

from django_registration.forms import RegistrationFormUniqueEmail
from django_registration.views import RegistrationView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

sitemaps = {
    'posts': PostSitemap,
}
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('rosetta/', include('rosetta.urls')),
    path('orders/', include('orders.urls', namespace = 'orders')),
    path('cart/', include('cart.urls', namespace = 'cart')),
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls', namespace = 'payment')),
    path('blog/', include('blog.urls', namespace = 'blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name = 'django.contrib.sitemaps.views.sitemap'),
    path('account/', include('account.urls', namespace = 'account')),
    path('social-auth/',
         include('social_django.urls', namespace = 'social')),
    path('images/', include('images.urls', namespace = 'images')),
    path('', include('shop.urls', namespace = 'shop')),
    url(r'^account/register/$',
        RegistrationView.as_view(form_class = RegistrationFormUniqueEmail),
        name = 'registration_register'),
    url(r'^account/', include('django_registration.backends.activation.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
