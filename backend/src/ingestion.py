import lancedb
from pathlib import Path
from backend.constants import VECTOR_DB_PATH, DATA_PATH
from backend.data_models import Paragraph
from backend.parsing import chunk_chapter
import time

TABLE_NAME = "paragraphs"

# TEST_PARAGRAPHS = [
#     {
#         "doc_id": "il_12_1",
#         "title": "Huvudregel",
#         "paragraph_nr": "1",
#         "law": "Inkomstskattelag (1999:1229)",
#         "content": "Testtext om kostnader för att få inkomster i tjänst.",
#         "embed_text": "Huvudregel\n1 § Testtext om kostnader för att få inkomster i tjänst.",
#     },
#     {
#         "doc_id": "il_12_26",
#         "title": "Resor mellan bostaden och arbetsplatsen",
#         "paragraph_nr": "26",
#         "law": "Inkomstskattelag (1999:1229)",
#         "content": "Testtext om resor mellan bostaden och arbetsplatsen.",
#         "embed_text": "Resor mellan bostaden och arbetsplatsen\n26 § Testtext om resor mellan bostaden och arbetsplatsen.",
#     },
# ]


def setup_vector_db(path):
    # Öppnar eller skapar databasen och ser till att tabellen finns.
    vector_db = lancedb.connect(uri=path)
    vector_db.create_table(TABLE_NAME, schema=Paragraph, mode="overwrite")
    return vector_db


# Lägger in paragrafer.
def ingest_paragraphs(table) -> None:
    md_text = Path(DATA_PATH, "kap12.md").read_text(encoding="utf-8")
    paragraphs = chunk_chapter(md_text)
    table.add(paragraphs)


if __name__ == "__main__":
    vector_db = setup_vector_db(VECTOR_DB_PATH)
    table = vector_db[TABLE_NAME]
    ingest_paragraphs(table)
    print(vector_db, table)




    # vector_db = setup_vector_db(VECTOR_DB_PATH)
    # table = vector_db[TABLE_NAME]

    # ingest_paragraphs(table, TEST_PARAGRAPHS)

    # print(table.to_pandas()[["doc_id", "paragraph_nr"]])
    # print(
    #     table.search("får jag dra av resor till jobbet?")
    #     .limit(1)
    #     .to_list()[0]["doc_id"]
    # )
