from pydantic import BaseModel, RootModel
from typing import List, Optional



class ImportRecord(BaseModel):
    name: str
    url: str


class ImportRecordBase(RootModel):
    root: Optional[List[ImportRecord]]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]