import djclick as click

from backend.apps.testing.models import Answer

# from backend.apps.examination.selectors import ExaminationSelectors
from backend.apps.testing.selectors import TestTemplateSelectors

# from backend.apps.examination_templates.models import ExaminationTemplate
# from backend.apps.examination_templates.selectors import (
#     examination_template_selector,
# )


# from backend.apps.examination_templates.services import (
#     generate_scheme_template,
# )


@click.command()
def command():
    # print(ExaminationSelectors.get_all())
    t = TestTemplateSelectors.all().get(slug="test2")
    yes = [1, 2, 4, 8, 9, 13, 14, 16, 17]
    # no = [2, 5, 6, 9, 11, 13, 17]
    for q in t.questions.all():
        print(q.text)
        if q.answers.count() == 0:
            if q.number in yes:
                Answer.objects.create(
                    question=q, number=1, text="Да", is_win=True
                )
                Answer.objects.create(
                    question=q, number=1, text="Нет", is_win=False
                )
            else:
                Answer.objects.create(
                    question=q, number=1, text="Да", is_win=False
                )
                Answer.objects.create(
                    question=q, number=1, text="Нет", is_win=True
                )
        else:
            print(f"count {q.answers.count()}")
