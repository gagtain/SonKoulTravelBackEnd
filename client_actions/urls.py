from django.urls import path
from .views import (
    CommentStarView,
    CommentNameView,
    CommentTextView,
    CommentViewList,
    CommentImageView,
    BlogPostView,
    CommentViewRetrieveUpdateDestroy,
    BlogPostRetrieveUpdateDestroy,
    FormQuestionView,
)

urlpatterns = [

    path('stars/', CommentStarView.as_view(), name='star_comments'),
    path('name/', CommentNameView.as_view(), name='name_comments'),
    path('text/', CommentTextView.as_view(), name='text_comments'),
    path('image/', CommentImageView.as_view(), name='image_comments'),
    path('commentView/', CommentViewList.as_view(), name='view_comment'),
    path('commentView/<int:pk>/', CommentViewRetrieveUpdateDestroy.as_view(), name='view_comments'),
    path('blog_post/', BlogPostView.as_view(), name='blog_post'),
    path('blog_post/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name='blog_post'),
    path('form_question/', FormQuestionView.as_view(), name='form_question'),
    path('form_question_email/', FormQuestionView.as_view(), name='form_question_email'),
    path('form_question/<int:pk>/', FormQuestionView.as_view(), name='form_questions'),

]
