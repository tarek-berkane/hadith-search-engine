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


class Extractor:
    """Extract data from json """

    def simple_result_extract(self, data: dict) -> dict:
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

    # def extract_hadith_item(self, item: dict):
    #     # todo add support for all fields
    #     return {
    #         "id": item["_id"],
    #         "chapter_number": item["_source"]["chapter_number"],
    #         "chapter_arabic": item["_source"]["chapter_arabic"],
    #         "section_number": item["_source"]["section_number"],
    #         "section_arabic": item["_source"]["section_arabic"],
    #         "arabic_hadith": item["_source"]["arabic_hadith"],
    #         "arabic_grade": item["_source"]["arabic_grade"],
    #     }

    # data extractor
    def get_search_meta_data(self, data: dict):
        """
        Return search meta data
        describe search state of time lapsed,result item
        that have been searched status about shares of
        elasticsearch and if search done or timed out

        fields : ["took", "timed_out", "_shards", "hits"]
        inner fields:[
            "_shards" = {"total", "successful", "skipped", "failed"},
            "hits" = {"total", "max_score"},
            ]
        """
        result = {
            "took": data["took"],
            "timed_out": data["timed_out"],
            "_shards": data["_shards"].copy(),
            "hits": {
                "total": data["hits"]["total"].copy(),
                "max_score": data["hits"]["max_score"],
            },
        }
        return result

    def get_search_raw_list_hadith(self, data: dict) -> list:
        "Return list of hadith that match the query "
        return data["hits"]['hits']

    def get_hadith_item_meta_data(self, hadith_item: dict):

        result = {
            "_index": hadith_item['_index'],
            "_type": hadith_item["_doc"],
            "_id": hadith_item["_id"],
            "_score": hadith_item["_score"],
        }
        return result

    def extract_collection_data(self, hadith_item: dict):
        result = {
            "coll": hadith_item['_source']['coll'],
        }
        return result

    def extract_section_data(self, hadith_item: dict):
        result = {
            "section_number": hadith_item['_source']["section_number"],
            "section_english": hadith_item['_source']["section_english"],
            "section_arabic": hadith_item['_source']["section_arabic"],
        }
        return result

    def extract_chapter_data(self, hadith_item: dict):
        result = {
            "chapter_number": hadith_item['_source']["chapter_number"],
            "chapter_english": hadith_item['_source']["chapter_english"],
            "chapter_arabic": hadith_item['_source']["chapter_arabic"],
        }
        return result

    def extract_hadith_data(self, hadith_item: dict):
        result = {
            "hadith_number": hadith_item['_source']["hadith_number"],

            "english_hadith": hadith_item['_source']["english_hadith"],
            "english_isnad": hadith_item['_source']["english_isnad"],
            "english_matn": hadith_item['_source']["english_matn"],
            "english_grade": hadith_item['_source']["english_grade"],

            "arabic_hadith": hadith_item['_source']["arabic_hadith"],
            "arabic_isnad": hadith_item['_source']["arabic_isnad"],
            "arabic_matn": hadith_item['_source']["arabic_matn"],
            "arabic_grade": hadith_item['_source']["arabic_grade"],
        }
        return result

    def get_result_from_hadith_list(self, hadith_list: list) -> list:
        result = []

        for hadith_item in hadith_list:
            hadith_item_data = {}

            hadith_item_data.update(
                self.extract_collection_data(hadith_item))

            hadith_item_data.update(
                self.extract_chapter_data(hadith_item)
            )

            hadith_item_data.update(
                self.extract_section_data(hadith_item)
            )

            hadith_item_data.update(
                self.extract_hadith_data(hadith_item)
            )

            result.append(hadith_item_data)


        return result

    def extract(self, data):
        hadith_raw_data = self.get_search_raw_list_hadith(data)
        hadith_list_info = self.get_result_from_hadith_list(hadith_raw_data)

        return hadith_list_info