def get_item(data: dict):
    return {
        "maten": data["_source"]['maten-raw'],
        "saned": data["_source"]['saned-raw']
    }


def get_result(data: dict):
    if not data['hits']['hits']:
        return {}

    result = [get_item(item) for item in data['hits']['hits']]
    return result