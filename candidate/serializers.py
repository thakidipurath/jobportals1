from rest_framework.serializers import ModelSerializer
from candidate.models import Candiate_profile

class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candiate_profile
        fields ="__all__"
