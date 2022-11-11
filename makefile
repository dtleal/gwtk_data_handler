export_requirements:
	poetry export -f requirements.txt > requirements.txt --without-hashes

clean_pycache:
	find . -type d -name __pycache__ -exec rm -r {} \+

style:
	poetry run isort src/ tests/
	poetry run black src/ tests/
	poetry run flake8 src/ tests/
	poetry run flake8 *.md Makefile --select=W291
	poetry run mypy src/ tests/ --install-types --non-interactive --show-error-codes
	poetry run pylint src/ tests/

db_up:
	docker-compose up --build --force-recreate -d

run:
	export HOST="localhost" && \
	export PORT="5435" && \
	export DATABASE="postgres" && \
	export USER="postgres" && \
	export PASSWORD="postgres" && \
	poetry run gunicorn -w 2 -k uvicorn.workers.UvicornWorker --timeout 120 --chdir src main:app

debug:
	poetry run uvicorn --host 127.0.0.1 --port 8000 --reload --log-level debug --app-dir src main:app
