def count_unique_tuples(data: list[dict[str, str | None]]) -> None:
    seen = set()
    for d in data:
        title = d["title"]
        user_id = d["user_id"]
        element = title, user_id
        print(f"Current element: {element}")
        if element not in seen:
            print(f"{element} is not present, adding...")
            seen.add(element)
        else:
            print(f"Current element {element} is present in 'seen', skipping...")

    unique_counter = len(seen)
    print(f"Frequency of unique results: {(unique_counter / len(data) * 100)} %")


if __name__ == "__main__":
    events = [
        {"title": "search", "user_id": None},
        {"title": "main", "user_id": 123},
        {"title": "success", "user_id": 456},
        {"title": "search", "user_id": None},
    ]
    count_unique_tuples(events)
