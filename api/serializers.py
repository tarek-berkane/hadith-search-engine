from rest_framework import serializers

import core.data.fields  as fd


#
# class SearchSerializer(serializers.Serializer):
#     query = serializers.CharField(max_length=100)
#
#
# class BaseHadith(serializers.Serializer):
#     coll_id: int = serializers.IntegerField(required=False, default=None)
#     coll: str = serializers.CharField(required=False, default=None)
#     chapter_number: int = serializers.IntegerField(required=False, default=None)
#     section_number: int = serializers.IntegerField(required=False, default=None)
#
#
# class HadithSerializer(serializers.Serializer):
#     hadith_number = serializers.CharField()
#     coll: str = serializers.CharField(required=False, default=None)
#     coll_id: int = serializers.IntegerField(required=False, default=None)
#
#     def get(self, key: str):
#         return self.data[key]
#
#
# class HadithListSerializer(serializers.Serializer):
#     chapter_number: int = serializers.IntegerField(required=False, default=None)
#     section_number: int = serializers.IntegerField(required=False, default=None)
#     coll: str = serializers.CharField(required=False, default=None)
#     coll_id: int = serializers.IntegerField(required=False, default=None)
#

class BaseHadithSerializer(serializers.Serializer):
    collection_name = serializers.CharField(required=False, default=None)
    section_number = serializers.CharField(required=False, default=None)
    chapter_number = serializers.CharField(required=False, default=None)

    def get_data(self):
        query_data = {}

        query_data[fd.COLLECTION] = self.data.get('collection_name')
        query_data[fd.SECTION_NUMBER] = self.data.get('section_number')
        query_data[fd.CHAPTER_NUMBER] = self.data.get('chapter_number')
        return query_data

    def help(self):
        help_data = {
            "fields": [
                {"collection_name": "[required=False, default=None]"},
                {"section_number": "[required=False, default=None]"},
                {"chapter_number": "[required=False, default=None]"},
            ],
        }
        return help_data


class IdHadithSerializer(BaseHadithSerializer):
    hadith_number = serializers.IntegerField(required=True)

    def get_data(self):
        query_data = super().get_data()

        query_data[fd.HADITH_NUMBER] = self.data.get('hadith_number')
        return query_data

    def help(self):
        help_data = super().help()

        extra_field = {"hadith_number": "[required=True]"}
        help_data['fields'].insert(0, extra_field)
        return help_data


class TextQuerySerializer(BaseHadithSerializer):
    query = serializers.CharField(max_length=255, required=True)

    def get_data(self):
        query_data = super().get_data()

        query_data[fd.QUERY] = self.data.get('query')
        return query_data

    def help(self):
        help_data = super().help()

        extra_field = {"query_data": "max_length=255, required=True"}
        help_data['fields'].insert(0, extra_field)
        return help_data