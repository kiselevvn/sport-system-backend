from django.contrib.auth import get_user_model
from rest_framework import serializers

# from backend.apps.competitions.models import
from backend.apps.examination.models import ResultExamination
from backend.apps.testing.models import ResultTest


class SportsmanResultsExamination(serializers.ModelSerializer):
    class Meta:
        model = ResultExamination
        fields = "__all__"


class SportsmanResultTests(serializers.ModelSerializer):
    class Meta:
        model = ResultTest
        fields = "__all__"


# class SportsmanResultsSportCompetition(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = "__all__"


class SportsmanRetriveSerializer(serializers.ModelSerializer):
    """
    Информация о спортсменах
    """

    results_examination = SportsmanResultsExamination(
        many=True, read_only=True
    )
    result_tests = SportsmanResultTests(many=True, read_only=True)
    # results_sport_competition = SportsmanResultsSportCompetition(
    #     many=True, read_only=True
    # )

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "email",
            "gender",
            "username",
            "first_name",
            "last_name",
            "second_name",
            "birthday",
            "result_tests",
            "results_examination",
        ]
