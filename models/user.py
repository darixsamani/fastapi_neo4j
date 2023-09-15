from typing import ClassVar
from pydantic import EmailStr, Field
from uuid import uuid4, UUID
import pandas as pd
from neontology import BaseNode, BaseRelationship, init_neontology, auto_constrain
from datetime import datetime


# We define nodes by inheriting from BaseNode
class UserNode(BaseNode):
    __primarylabel__: ClassVar[str] = "User"
    __primaryproperty__: ClassVar[str] = "email"
    
    id: UUID = Field(default_factory=uuid4)
    email : EmailStr
    password: str
    fullname: str





