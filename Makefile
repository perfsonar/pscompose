
ifdef PSCOMPOSE_SETTINGS
TEST_CONFIG := $(PSCOMPOSE_SETTINGS)
else
TEST_CONFIG := ./SAMPLE_CONFIG.yml
endif

.PHONY: run-api
run-api:
	uvicorn pscompose.api.api:app --reload --host 0.0.0.0 --port 8000 --root-path /api

.PHONY: docker-build
docker-build:
	@echo "Building docker image..."
	$(eval HASH := $(shell docker build -q .))
	@echo $(HASH)

.PHONY: docker
docker: docker-build
	docker run -p "8080:80" -it $(HASH)

.PHONY: css-watch
css-watch:
	@echo "Starting tailwind via npm to watch for CSS changes..."
	cd pscompose/frontend && npm run css-watch

.PHONY: run-frontend
run-frontend:
	@echo "Starting simple HTTP server on http://localhost:5001/"
	cd pscompose/frontend && python3 server.py --port=5001

.PHONY: test
test:
	@echo "Running pytest test harness for Frontend (playwright/pytest) and Backend (standard pytest) tests..."
	source venv/bin/activate && pip install -r dev_requirements.txt
	playwright install
	source venv/bin/activate && PSCOMPOSE_SETTINGS=$(TEST_CONFIG) python3 -m pytest -v -s tests/*.py
