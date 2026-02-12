def merge_observations(list1, list2):

    merged = []
    seen = {}

    for obs in list1 + list2:
        key = (obs.get("area","").lower(), obs.get("issue","").lower())

        if key not in seen:
            seen[key] = obs
        else:
            # Merge evidence if duplicate
            seen[key]["evidence"] += " | " + obs.get("evidence","")

    merged = list(seen.values())
    return merged
