from django.db import models
from django.utils.translation import gettext as _


class SportType(models.Model):
    """
    Вид спорта
    """

    code_id = models.CharField(
        verbose_name=_("Код"),
        max_length=25,
    )
    name = models.CharField(
        verbose_name=_("Наименование"),
        max_length=250,
    )
    is_actual = models.BooleanField(_("Является актуальным"), default=False)

    GROUPS = {
        "А": "мужчины, юноши (юниоры)",
        "Б": "женщины, девушки (юниорки)",
        "Г": "мужчины, юноши (юниоры), женщины",
        "Д": "девушки (юниорки)",
        "Е": "мужчины, девушки (юниорки)",
        "Ж": "женщины",
        "К": "мужчины, женщины, девушки (юниорки)",
        "Л": "мужчины, женщины",
        "М": "мужчины",
        "Н": "юноши (юниоры), девушки (юниорки)",
        "С": "юноши (юниоры), девушки (юниорки), женщины",
        "Ф": "мужчины, юноши (юниоры), девушки (юниорки)",
        "Э": "юноши (юниоры), женщины.",
        "Ю": "юноши (юниоры)",
        "Я": "все категории",
    }
    SEASON = {
        False: {
            "1": "летний неигровой вид спорта",
            "2": "летний игровой вид спорта",
            "3": "зимний неигровой вид спорта",
            "4": "зимний игровой вид спорта",
            "5": "внесезонный, неигровой вид спорта",
            "6": "внесезонный, игровой вид спорта",
            "7": "внесезонный вид спорта, содержащий как игровые,"
            + " так и неигровые спортивные дисциплины",
            "8": "летний вид спорта, содержащий как игровые,"
            + " так и неигровые спортивные дисциплины",
            "9": "зимний вид спорта, содержащий как игровые,"
            + " так и неигровые спортивные дисциплины",
        },
        True: {
            "1": "летняя неигровая спортивная дисциплина",
            "2": "летняя игровая спортивная дисциплина",
            "3": "зимняя неигровая спортивная дисциплина",
            "4": "зимняя игровая спортивная дисциплина",
        },
    }
    PROPAGATION = {
        False: {
            "1": "военно-прикладной или служебно-прикладной вид спорта,"
            + " развивается в рамках деятельности одного"
            + " или нескольких федеральных органов исполнительной власти",
            "2": "вид спорта развивается в пределах одного из субъектов"
            + " Российской Федерации — национальный вид спорта",
            "3": "вид спорта развивается спортивными федерациями, получил"
            + " развитие только в Российской Федерации",
            "4": "вид спорта развивается международной спортивной федерацией",
            "5": "вид спорта развивается международной спортивной федерацией,"
            + " получил признание Международного олимпийского"
            + " комитета (далее — МОК)",
            "6": "вид спорта развивается международной спортивной федерацией,"
            + " получил признание МОК и включён в программу Олимпийских игр",
            "7": "вид спорта инвалидов и лиц с ограниченными возможностями"
            + " здоровья, развивается международной спортивной федерацией",
        },
        True: {
            "1": "спортивная дисциплина военно-прикладного или"
            + " служебно-прикладного вида спорта",
            "2": "спортивная дисциплина национального вида спорта",
            "6": "спортивная дисциплина вида спорта, указанного"
            + " в подпункте 6.1.6. и включённая в программу Олимпийских игр",
            "7": "спортивная дисциплина вида спорта инвалидов"
            + " и лиц с ограниченными возможностями здоровья",
            "8": "спортивная дисциплина видов спорта, указанных в"
            + " подпунктах 6.1.3. — 6.1.5., а также вида спорта,"
            + " указанного в подпункте 6.1.6. и не включённая"
            + " в программу Олимпийских игр.",
        },
    }
    DEVELOPMENT = {
        "1": "руководство развитием вида спорта федеральными органами"
        + " исполнительно власти не осуществляется",
        "2": "Минобороны России",
        "3": "МЧС России",
        "4": "ФСКН России",
        "5": "ГФС России",
        "6": "Федеральная таможенная служба",
        "9": "ФСО России",
        "Л": "МЧС России, ФСО России",
        "М": "ФСКН России, МВД России",
        "Н": "ФСО России, МВД России, ГУСП",
        "Р": "ФСО России, Федеральная таможенная служба, ГУСП",
        "С": "ФСБ России, ФСО России, МВД России, ГУСП",
        "Ф": "Минюст России, ФССП России, ФСИН России, ФСО России",
        "Э": "ФСКН России, ФССП России, ФСИН России, ФСО России, ГУСП,"
        + " Минюст России, МВД России",
        "Ю": "ФСБ России, ФСКН России, ФССП России, ФСО России,"
        + " Федеральная таможенная служба, МВД России,"
        + " СВР России, ГУСП, ФМС России",
        "Я": "ФСБ России, ФСКН России, Минюст России, ФССП России,"
        + " ФСИН России, ФСО России, ГФС России,"
        + " Федеральная таможенная служба, МВД России, СВР России, ГУСП",
    }
    EXTRA = {
        "1": "не имеется ограничений",
        "2": "имеются ограничения, установленные федеральным"
        + " органом исполнительной власти"
        + " в области физической культуры и спорта",
        "3": "национальный вид спорта Республики Саха (Якутии)",
        "4": "национальный вид спорта Республики Татарстан (Татарстана)",
        "5": "национальный вид спорта Чувашской Республики — Чувашии",
        "6": "национальный вид спорта Республики Тыва",
        "7": "национальный вид спорта Республики Ингушетия",
        "8": "---",
    }

    @property
    def is_discipline(self):
        """
        Вида спорта является дисциплиной
        """
        return self.code_id[3:6] != "000"

    @property
    def discipline_id(self):
        """
        Публичный идентификатор диссциплины
        в рамках вида спорта
        """
        return self.code_id[3:6]

    @property
    def public_id(self):
        """
        Публичный идентификатор вида спорта
        """
        if self.code_id == "" or self.code_id is None:
            return None
        return self.code_id[0:3]

    @property
    def get_seaseon_id(self):
        return self.code_id[6]

    @property
    def get_seaseon_label(self):
        return self.SEASON[self.is_discipline][self.code_id[6]]

    @property
    def get_propagation_id(self):
        return self.code_id[7]

    @property
    def get_propagation_label(self):
        return self.PROPAGATION[self.is_discipline][self.code_id[7]]

    @property
    def get_development_label(self):
        return self.DEVELOPMENT[self.code_id[8]]

    @property
    def get_extra_id(self):
        return self.code_id[9]

    @property
    def get_extra_label(self):
        print(self.code_id)
        return self.EXTRA[self.code_id[9]]

    @property
    def get_group_id(self):
        return self.code_id[10]

    @property
    def get_group_label(self):
        return self.GROUPS[self.code_id[10]]

    list_fields = [
        "id",
        "name",
        "is_actual",
        "code_id",
        "is_discipline",
        "discipline_id",
        "public_id",
        "get_seaseon_id",
        "get_seaseon_label",
        "get_propagation_id",
        "get_propagation_label",
        "get_development_label",
        "get_extra_id",
        "get_extra_label",
        "get_group_id",
        "get_group_label",
    ]

    class Meta:
        verbose_name = _("Вид спорта")
        verbose_name_plural = _("Виды спорта")
