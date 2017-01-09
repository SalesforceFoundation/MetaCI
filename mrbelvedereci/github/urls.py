from django.conf.urls import url

from mrbelvedereci.github import views as github_views

urlpatterns = [
    url(r'/(?P<owner>\w+)/(?P<name>[^/].*)/branch/(?P<branch>.*)$', github_views.branch_detail, name="branch_detail"),
    url(r'/(?P<owner>\w+)/(?P<name>[^/].*)/commit/(?P<sha>\w+)$', github_views.commit_detail, name="commit_detail"),
    url(r'/(?P<owner>\w+)/(?P<name>[^/].*)/branches', github_views.repo_branches, name="repo_branches"),
    url(r'/(?P<owner>\w+)/(?P<name>[^/].*)/triggers', github_views.repo_triggers, name="repo_triggers"),
    url(r'/(?P<owner>\w+)/(?P<name>[^/].*)/*$', github_views.repo_detail, name="repo_detail"),
    url(r'/webhook/github/push$', github_views.github_push_webhook, name="github_push_webhook"),
    url(r'$', github_views.repo_list, name="repo_list"),
]
