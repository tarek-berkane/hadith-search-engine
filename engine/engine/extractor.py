
# todo validate data is very primitive
def is_data_valid(data: dict) -> bool:
    if n := data.get('hits'):
        if n := n.get('hits'):
            return True
    return False



def get_result_item(item: dict):
    # todo add support for all fields
    return {
        "id": item["_id"],
        "maten": item["_source"]["maten-raw"],
        "saned": item["_source"]["saned-raw"],
        # "chapiter": item[],
        # "chapiter_number": item[],
        # "section": item[],
        # "section_number": item[],

    }


def result_extractor(data: dict):
    result = {
        'total': 0,
        'result': [],
    }

    if not is_data_valid(data):
        return result

    result["total"] = data['hits']['total']['value']

    items = data['hits']['hits']
    result["result"] = [get_result_item(item) for item in items]

    return result
