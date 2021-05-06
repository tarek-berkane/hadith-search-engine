def get_item(data: dict):
    return {
        "arabic_hadith": data["_source"]['arabic_hadith'],
        "chapter_number": data["_source"]['chapter_number'],
        "section_arabic": data["_source"]['section_arabic'],
        "hadith_number": data["_source"]['hadith_number'],
        "chapter_arabic": data["_source"]['chapter_arabic'],
        "section_number": data["_source"]['section_number'],
    }


def get_result(data: dict):
    if not data['hits']['hits']:
        return {}

    result = [get_item(item) for item in data['hits']['hits']]
    return result