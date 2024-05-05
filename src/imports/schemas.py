import os

from pydantic import BaseModel, field_validator, RootModel
from typing import List, Optional
import json


class ImportRecord(BaseModel):
    name: str
    url: str


class ImportRecordBase(RootModel):
    root: Optional[List[ImportRecord]]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]

# # Получаем путь к директории, в которой находится скрипт (../src/imports)
# script_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Поднимаемся на два уровня выше (../src)
# project_dir = os.path.dirname(os.path.dirname(script_dir))
#
# # Формируем путь к файлу относительно корня проекта
# file_path = os.path.join(project_dir, "mock", "example.json")
#
# # Загрузка JSON из файла
# with open(file_path, 'r') as file:
#     mocks = json.load(file)
#
# # # Проверка соответствия JSON модели
# # try:
# #     for mock in mocks:
# #         if mock.get('data'):
# #             import_record_base = ImportRecordBase(records_list=mock['data'])
# #             print(mock['data'])
# #             print("JSON соответствует модели ImportRecordBase.")
# # except Exception as e:
# #     print("Ошибка при проверке соответствия JSON модели:", e)
#
#
# import_record_base = ImportRecordBase(records_list=mocks)
# print(mocks)
# print("JSON соответствует модели ImportRecordBase.")

records_list = ImportRecordBase.model_validate([{"name": "name_1", "url": "/1"}, {"name": "name_2", "url": "/2"}, {"name": "name_3", "url": "/3"}, {"name": "name_4", "url": "/4"}, {"name": "name_5", "url": "/5"}, {"name": "name_6", "url": "/6"}])

one_record_list = ImportRecord.model_validate(records_list[0])

print(type(records_list[0]))