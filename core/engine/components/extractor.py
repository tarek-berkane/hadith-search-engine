# todo validate data is very primitive
def is_data_valid(data: dict) -> bool:
    if n := data.get('hits'):
        if n := n.get('hits'):
            return True
    return False


def extract_hadith_item(item: dict):
    # todo add support for all fields
    return {
        "id": item["_id"],
        "chapter_number": item["_source"]["chapter_number"],
        "chapter_arabic": item["_source"]["chapter_arabic"],
        "section_number": item["_source"]["section_number"],
        "section_arabic": item["_source"]["section_arabic"],

        "arabic_hadith": item["_source"]["arabic_hadith"],
        "arabic_grade": item["_source"]["arabic_grade"],
        # "saned": item["_source"][""],


    }


def result_extractor(data: dict):
    result = {
        'total': 0,
        'result': [],
    }
    if not data:
        return result

    if not is_data_valid(data):
        return result

    result["total"] = data['hits']['total']['value']

    items = data['hits']['hits']
    # result["result"] = [get_result_item(item) for item in items]

    for item in items:
        result['result'].append(extract_hadith_item(item))

    return result


