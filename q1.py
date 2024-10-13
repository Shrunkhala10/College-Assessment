def suggest_completions(search_history, query):

    suggestions = [item for item in search_history if item.startswith(query.lower())]
    return suggestions

search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]


query = input("Enter your partial search query: ")

suggestions = suggest_completions(search_history, query)
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")
