# Snowflake LangChain Governance Assistant

This project demonstrates how to build an enterprise-style data governance chatbot using Snowflake, LangChain, OpenAI, and Streamlit.

The application allows users to ask natural-language questions about Snowflake governance metadata, including:

* Governed databases, schemas, tables, and columns
* Data classifications such as PII, confidential, restricted, and financial data
* Masking policy mappings
* Role hierarchy and inherited access
* Direct object grants and privileges
* Sensitive columns without active masking protection

The solution uses LangChain’s SQL agent to inspect the permitted metadata tables, generate read-only SQL queries, execute them in Snowflake, and convert the results into clear business-friendly answers.

## Architecture

```text
Streamlit Chat Interface
        ↓
LangChain SQL Agent
        ↓
OpenAI Language Model
        ↓
Snowflake Governance Metadata
```

## Main Components

* `langchain_database.py` – Creates the Snowflake SQLAlchemy and LangChain database connection.
* `sql_agent.py` – Builds the governance-aware LangChain SQL agent and defines security rules.
* `chat.py` – Provides a command-line chatbot interface.
* `streamlit_app.py` – Provides an interactive web-based chat interface.
* Governance metadata tables:

  * `DATA_ASSET`
  * `DATA_CLASSIFICATION`
  * `MASKING_POLICY_MAPPING`
  * `ROLE_HIERARCHY`
  * `OBJECT_GRANT`

The metadata repository can be populated from Snowflake `ACCOUNT_USAGE` views, including object metadata, tags, masking-policy references, grants, and role relationships.
Snowflake_Scripts.sql contains the required SQL scripts.

## Security

The chatbot is designed for read-only governance analysis:

* The agent is instructed to generate `SELECT` statements only.
* Snowflake RBAC restricts the application role to approved metadata objects.
* Credentials and API keys are stored outside the source code using environment variables.
* The `.env` file should never be committed to GitHub.

## Example Questions

* Which columns are classified as PII?
* Which restricted columns do not have an active masking policy?
* Which roles have direct `SELECT` access to the `EMPLOYEE` table?
* Does `AI_ADMIN_ROLE` inherit privileges from `AI_CHATBOT_ROLE`?
* Which masking policy protects the salary column?

This project is intended as a practical portfolio example of integrating Snowflake governance, metadata management, role-based access control, natural-language SQL, and generative AI.

