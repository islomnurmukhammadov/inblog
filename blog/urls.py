from django.urls import path
from .views import homeView, aboutView, blogView, oneBlogPostView, solutionsView, oneSolutionPostView
urlpatterns=[
    path('', homeView.as_view(), name='home'),
    path('about/', aboutView.as_view(), name='about'),
    path('blog/', blogView.as_view(), name='blog'),
    path('blog/<int:pk>/', oneBlogPostView.as_view(), name='post'),
    path('solutions/', solutionsView.as_view(),name='solutions'),
    path('solutions/<int:pk>/', oneSolutionPostView.as_view(), name='solution')
]