## Här skriver vi vad som gjorts under dagen.

```md
### Datum - Rubrik

#### Medverkande:

#### Beskrivning:

#### Information: - vilken fil du jobbat i - var finns ytterligare information - ex mapp/fil

#### Todo: (om det är något särskilt som ska göras härnäst. Antingen att ta vid/granska eller göra för att vara up to date)
```
--- 

### 23/11 - Setup och backlog

#### Medverkande: Lisa, Miranda, Rickard

#### Beskrivning:
- Skapat issues i github projects (backlog)
- satt upp uv enviornment och struktur, installerat dependencies
- Lagt in git_commands (git regler för projektet)
- lagt till mappen dockerfiles och .dockerignore
- lagt in Nvidia-modellen i model.py i backend/src/backend

#### Information: 
- README 
- .dockerignore
- model.py

#### Todo:
1. skapa eget brach
2. Kör kommandon:
```bash
git pull origin main
uv sync --all-packages
```
3. skapa en .env fil med strukturen: 
```
NVIDIA_API_KEY=
LOGFIRE_TOKEN=
FIRECRAWL_API_KEY=
```

### 24/11 - Scraping, Structure and LanceDB

#### Medverkande: Miranda, Lisa, Rickard 

#### Beskrivning:
- kollat skatteverket.se/robots.txt
- Skapade data_models.py 
    - LanceModel för vector embedding
    - Basemodel för svar från RAG, samt prompt 
- Satte upp vektordatabas i LanceDB (#16)
- Skapade constants.py
    - DATA_PATH och VECTOR_DB_PATH
- Skapade ingestion.py
    - setup_vector_db: skapar tabellen "paragraphs" enligt Paragraph
    - ingest_paragraphs: lägger in paragrafer i tabellen

##### Scraping:
- Testade crawl först men valde att scrapa hela sidan för att sedan plocka ut kapitel 12
- Se backend/src/scrape/scrape_skatteverket.ipynb
- Datan sparades ned i backend/src/scrape/data/raw

#### Information: - vilken fil du jobbat i - var finns ytterligare information - ex mapp/fil

- Se issue 09 i backlog för ytterligare information om does and don't s 
- Skapade data_models.py i backend/src/backend 
- backend/src/scrape/data/raw
- backend/src/scrape/scrape_skatteverket.ipynb
- Vi har testat ingestion.py med test-paragrafer 

### 26/11 - embed_text i Paragraph

#### Medverkande: Alex

#### Beskrivning:
- Lagt till fältet `embed_text` i `Paragraph` (data_models.py)
- Flyttat `SourceField()` från `content` till `embed_text`. Nu är det `embed_text` som blir vektor, inte bara `content`
- `embed_text` = rubrik + paragrafnummer + paragraftext, t.ex. "Maximibelopp och normalbelopp\n11 § Maximibeloppet är..."
- `content` är kvar som ren paragraftext, den visar vi för användaren
- Uppdaterat testparagraferna i ingestion.py (1 § och 26 §) med `embed_text`
- Testat ingestion.py, 26 § kommer som bästa träff på "får jag dra av resor till jobbet?"

#### Information:
- backend/src/backend/data_models.py
- backend/src/ingestion.py
- Varför: många paragrafer säger inte själva vad de handlar om (ex. 12 kap. 11 §). Ämnet står i rubriken, och den var inte med i vektorn innan


#### ToDo: 
- Den som skriver parsern för kap12.md måste fylla i `embed_text` för varje paragraf: f"{title}\n{paragraph_nr} § {content}"
- Alla rader måste ha `embed_text`, annars kraschar table.add() (fältet får inte vara tomt)
- Nästa steg: parser som gör om kap12.md till paragrafer
