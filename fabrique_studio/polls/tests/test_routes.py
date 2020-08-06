"""
Test for all routes
"""
from rest_framework.test import APIClient


def test_route_polls(test_polls):
    """
    Test for route /api/polls
    :return:
    """
    client = APIClient()
    response = client.get('/api/polls/')
    assert response.status_code == 200


def test_route_vote_poll(test_polls):
    """
    Test for vote in poll /api/poll/8
    :return:
    """
    client = APIClient()
    data = {
        "poll": 8,
        "question": 4,
        "answer": "More than dogs"
    }

    response = client.post('/api/polls/8/', data, format='json')
    assert response.status_code == 201
