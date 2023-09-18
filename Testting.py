import re


def user():
    value = input("Search: ")
    return value


def database():
    data = ["banana", "apple", "orange", "pineapple", "watermelon"]
    return data


def search():
    search_term = user().lower()
    data = database()
    results = {}

    for item in data:
        count = 0

        # Exact match check
        if item.lower() == search_term:
            results[item] = float(
                "inf"
            )  # Assigning a high count to prioritize exact matches
            continue

        # Counting occurrences of search term within the item
        count += item.lower().count(search_term)

        # Regular expression matching for more advanced patterns
        pattern = r"\b{}\b".format(search_term)
        count += len(re.findall(pattern, item.lower()))

        results[item] = count

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    max_count = sorted_results[0][1] if sorted_results else 0

    threshold = max(max_count - 2, 1)  # Adjust the threshold as desired

    closest_matches = []
    exact_matches = []

    for item, count in sorted_results:
        if count >= threshold:
            if count == float("inf"):
                exact_matches.append(item)
            else:
                closest_matches.append(item)
        else:
            break

    return closest_matches, exact_matches


closest, exact = search()

print("Exact Matches:", exact)
print("Closest Matches:", closest)
