"""
tech_resolver.py
Convert technology NAMES → technology IDs
"""


def resolve_technology_ids(client, technology_names):
    """
    technology_names: list[str]
    returns: list[str] (MongoDB IDs)
    """
    url = f"{client.base_url}/technology"
    res = client.session.get(url)

    if res.status_code != 200:
        raise Exception("Failed to fetch technologies")

    technologies = res.json()

    name_to_id = {
        tech["technology"].lower(): tech["technologyID"]
        for tech in technologies
    }

    resolved_ids = []

    for name in technology_names:
        key = name.lower()
        if key not in name_to_id:
            raise Exception(f"Technology not found: {name}")
        resolved_ids.append(name_to_id[key])

    return resolved_ids
