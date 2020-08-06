from rest_framework.generics import ListCreateAPIView, ListAPIView
from django.utils.timezone import now

from .models import Poll, Question, Answer
from .serializers import PollSerializer, QuestionSerializer, MyPollSerializer, AnswerSerializer


# Create your views here.


class PollView(ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        return Poll.objects.filter(poll_start__lt=now(), poll_end__gt=now())


class SinglePollView(ListCreateAPIView):
    # serializer_class = QuestionSerializer

    def get_serializer_class(self):
        if hasattr(self.request, 'method'):
            if self.request.method == 'GET':
                return QuestionSerializer
            if self.request.method == 'POST':
                return AnswerSerializer

    def create(self, request, *args, **kwargs):
        if 'user_id' in request.headers:
            user_id = request.headers['user_id']
            request.data.update({'user': user_id})
        else:
            # lets allow anonymous to answer
            request.data.update({'user': 0})
        return super(SinglePollView, self).create(request, *args, **kwargs)

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Question.objects.filter(poll=self.kwargs['pk'])
        else:
            return Answer.objects.all()


class MyPollView(ListAPIView):
    """
    return results of my polls
    """
    serializer_class = MyPollSerializer

    def get_queryset(self):
        if 'user_id' in self.request.headers:
            return Poll.objects.filter(
                pk__in=Question.objects.filter(
                    pk__in=Answer.objects.filter(
                        user=self.request.headers['user_id']).values('question')).values('poll'))
