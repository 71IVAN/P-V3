from django.urls import path
from pages.views import (
    
    authentication_signin,
    authentication_signup,
    authentication_pass_reset,
    authentication_change,
    authentication_lockscreen,
    authentication_logout,
    authentication_success_msg,
    authentication_twostep_verification,
    authentication_404_error,
    authentication_500_error,
    authentication_503_error,
    authentication_offline,
    
    pages_starter,
    pages_profile,
    pages_profile_settings,
    pages_contacts,
    pages_timeline,
    pages_faqs,
    pages_pricing,
    pages_maintenance,
    pages_coming_soon,
    pages_privacy_policy,
    pages_term_conditions,
    
)

app_name = 'pages'


urlpatterns = [
    
    # authentication
    path('authentication/signin',authentication_signin,name="authentication.signin"),
    path('authentication/signup',authentication_signup,name="authentication.signup"),
    path('authentication/pass-reset',authentication_pass_reset,name="authentication.pass_reset"),
    path('authentication/change',authentication_change,name="authentication.change"),
    path('authentication/lockscreen',authentication_lockscreen,name="authentication.lockscreen"),
    path('authentication/logout',authentication_logout,name="authentication.logout"),
    path('authentication/success-msg',authentication_success_msg,name="authentication.success_msg"),
    path('authentication/twostep-verification',authentication_twostep_verification,name="authentication.twostep_verification"),
    path('authentication/404error',authentication_404_error,name="authentication.404_error"),
    path('authentication/500error',authentication_500_error,name="authentication.500_error"),
    path('authentication/503error',authentication_503_error,name="authentication.503_error"),
    path('authentication/offline',authentication_offline,name="authentication.offline"),
    
    # pages
    path('pages/starter',pages_starter,name="pages.starter"),
    path('pages/profile',pages_profile,name="pages.profile"),
    path('pages/profile-settings',pages_profile_settings,name="pages.profile_settings"),
    path('pages/contacts',pages_contacts,name="pages.contacts"),
    path('pages/timeline',pages_timeline,name="pages.timeline"),
    path('pages/faqs',pages_faqs,name="pages.faqs"),
    path('pages/pricing',pages_pricing,name="pages.pricing"),
    path('pages/maintenance',pages_maintenance,name="pages.maintenance"),
    path('pages/coming-soon',pages_coming_soon,name="pages.coming_soon"),
    path('pages/privacy-policy',pages_privacy_policy,name="pages.privacy_policy"),
    path('pages/term-conditions',pages_term_conditions,name="pages.term_conditions"),
    
    
]