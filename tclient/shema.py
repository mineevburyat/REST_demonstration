from pydantic import BaseModel, Field
from typing import List, Dict
# from xmlrpc.client import Boolean, boolean
import datetime
#Повторить json структуру как у IDL Thrift
class resultTask(BaseModel):
    id: str
    status: str
    pushtime: str
    starttime: str
    stoptime: str
    result: float

