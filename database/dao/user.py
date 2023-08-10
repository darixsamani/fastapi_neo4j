from neo4j import RoutingControl

def find_user_with_email(driver, email):
    user  = driver.run(
        """MATCH (a:User {email: $email}) 
        RETURN a
        """,
        email=email,  routing_=RoutingControl.READ
    )
    print(user)
    return user