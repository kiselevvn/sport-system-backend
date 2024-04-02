import os

import xlrd
from django.conf import settings

from backend.apps.competitions.models import SportCategory, SportDiscipline


class SportTypeServices:

    @classmethod
    def get_file_path(cls):
        return os.path.join(settings.FIXTURES_DIR, "VRVS_441b8cea69.xls")

    @classmethod
    def create_sport_types(cls):
        workbook = xlrd.open_workbook(cls.get_file_path())
        sheet = workbook.sheet_by_index(1)
        data = []
        prev_obj = None
        for row in range(7, 5416):
            row_data = []
            for col in range(0, 17):
                try:
                    if sheet.cell_value(rowx=row, colx=col) == "":
                        cell_value = sheet.cell_value(rowx=row, colx=col)
                    elif col in (2, 3, 10, 11):
                        cell_value = str(
                            int(sheet.cell_value(rowx=row, colx=col))
                        ).zfill(3)
                    elif col in (1, 9, 16, 8):
                        cell_value = str(sheet.cell_value(rowx=row, colx=col))
                    else:
                        cell_value = str(
                            int(sheet.cell_value(rowx=row, colx=col))
                        )
                    # print(sheet.cell(row, col).value)
                except TypeError as error:
                    cell_value = ""
                except IndexError as error:
                    cell_value = ""
                row_data.append(cell_value)
            data.append(row_data)

            if row_data[0] != "":
                obj_c, created_d = SportCategory.objects.get_or_create(
                    name=row_data[1],
                    code_id=f"{row_data[2]}{row_data[3]}{row_data[4]}{row_data[5]}{row_data[6]}{row_data[7]}{row_data[8]}",
                )
            else:
                obc_c = prev_obj.sport_category
            obj_d, created_d = SportDiscipline.objects.get_or_create(
                name=row_data[9],
                code_id=f"{row_data[10]}{row_data[11]}{row_data[12]}{row_data[13]}{row_data[14]}{row_data[15]}{row_data[16]}",
                sport_category=obj_c,
            )
            prev_obj = obj_d

    @classmethod
    def clear(cls):
        SportCategory.objects.all().delete()
        SportDiscipline.objects.all().delete()
