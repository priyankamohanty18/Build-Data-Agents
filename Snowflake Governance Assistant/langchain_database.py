import os

from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

load_dotenv()


def create_langchain_database() -> SQLDatabase:
    """Create a restricted SQLAlchemy connection for LangChain."""

    required_variables = [
        "SNOWFLAKE_ACCOUNT",
        "SNOWFLAKE_USER",
        "SNOWFLAKE_PASSWORD",
        "SNOWFLAKE_WAREHOUSE",
        "SNOWFLAKE_DATABASE",
        "SNOWFLAKE_SCHEMA",
        "SNOWFLAKE_ROLE",
    ]

    missing = [
        variable
        for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing:
        raise RuntimeError(
            f"Missing environment variables: {', '.join(missing)}"
        )

    engine = create_engine(
        URL(
            account=os.environ["SNOWFLAKE_ACCOUNT"],
            user=os.environ["SNOWFLAKE_USER"],
            password=os.environ["SNOWFLAKE_PASSWORD"],
            warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
            database=os.environ["SNOWFLAKE_DATABASE"],
            schema=os.environ["SNOWFLAKE_SCHEMA"],
            role=os.environ["SNOWFLAKE_ROLE"],
        ),
        pool_pre_ping=True,
    )

    database = SQLDatabase(
        engine=engine,
        include_tables=[ "data_asset",
        "data_classification",
        "masking_policy_mapping",
        "role_hierarchy",
        "object_grant"],
        sample_rows_in_table_info=3,
    )

    return database