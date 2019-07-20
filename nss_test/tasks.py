from datamodel.models import Datamodel
import openpyxl

from celery import shared_task


@shared_task
def upload_data(excel_file):

    # validations can be placed here to check file extension

    wb = openpyxl.load_workbook(excel_file)

    # getting a particular sheet by name out of many sheets

    worksheet = wb["Sheet1"]
    print(worksheet)
    excel_data = list()
    # iterating over the rows and
    # getting value from each cell in row

    for row in worksheet.iter_rows():
        row_data = list()
        Datamodel.objects.create(firstname=row[A1], lastname=row[A2])
        for cell in row:
            row_data.append(str(cell.value))
            excel_data.append(row_data)
