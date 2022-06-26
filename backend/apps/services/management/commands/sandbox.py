import djclick as click

# from backend.apps.examination_templates.models import ExaminationTemplate
# from backend.apps.examination_templates.selectors import (
#     examination_template_selector,
# )


# from backend.apps.examination_templates.services import (
#     generate_scheme_template,
# )


@click.command()
def command():
    pass
    # obj = ExaminationTemplate.objects.first()
    # examination_template_instace = examination_template_selector(obj.pk)
    # result = generate_scheme_template(examination_template_instace)
    # print(result)
