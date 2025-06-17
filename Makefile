install:
	python -m venv venv && . venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && python main.py

init_DB:
	flask db init && flask db migrate -m "Initial migration" && flask db upgrade