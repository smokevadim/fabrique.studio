from rest_framework import serializers
from .models import Poll, Question, Answer


class PollSerializer(serializers.ModelSerializer):
    """
    Serializer for single poll
    """
    class Meta:
        model = Poll
        fields = ('id', 'title', 'poll_start', 'poll_end', 'description')


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for questions list
    """

    class Meta:
        model = Question
        fields = (['id', 'question'])


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for answers list
    """

    class Meta:
        model = Answer
        fields = (['user', 'question', 'answer'])


class QuestionReadSerializer(serializers.ModelSerializer):
    """
    Serializer for chain "Question -> Answer"
    """

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question', 'answers')


class MyPollSerializer(serializers.ModelSerializer):
    """
    Serializer for poll's results (chain "Poll -> Question -> Answer")
    """
    answers = AnswerSerializer(many=True, read_only=True)
    poll = PollSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('poll', 'question', 'answers')
