from typing import ClassVar
from pydantic import EmailStr
import pandas as pd
from neontology import BaseNode, BaseRelationship, init_neontology, auto_constrain
from datetime import datetime


# We define nodes by inheriting from BaseNode
class UserNode(BaseNode):
    __primarylabel__: ClassVar[str] = "User"
    __primaryproperty__: ClassVar[str] = "email"
    
    email : EmailStr
    password: str
    fullname: str



def find_user_with_email(driver, email):
    user = driver.run(
        """MATCH (a:User {email: $email}) 
        RETURN a
        """,
        email=email,  routing_=RoutingControl.READ
    )
    print(user)
    return user



