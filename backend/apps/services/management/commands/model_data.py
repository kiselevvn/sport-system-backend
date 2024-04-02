import djclick as click
from django.apps import apps
from django.core.management import call_command
from tqdm import tqdm


@click.command()
def command():
    def get_name():
        return ""

    def get_path(file_name, folder=None):
        if folder:
            return f".\docs\diagrams\src\class\{folder}\{file_name}.puml"
        return f".\docs\diagrams\src\class\{file_name}.puml"

    plant_entities = {
        "organization": ["ChildGroup", "EducationGroup", "Organization"],
        "users": ["User", "ProxyGroup", "Sportsman", "Employee"],
        "competitions": ["SportCategory", "SportDiscipline"],
        "examination": [
            "Examination",
            "GroupExaminations",
            "ResultExamination",
            "ResultIndicator",
            "Unit",
            "Indicator",
            "CategoryIndicators",
            "ExaminationTemplate",
            "ExaminationTemplateIndicators",
            "GroupIndicators",
            "IndicatorWeight",
        ],
        "testing": [
            "ResultAnswer",
            "ResultQuestion",
            "ResultTest",
            "Answer",
            "MediaObject",
            "Question",
            "TestTemplate",
        ],
    }

    # for app in tqdm(apps.get_app_configs()):

    #     print(
    #         app.__class__.__name__,
    #         ":",
    #         [model.__name__ for model in app.get_models()],
    #         ",",
    #     )
    # for model in app.get_models():
    #     print("\t", model)
    for e in plant_entities.keys():
        call_command(
            "generate_puml",
            "--file",
            get_path(file_name=e, folder="v2"),
            "--include",
            e,
            "--add-help",
            "--add-choices",
            "--add-legend",
            "--add-omitted-headers",
        )
