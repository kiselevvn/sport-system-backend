import os
import xml.etree.ElementTree as ET

from django.conf import settings
from django.db import models

_DIRECTORY = os.path.join(settings.PROJECT_DIR, "Np23074")
_DIRECTORIES = os.listdir(_DIRECTORY)


class NpService:
    """
    Сервис работы со
    справочной информацией
    """

    @classmethod
    def get_folder_path(
        cls,
    ):
        return _DIRECTORY

    @classmethod
    def get_file_names(
        cls,
    ):
        return _DIRECTORIES

    @classmethod
    def get_nodes(cls, file_name):
        return ET.parse(
            os.path.join(cls.get_folder_path(), file_name),
        ).findall("./records/record")

    @classmethod
    def _create_django_model_from_xml(cls, xml_node, file_name):
        """
        Функция для создания модели Django на основе XML-узла
        Создание класса модели Django
        """
        class_name = file_name.split("-")[0]
        fields = {}

        # Создание полей модели на основе атрибутов XML-узла
        for attribute in xml_node:
            field_name = attribute.tag
            field_value = attribute.text
            # Определение типа поля на основе значения
            # целочисленные значеня
            field_type = models.CharField(
                max_length=255, blank=True, null=True
            )
            if "date" in field_name:
                field_type = models.DateField(blank=True, null=True)
            elif field_value is None:
                field_type = models.CharField(
                    max_length=255, blank=True, null=True
                )
            elif field_value.isdigit():
                field_type = models.IntegerField(blank=True, null=True)
            fields = {**fields, field_name: field_type}

        model_class = type(
            class_name,
            (models.Model,),
            {
                **fields,
                "__module__": f"backend.apps.np.models.{class_name}",
            },
        )

        return model_class

    @classmethod
    def get_np_models(cls):
        models_pool = []
        for fn in cls.get_file_names():
            nodes = cls.get_nodes(file_name=fn)
            model = cls._create_django_model_from_xml(nodes[0], file_name=fn)
            models_pool.append(model)
        return models_pool
