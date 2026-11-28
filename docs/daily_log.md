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

---


### 25/11 - Test for chunking in paragraphs 

#### Medverkande: Miranda 

#### Beskrivning: 
- Delade upp markdown-filen kap12.md paragraf för paragraf 
- testade embedding model och lancemodel för att testa vector embedding på datan 
- göra rader av paragraferna för och dela upp dem (splitta vid ny paragraf)
- testade med lancedb connection 
- skapade table 
- adderade raderna
- testade att söka i vector databasen

#### Information: - vilken fil du jobbat i - var finns ytterligare information - ex mapp/fil
- i chunk_test.ipynb 

#### Todo: (om det är något särskilt som ska göras härnäst. Antingen att ta vid/granska eller göra för att vara up to date)

- uppdatera chunking i ingestion.py och paragraph(lancemodel), Ragresponse i models.py 

--- 


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

### 26/11 - Uppdaterat RagResponse

#### Medverkande: Alex

#### Beskrivning:
- Lagt till `abstained: bool` i `RagResponse`, så att systemet kan säga att svaret inte finns i lagtexten
- Skrivit om descriptions (engelska):
    - "retrieved file" → "retrieved paragraphs", eftersom datan ligger i LanceDB och inte i filer
    - `answer` ska vara på svenska och bara bygga på de hämtade paragraferna
    - `paragraph_nr` har exempel på format ('26', '6 a') och måste vara en av de hämtade paragraferna
- Kommenterat bort `law_nr`, eftersom det alltid är samma lag 
-  Kommenterat bort `filename` och `filepath`. Hos oss är källan en paragraf, inte en egen fil, så `paragraph_nr` och `title` räcker

#### Information:
- backend/src/backend/data_models.py

#### ToDo: 
- Den som skriver parsern för kap12.md måste fylla i `embed_text` för varje paragraf: f"{title}\n{paragraph_nr} § {content}"
- Alla rader måste ha `embed_text`, annars kraschar table.add() (fältet får inte vara tomt)
- Nästa steg: parser som gör om kap12.md till paragrafer


### 26 / 11 - Setup agent, fastapi och connection till logfire och lancedb 

#### Medverkande: Miranda 

#### Beskrivning:
**api.py**
- Setup FastAPI 
- Initialize logfire till pydantic_ai och fastapi(app)
- Skapat endpoint för fråga i fastapi 
- testat den i Swagger ui 

**rag.py**
- setup agent med nvidia_model 
- connection till lancedb 
- system_prompt - nu är den hårdkodad (V1)
- skapa agenten för rag med output baserat på ragresponse - modellen för struktur 

#### Information: - vilken fil du jobbat i - var finns ytterligare information - ex mapp/fil
- rag.py (agenten och system-prompt)
- Swagger UI:
    -  i backend/src/backend 
    - kör kommando:
        ```bash
         uv run uvicorn api:app --reload
        ```
#### Todo: (om det är något särskilt som ska göras härnäst. Antingen att ta vid/granska eller göra för att vara up to date)

- system_prompt 
    - testa olika prompts i logfire 
    - hämta dem på rätt sätt och inte hårdkodat som nu 
    - gör detta med hjälp av lable e.g. latest

- Testa agenten mot databasen
    - när databasen är uppsatt i lancedb testa agenten mot denna 

- tool 
    - om vi vill ha någon tool för agenten ska denna ligga i rag.py 

---

### 26/11 - Parsing/chunking

#### Medverkande: Lisa

#### Beskrivning: 
- skapat parsing.py:
    - i backend som chunkar upp och parsar markdown filen med kap 12
    - delar upp texten så att varje rubrik hamnar ovanför paragrafen
- ändrat i data_models.py och ingestion.py
    - tog bort title, ebmed_text (ger samma som content)
    - lade till och ändrade i ingestion så att vi får med det chunkade texten


#### Information: 
- data_models.py
- ingestions.py
- pasring.py

#### Todo:
- göra en tool för rag så att den kan hitta databasen


### 26 / 11 - agent tool plain 

#### Medverkande: Miranda
#### Beskrivning: 
- tog bort   abstained: bool = Field i data_models då det inte fungerade 
- skapade ett tool_plain för agenten (detta behövs för att kunna få ett svar då agenten måste veta när den ska användas)
- skrev ut svaret utan embeddings 
- satte default om ingen paragraph hittas 
- testade i swagger UI 

#### Information: 
- rag.py 
- data_models.py 

#### Todo:
- se över svaret i tool om det är bra nog 

```bash
uv run ingestion.py # behövs för att få in data i lancedb 
```

---

### 28/11 - Parsing/chunking, Streamlit

#### Medverkande: Rickard

#### Beskrivning:
- Ändrat chunk_chapter i parsing.py
    - Rubriken '####' hamnade sist i föregående paragraf, t.ex stod "#### Arbetsresor"
    - Nu sparas senaste rubriken och läggs överst i rätt paragraf: "12 kap. Arbetsresor\n**26 §** ..."
    - chunk_id byggs från paragrafnumret i stället för en räknare. Förut var t.ex. 26 § il_12_28, nu är den il_12_26 (6 a § blir il_12_6a)
    - De två versionerna av 6 a § (upphör/träder i kraft 2027-01-01) får olika id: ` och il_12_6a_ny
    - Kört ingestion.py igen så databasen har de rättade chunkarna

- Ändrade description av title i RagResponse (data_models.py)
    - För att säkerställa att modellen kopierar rubriken från första raden i den hämtade paragrafen ("12 kap. <rubrik>") i stället för att hitta på en egen 

- rag.py
    - Lagt till i system_prompt: "Återge belopp, procentsatser och enheter exakt som i lagtexten, räkna aldrig om dem."
    - Tagit bort ur system_prompt: "Avsluta alltid med att ange vilka paragrafer du har använt som källa..." eftersom källan då kom med två gånger, en gång i svaret och en gång under rubriken Källa i frontenden

- app.py (frontend)
    - Chattgränssnitt i Streamlit med st.chat_input och historik i st.session_state (#26)
        - Mall: lektion 05 (JokeBot) för chatten, RAGbit (https://github.com/kokchun/ragbit) för anropet till backend
        - Varje svar visar källa längst ner: paragraf + rubrik
    - Visar felmeddelande om backend inte svarar med 200
    - Lagt till requests i frontend/pyproject.toml (behövs för Docker senare)


#### Information:
- backend/src/backend/parsing.py
- backend/src/backend/data_models.py
- backend/src/backend/rag.py
- frontend/src/frontend/app.py
- Varför parsing: rubriken säger ofta vad paragrafen handlar om (ex. 26 § "Arbetsresor"). Med rubriken i fel chunk hittade sökningen fel paragraf först
- Varför system_prompt: frågan "Får jag dra av resor till jobbet?" gav "2,50 kronor per mil", men 27 § säger "2 kronor och 50 öre för varje kilometer". Det blir tio gånger fel

#### Todo:
- Felhantering, timeouts och rate limiting i api.py (#23)
- Frontend behöver requests: kör uv sync --all-packages