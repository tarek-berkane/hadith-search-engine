QUERY = "query"
P_QUERY = "processed query"

# "coll": {"type": "text"},
COLLECTION = "coll"

# "matn_p": {"type": "text"},
MATN_P = "matn_p"

# "isnad_p": {"type": "text"},
ISNAD_P = "isnad_p"

# "chapter_number": {"type": "integer"},
CHAPTER_NUMBER = "chapter_number"

# "chapter_english": {"type": "text"},
CHAPTER_ENGLISH = "chapter_english"

# "chapter_arabic": {"type": "text"},
CHAPTER_ARABIC = "chapter_arabic"

# "section_number": {"type": "integer"},
SECTION_NUMBER = "section_number"

# "section_english": {"type": "text"},
SECTION_ENGLISH = "section_english"

# "section_arabic": {"type": "text"},
SECTION_ARABIC = "section_arabic"

# "hadith_number": {"type": "integer"},
HADITH_NUMBER = "hadith_number"

# "english_hadith": {"type": "text", "index": False},
ENGLISH_HADITH = "english_hadith"

# "english_isnad": {"type": "text", "index": False},
ENGLISH_ISNAD = "english_isnad"

# "english_matn": {"type": "text", "index": False},
ENGLISH_MATN = "english_matn"

# "arabic_hadith": {"type": "text", "index": False},
ARABIC_HADITH = "arabic_hadith"

# "arabic_isnad": {"type": "text", "index": False},
ARABIC_ISNAD = "arabic_isnad"

# "arabic_matn": {"type": "text", "index": False},
ARABIC_MATN = "arabic_matn"

# "english_grade": {"type": "text"},
ENGLISH_GRADE = "english_grade"

# "arabic_grade": {"type": "text"},
ARABIC_GRADE = "english_grade"

arabic_fields = [ARABIC_HADITH, ARABIC_ISNAD, ARABIC_MATN, CHAPTER_ARABIC, SECTION_ARABIC, ARABIC_GRADE]
english_fields = [ENGLISH_HADITH, ENGLISH_ISNAD, ENGLISH_MATN, CHAPTER_ENGLISH, SECTION_ENGLISH, ENGLISH_GRADE]
id_fields = [CHAPTER_NUMBER, SECTION_NUMBER, HADITH_NUMBER]

