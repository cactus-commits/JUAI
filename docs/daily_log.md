## Här skriver vi vad som gjorts under dagen.

```md
### Datum - Rubrik

#### Medverkande:

#### Beskrivning:

#### Information: - vilken fil du jobbat i - var finns ytterligare information - ex mapp/fil
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