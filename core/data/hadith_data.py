BUKHARI = {
    "name": "bukhari",
    "collection": [
        {
            "lang": "en",
            "title": "Sahih al-Bukhari"
        },
        {
            "lang": "ar",
            "title": "صحيح البخاري"
        }
    ],
    "total_Hadith": 7291
}

MUSLIM = {
    "name": "muslim",
    "collection": [
        {
            "lang": "en",
            "title": "Sahih Muslim"
        },
        {
            "lang": "ar",
            "title": "صحيح مسلم"
        }
    ],
    "totalHadith": 7470
}

NASAI = {
    "name": "nasai",
    "collection": [
        {
            "lang": "en",
            "title": "Sunan an-Nasa'i"
        },
        {
            "lang": "ar",
            "title": "سنن النسائي"
        }
    ],
    "totalHadith": 5766
}

ABUDAWUD = {
    "name": "abudawud",
    "collection": [
        {
            "lang": "en",
            "title": "Sunan Abi Dawud"
        },
        {
            "lang": "ar",
            "title": "سنن أبي داود"
        }
    ],
    "totalHadith": 5276
}

TIRMIDHI = {
    "name": "tirmidhi",
    "collection": [
        {
            "lang": "en",
            "title": "Jami` at-Tirmidhi"
        },
        {
            "lang": "ar",
            "title": "جامع الترمذي "
        }
    ],
    "totalHadith": 3956
}

IBNMAJAH = {
    "name": "ibnmajah",
    "collection": [
        {
            "lang": "en",
            "title": "Sunan Ibn Majah"
        },
        {
            "lang": "ar",
            "title": "سنن ابن ماجه"
        }
    ],
    "totalHadith": 4341
}

list_author = [BUKHARI, MUSLIM, NASAI, ABUDAWUD, TIRMIDHI, IBNMAJAH]


def get_collections() -> dict:
    data = {
        "data": []
    }

    for author in list_author:
        data['data'].append(author)

    return data


def get_collection_by_name(name: str):
    if name == "bukhari":
        return BUKHARI
    elif name == "muslim":
        return MUSLIM
    elif name == "nasai":
        return NASAI
    elif name == "abudawud":
        return ABUDAWUD
    elif name == "tirmidhi":
        return TIRMIDHI
    elif name == "ibnmajah":
        return IBNMAJAH
    else:
        return {
            "error": "no collection found by this name "
        }
