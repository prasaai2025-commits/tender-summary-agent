def validate_summary(data):
    for key, val in data.items():
        if not val:
            data[key] = {}
    return data
