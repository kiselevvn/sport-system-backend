import os
import xml.etree.ElementTree as ET

from django.apps import apps
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

_DIRECTORY = os.path.join(settings.PROJECT_DIR, "Np23074")
_DIRECTORIES = os.listdir(_DIRECTORY)
MODERATED_NAMES = [
    "A001",
    # "C001",
    # "C002",
    # "C003",
    # "C004",
    # "C005",
    # "C006",
    # "C007",
    # "C008",
    # "C009",
    # "C010",
    # "C011",
    # "D001",
    # "D002",
    # "D003",
    # "D004",
    # "D005",
    # "D006",
    # "D007",
    # "D008",
    # "D009",
    # "D010",
    # "D011",
    # "E001",
    # "E002",
    # "E003",
    # "E004",
    # "E005",
    # "F001",
    # "F002",
    # "F003",
    # "N001",
    # "N002",
    # "N003",
    # "O001",
    # "O002",
    # "O004",
    # "O005",
    # "O006",
    # "O007",
    # "P001",
    # "P002",
    # "P003",
    # "P004",
    # "P005",
    # "P006",
    # "P007",
    # "P008",
    # "P009",
    # "P010",
    # "P011",
    # "P012",
    # "S001",
    # "S002",
    # "T001",
    # "T002",
    # "T003",
    # "T005",
]


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
    def get_model_name(cls, file_name):
        return file_name.split("-")[0]

    @classmethod
    def _create_model_from_xml(cls, xml_node, file_name):
        """
        Функция для создания модели Django на основе XML-узла
        Создание класса модели Django
        """
        class_name = file_name.split("-")[0]
        fields = {
            "is_actual": models.BooleanField(
                verbose_name=_("Является актуальным"),
                default=True,
            )
        }

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
    def create_instance_from_xml(
        cls,
    ):
        """
        Функция для создания модели Django на основе XML-узла
        Создание класса модели Django
        """
        models_pool = []
        for fn in cls.get_file_names():
            model_name = cls.get_model_name(fn)
            if model_name in MODERATED_NAMES:
                nodes = cls.get_nodes(file_name=fn)
                for node in nodes:
                    model = apps.get_model("np", model_name)
                    instance = model()
                    for a in node:
                        setattr(instance, a.tag, a.text)
        return models_pool
        # class_name = file_name.split("-")[0]
        # fields = {
        #     "is_actual": models.BooleanField(
        #         verbose_name=_("Является актуальным"),
        #         default=True,
        #     )
        # }

        # # Создание полей модели на основе атрибутов XML-узла
        # for attribute in xml_node:
        #     field_name = attribute.tag
        #     field_value = attribute.text
        #     # Определение типа поля на основе значения
        #     # целочисленные значеня
        #     field_type = models.CharField(
        #         max_length=255, blank=True, null=True
        #     )
        #     if "date" in field_name:
        #         field_type = models.DateField(blank=True, null=True)
        #     elif field_value is None:
        #         field_type = models.CharField(
        #             max_length=255, blank=True, null=True
        #         )
        #     elif field_value.isdigit():
        #         field_type = models.IntegerField(blank=True, null=True)
        #     fields = {**fields, field_name: field_type}

        # model_class = type(
        #     class_name,
        #     (models.Model,),
        #     {
        #         **fields,
        #         "__module__": f"backend.apps.np.models.{class_name}",
        #     },
        # )

        # return model_class

    @classmethod
    def get_models(cls):
        models_pool = []
        for fn in cls.get_file_names():
            model_name = cls.get_model_name(fn)
            if model_name in MODERATED_NAMES:
                nodes = cls.get_nodes(file_name=fn)
                model = cls._create_model_from_xml(nodes[0], file_name=fn)
                models_pool.append(model)
        return models_pool

    @classmethod
    def get_model_names(cls):
        models_pool = []
        for fn in cls.get_file_names():
            nodes = cls.get_nodes(file_name=cls.get_model_name(fn))
            models_pool.append(fn.split("-")[0])
        return models_pool
