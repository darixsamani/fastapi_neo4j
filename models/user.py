from typing import ClassVar
from pydantic import EmailStr, Field
from uuid import uuid4
import pandas as pd
from neontology import BaseNode, BaseRelationship, init_neontology, auto_constrain
from datetime import datetime


# We define nodes by inheriting from BaseNode
class UserNode(BaseNode):
    __primarylabel__: ClassVar[str] = "User"
    __primaryproperty__: ClassVar[str] = "email"
    
    id: int = Field(default_factory=lambda: uuid4().hex)    
    email : EmailStr
    password: str
    fullname: str





