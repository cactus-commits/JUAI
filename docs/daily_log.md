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


#### ToDo: 
- Bara kap 12 eller hela lagen? Båda finns som data i markdown 
- I uppgiften står det "en lag" inte ett kap - kolla med Kokchun 
- Se hur vi ska chunka upp i kap/paragrafer för att få ut korrekt format 
- Behöver vi ha separata filer för kap/paragraferna ?
