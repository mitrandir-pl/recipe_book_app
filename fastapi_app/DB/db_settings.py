from DB.neo4j_db_handler import Neo4jSession


async def get_session():
    async with Neo4jSession() as session:
        yield session
