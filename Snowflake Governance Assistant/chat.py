from sql_agent import build_agent


def extract_final_answer(result: dict) -> str:
    """Extract the final text response from a LangChain agent result."""

    messages = result.get("messages", [])

    if not messages:
        return "The agent returned no response."

    final_message = messages[-1]
    content = getattr(final_message, "content", None)

    if isinstance(content, str):
        return content

    return str(content)


def main() -> None:
    agent = build_agent()

    print("Snowflake chatbot is ready.")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            result = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": question,
                        }
                    ]
                }
            )

            answer = extract_final_answer(result)
            print(f"\nAssistant: {answer}\n")

        except Exception as error:
            print(f"\nError: {error}\n")


if __name__ == "__main__":
    main()