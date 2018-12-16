# Prerequisites
1. Install Docker
2. Install docker-compose
3. `pip install -r backend/requierements.txt` (after activate virtualenv)

# Databases
1. From `./deployments` directory run: `docker-compose up`.
Create three databases - default (for django middleware), sc_db (selection commitee), hrd_db (HR department)
2. From `./backend` directory run:

- `python manage.py migrate  --database=default`
- `python manage.py makemigrations  selection_commitee`
- `python manage.py migrate selection_commitee —database=sc_db`
- `python manage.py makemigrations  human_resources_dep`
- `python manage.py migrate human_resources_dep —database=hrd_db`

# Test
Scripts: `backend/selection_commitee/management/commands/`
1. Fill the database with test data: `python manage.py filltestdata`
2. Show abiturients with a flag enlisted = True: `python manage.py enlistedlist`
3. Transfer to hr department: `python manage.py transfertohdr --id <id>`

In addition, you can use the sites of the administrator: `localhost:8000/sc_admin/` and `localhost:8000/hdr_admin/`
