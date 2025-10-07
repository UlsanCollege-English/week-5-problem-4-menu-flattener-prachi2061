def flatten_menu(node):
    if node is None:
        return []

    node_type = node.get("type")

    if node_type == "item":
        name = node.get("name")
        return [name] if name is not None else []

    elif node_type == "category":
        items = []
        for child in node.get("children", []):
            items.extend(flatten_menu(child))
        return items

    return []
