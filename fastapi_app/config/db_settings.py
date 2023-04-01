from DB import Neo4jSession


def get_session():
    with Neo4jSession() as session:
        yield session
