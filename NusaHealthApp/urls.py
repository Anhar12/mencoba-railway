from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('blogs', views.Blog, name='blogs'),
    # path('detail-blogs', views.BlogDetail, name='detail-blogs'),
    path('blogs/<int:blog_id>/', views.BlogDetail, name='blog_detail'),
    path('activities', views.Activity, name='activities'),
    # path('detail-activities', views.ActivityDetail, name='detail-activities'),
    path('detail-activities/<int:activity_id>/', views.ActivityDetail, name='detail-activities'),
    path('contact', views.Contact, name='contact'),
    path('sign-in', views.SignIn, name='sign-in'),
    path('sign-out', views.SignOut, name='sign-out'),
    path('dashboard', views.Dashboard, name='dashboard'),
    
    path('dashboard/blogs-management', views.BlogsManagement, name='blogs-management'),
    path('dashboard/blogs-management/add', views.BlogsManagementAdd, name='blogs-management-add'),
    path('dashboard/blogs-management/update/<int:blog_id>', views.BlogsManagementUpdate, name='blogs-management-update'),
    path('dashboard/blogs-management/delete/<int:blog_id>', views.BlogsManagementDelete, name='blogs-management-delete'),
    
    path('dashboard/activities-management', views.ActivitiesManagement, name='activities-management'),
    path('dashboard/activities-management/add', views.ActivitiesManagementAdd, name='activities-management-add'),
    path('dashboard/activities-management/update/<int:activity_id>', views.ActivitiesManagementUpdate, name='activities-management-update'),
    path('dashboard/activities-management/delete/<int:activity_id>', views.ActivitiesManagementDelete, name='activities-management-delete'),
    
    path('dashboard/content-management', views.ContentManagement, name='content-management'),
    
    path('dashboard/home-management', views.HomeManagement, name='home-management'),
    path('dashboard/about-management', views.AboutManagement, name='about-management'),
    path('dashboard/contact-management', views.ContactManagement, name='contact-management'),

    path('dashboard/upload-logo', views.UploadLogo, name='upload-logo'),
    path('dashboard/upload-slider', views.UploadSlider, name='upload-slider'),
    path('dashboard/upload-hero', views.UploadHero, name='upload-hero'),
    path('dashboard/upload-services', views.UploadServices, name='upload-services'),
    path('dashboard/upload-philosophy', views.UploadPhilosophy, name='upload-philosophy'),
    path('dashboard/upload-vision-mission', views.UploadVisionMission, name='upload-vision-mission'),
    path('dashboard/upload-business-structure', views.UploadBusinessStructure, name='upload-business-structure'),
    path('dashboard/upload-solutions', views.UploadSolutions, name='upload-solutions'),
    path('dashboard/upload-contact', views.UploadContact, name='upload-contact'),
    path('dashboard/upload-location', views.UploadLocation, name='upload-location'),
]
