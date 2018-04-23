# course/urls.py

from django.urls import path,re_path
from .views import CourseListView,CourseDetailView,CourseInfoView,CommentsView,AddCommentsView,VideoPlayView

# 要写上app的名字
app_name = "course"

urlpatterns = [
    # 课程列表
    path('list/',CourseListView.as_view(),name='course_list'),
    #课程详情
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    # 课程章节信息页
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),
    #课程评论
    re_path('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),
    #添加评论
    path('add_comment/', AddCommentsView.as_view(), name="add_comment"),
    # 课程视频播放页
    re_path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video_play"),
]