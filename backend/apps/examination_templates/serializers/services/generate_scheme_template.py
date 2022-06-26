import json

from rest_framework.renderers import JSONRenderer

from ..examination_template_base_serializer import (
    ExaminationTemplateBaseSerializer,
)


def generate_scheme_template(examination_template_instance):
    serializer = ExaminationTemplateBaseSerializer(
        examination_template_instance
    )
    scheme = JSONRenderer().render(serializer.data)
    return scheme
