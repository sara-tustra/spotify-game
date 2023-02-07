from django.urls import path
from .views import (
    CustomerCreate,
    CustomerList,
    CustomerDetail,
    CustomerUpdate,
    CustomerDelete,
    TournamentCreate,
    TournamentList,
    PlayerCreate,
    PlayerList,
    RoundCreate,
    RoundList,
    MatchCreate,
    MatchList,
)


urlpatterns = [
    path("create/", CustomerCreate.as_view(), name="create-customer"),
    path("", CustomerList.as_view()),
    path("<int:pk>/", CustomerDetail.as_view(), name="retrieve-customer"),
    path("update/<int:pk>/", CustomerUpdate.as_view(), name="update-customer"),
    path("delete/<int:pk>/", CustomerDelete.as_view(), name="delete-customer"),
    path("tournament/create/", TournamentCreate.as_view(), name="create-tournament"),
    path("tournament", TournamentList.as_view()),
    path("player/create/", PlayerCreate.as_view(), name="create-player"),
    path("player", PlayerList.as_view()),
    path("round/create/", RoundCreate.as_view(), name="create-round"),
    path("round", RoundList.as_view()),
    path("match/create/", MatchCreate.as_view(), name="create-match"),
    path("match", MatchList.as_view()),
]
