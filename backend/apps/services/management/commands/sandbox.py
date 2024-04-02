import djclick as click
from tqdm import tqdm

from backend.apps.competitions.services import SportTypeServices

# from backend.apps.examination_templates.models import ExaminationTemplate
# from backend.apps.examination_templates.selectors import (
#     examination_template_selector,
# )
from backend.apps.np import models as np_models

# from backend.apps.examination_templates.services import (
#     generate_scheme_template,
# )
from backend.apps.np.services import NpService
from backend.apps.organization.models import Organization
from backend.apps.testing.models import (
    Answer,
    ResultAnswer,
    ResultQuestion,
    ResultTest,
    TestTemplate,
)

# from backend.apps.examination.selectors import ExaminationSelectors
from backend.apps.testing.selectors import TestTemplateSelectors
from backend.apps.users.models import Sportsman


@click.command()
def command():
    # Import the xlrd module
    # import openpyxl

    # # Open the Workbook
    # workbook = openpyxl.load_workbook(
    #     r"C:\Users\Vladimir Kiselev\projects\sport-system-backend\backend\fixtures\Perechen_Yu_L_2024_588ca6de3e.xlsx"
    # )
    # worksheet = workbook.active
    # instances = []
    # for i in range(2, 2294):
    #     values_dict = {}
    #     # Наименование организации полное Краткое наименование    ИНН     КПП     ОГРН    Адрес
    #     for j in range(1, 7):
    #         # Print the cell values with tab space
    #         values_dict[j] = worksheet.cell(row=i, column=j).value
    #         # print(worksheet.cell(row=i, column=j).value, end="\t")
    #     # print(values_dict)
    #     inst = Organization(
    #         full_name=values_dict[1],
    #         short_name=values_dict[2],
    #         inn=values_dict[3],
    #         kpp=values_dict[4],
    #         ogrn=values_dict[5],
    #         address=values_dict[6],
    #     )
    #     instances.append(inst)
    #     # print("")
    # Organization.objects.bulk_create(instances)
    # sprs = Sportsman.objects.all()
    # tst_templates = TestTemplate.objects.all()
    # print(Sprs, Sprs.count())
    # print(tst_templates, tst_templates.count())
    # for s in tqdm(sprs):
    #     for template in tst_templates:
    #         result_test, _ = ResultTest.objects.get_or_create(
    #             test_template=template,
    #             user=s,
    #         )
    #         result_score = 0
    #         for q in template.questions.all():
    #             result_q, result_q_created = (
    #                 ResultQuestion.objects.get_or_create(
    #                     result_test=result_test,
    #                     question=q,
    #                 )
    #             )
    #             if result_q.answers.all().first().answers.all().first().is_win:
    #                 result_score = result_score + 1
    #             # if result_q_created:
    #             #     result_a, _ = ResultAnswer.objects.get_or_create(
    #             #         result_question=result_q,
    #             #     )
    #             #     result_a.answers.add(q.answers.order_by("?")[0])

    #         result_test.result_score = result_score
    #         result_test.save()
    # SportTypeServices.clear()
    # SportTypeServices.create_sport_types()
    # print(np_models.A001.objects.all())
    # for s in SportType.objects.all():
    #     print(s.code_id, s.public_id, s.is_discipline)
    # print(ExaminationSelectors.get_all())
    # t = TestTemplateSelectors.all().get(slug="test2")
    # yes = [1, 2, 4, 8, 9, 13, 14, 16, 17]
    # # no = [2, 5, 6, 9, 11, 13, 17]
    # for q in t.questions.all():
    #     print(q.text)
    #     if q.answers.count() == 0:
    #         if q.number in yes:
    #             Answer.objects.create(
    #                 question=q, number=1, text="Да", is_win=True
    #             )
    #             Answer.objects.create(
    #                 question=q, number=1, text="Нет", is_win=False
    #             )
    #         else:
    #             Answer.objects.create(
    #                 question=q, number=1, text="Да", is_win=False
    #             )
    #             Answer.objects.create(
    #                 question=q, number=1, text="Нет", is_win=True
    #             )
    #     else:
    #         print(f"count {q.answers.count()}")
