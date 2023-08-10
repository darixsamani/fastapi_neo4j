from typing import ClassVar
from pydantic import EmailStr
import pandas as pd
from neontology import BaseNode, BaseRelationship, init_neontology, auto_constrain
from datetime import datetime
from .user import UserNode
from typing import List



class PosteNode(BaseNode):
    __primarylabel__: ClassVar[str] = "Poste"
    __primaryproperty__: ClassVar[str] = "name"
    
    title: str
    content: str
    date_created : datetime = datetime.now()
    date_updated : datetime
    tags : List[str]



class Posted(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "POSTED"
    
    source: UserNode
    target: PosteNode