from langchain_database import create_langchain_database


def main() -> None:
    database = create_langchain_database()

    print("Available tables:")
    print(database.get_usable_table_names())

    print("\nTable information:")
    print(database.get_table_info())

    print("\nTest query:")
    result = database.run(
        """
        SELECT EMP_ID, EMP_NAME, DEPARTMENT
        FROM EMPLOYEE
        ORDER BY EMP_ID
        """
    )
    print(result)


if __name__ == "__main__":
    main()