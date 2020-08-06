from abc import ABC

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


class FilteredListSerializer(serializers.ListSerializer, ABC):
    """
    Filtering only user_id answers in serializer
    """

    def to_representation(self, data):
        data = data.filter(user=self.context.get('request').headers['user_id'])
        return super(FilteredListSerializer, self).to_representation(data)


class MyAnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for answers list
    """

    class Meta:
        list_serializer_class = FilteredListSerializer
        model = Answer
        fields = (['answer'])


class MyQuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for questions list
    """
    answers = MyAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = (['question', 'answers'])


class MyPollSerializer(serializers.ModelSerializer):
    """
    Serializer for poll's results (chain "Poll -> Question -> Answer")
    """
    questions = MyQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('title', 'questions')
