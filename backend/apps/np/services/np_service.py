import os
import xml.etree.ElementTree as ET

from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.db import models
from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer

_DIRECTORY = os.path.join(settings.FIXTURES_DIR, "Np23074")
_DIRECTORIES = os.listdir(_DIRECTORY)
MODERATED_NAMES = [
    "A001",
    "C001",
    "C002",
    "C003",
    "C004",
    "C005",
    "C006",
    "C007",
    "C008",
    "C009",
    "C010",
    "C011",
    "D001",
    "D002",
    "D003",
    "D004",
    "D005",
    "D006",
    "D007",
    "D008",
    "D009",
    "D010",
    "D011",
    "E001",
    "E002",
    "E003",
    "E004",
    "E005",
    "F001",
    "F002",
    "F003",
    "N001",
    "N002",
    "N003",
    "O001",
    "O002",
    "O004",
    "O005",
    "O006",
    "O007",
    "P001",
    "P002",
    "P003",
    "P004",
    "P005",
    "P006",
    "P007",
    "P008",
    "P009",
    "P010",
    "P011",
    "P012",
    "S001",
    "S002",
    "T001",
    "T002",
    "T003",
    "T005",
]


class CreateNpModel:
    pass


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
    def get_description(cls, file_name):
        model_name = cls.get_model_name(file_name=file_name)
        if model_name == "A001":
            return "Список справочников"
        else:
            description = None
            nodes = ET.parse(
                os.path.join(
                    cls.get_folder_path(), "A001-1.0.1-24072023_1845.xml"
                ),
            ).findall("./records/record")
            for node in nodes:
                if node.find("id_guide").text == model_name:
                    description = node.find("name_guide").text

            if description == None:
                return "Нет описания"
            else:
                return description[:235]

    @classmethod
    def get_nodes(cls, file_name):
        return ET.parse(
            os.path.join(cls.get_folder_path(), file_name),
        ).findall("./records/record")

    @classmethod
    def get_model_name(cls, file_name):
        """
        Возвращает имя сущности
        """
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
            field_type = models.TextField(blank=True, null=True)
            if "date" in field_name:
                field_type = models.DateField(blank=True, null=True)
            elif "ogrn" in field_name or "inn" in field_name:
                field_type = models.CharField(
                    max_length=50, blank=True, null=True
                )
            elif field_value is None:
                field_type = models.TextField(blank=True, null=True)
            elif field_value.isdigit():
                field_type = models.IntegerField(blank=True, null=True)
            fields = {**fields, field_name: field_type}

        model_class = type(
            class_name,
            (models.Model,),
            {
                **fields,
                "__str__": lambda s: str(s.pk),
                "__module__": f"backend.apps.np.models.{class_name}",
            },
        )

        description = cls.get_description(file_name=file_name)
        model_class._meta.verbose_name_plural = class_name + ". " + description
        # model_class._meta.verbose_name_plural = class_name
        # model_class.description = description
        model_class._meta.verbose_name = class_name
        return model_class

    @classmethod
    def get_models(cls):
        models_pool = []
        for file_name in cls.get_file_names():
            model_name = cls.get_model_name(file_name)
            if model_name in MODERATED_NAMES:
                nodes = cls.get_nodes(file_name=file_name)
                model = cls._create_model_from_xml(
                    nodes[0], file_name=file_name
                )
                models_pool.append(model)
        return models_pool

    @classmethod
    def get_model_names(cls):
        models_pool = []
        for file_name in cls.get_file_names():
            models_pool.append(cls.get_model_name(file_name))
        return models_pool

    @classmethod
    def _create_admin_class_from_xml(cls, model, file_name):
        """ """
        class_name = cls.get_model_name(file_name) + "Admin"
        admin_class = type(
            class_name,
            (admin.ModelAdmin,),
            {
                # **fields,
            },
        )
        admin.site.register(model, admin_class)

    @classmethod
    def get_admins(cls):
        """
        Возвращает классы панели администрирования
        """
        models_pool = []
        for file_name in cls.get_file_names():
            model_name = cls.get_model_name(file_name)
            if model_name in MODERATED_NAMES:
                model = apps.get_model("np", model_name)
                model = cls._create_admin_class_from_xml(
                    model, file_name=file_name
                )
                models_pool.append(model)
        return models_pool

    @classmethod
    def _create_view_set(cls, model, file_name):
        queryset = model.objects.all()
        model_name = cls.get_model_name(file_name)
        meta_serializer = type(
            "Meta", (object,), dict(model=model, fields="__all__")
        )
        serializer_class = type(
            model_name + "Serializer",
            (ModelSerializer,),
            dict(Meta=meta_serializer),
        )
        view_set = type(
            model_name + "ViewSet",
            (viewsets.ModelViewSet,),
            {"serializer_class": serializer_class, "queryset": queryset},
        )

        return view_set

    @classmethod
    def register_endpoints(cls, router):
        """
        Регестрирует маршруты в роутере
        """
        models_pool = []
        for file_name in cls.get_file_names():
            model_name = cls.get_model_name(file_name)
            if model_name in MODERATED_NAMES:
                # nodes = cls.get_nodes(file_name=file_name)
                model = apps.get_model("np", model_name)
                view_set = cls._create_view_set(model, file_name=file_name)
                router.register(
                    model_name,
                    view_set,
                    basename=model_name,
                )
                models_pool.append(model)
        return models_pool

    @classmethod
    def bulk_create_from_nodes(cls, nodes, model):
        """
        Создает записи на основе xml и модели
        """
        objects = []
        for node in nodes:
            attributes = {}
            for attribute in node:
                if "date" in attribute.tag and attribute.text is not None:
                    attributes[attribute.tag] = "-".join(
                        reversed(attribute.text.split("."))
                    )
                else:
                    attributes[attribute.tag] = attribute.text
            instance = model(**attributes)
            objects.append(instance)
        model.objects.bulk_create(objects)

    @classmethod
    def load_data(
        cls,
    ):
        """
        Загружает данные справочников
        """
        for file_name in cls.get_file_names():
            model_name = cls.get_model_name(file_name)
            if model_name in MODERATED_NAMES:
                nodes = cls.get_nodes(file_name=file_name)
                model = apps.get_model("np", model_name)
                cls.bulk_create_from_nodes(nodes, model)
