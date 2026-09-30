
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
	(cd pscompose/frontend && npm run generate-components-index) && cd pscompose/frontend/root && python3 server.py --port=5001

.dev-installed: dev_requirements.txt
	source venv/bin/activate && pip install -r dev_requirements.txt && playwright install
	touch .dev-installed

.PHONY: test
test: .dev-installed
	@echo "Running backend tests..."
	source venv/bin/activate && PSCOMPOSE_SETTINGS=$(TEST_CONFIG) python3 -m pytest -v -s tests/*.py

.PHONY: test-frontend
test-frontend: .dev-installed
	@echo "Running frontend (Playwright) tests — ensure make run-api and make run-frontend are running first."
	source venv/bin/activate && python3 -m pytest -v tests/frontend/

# RPM install target
# Variables passed in from the spec file:
#   ROOTPATH           - destination for Python package files (pscompose_base)
#   CONFIGPATH         - destination for config files
#   HTTPD-CONFIGPATH   - destination for Apache config
#   SYSTEMD-CONFIGPATH - destination for systemd unit files
#   VENVPATH           - destination for the Python virtualenv
.PHONY: install
install:
	# Application source
	install -d $(ROOTPATH)
	cp -r pscompose $(ROOTPATH)/
	find $(ROOTPATH)/pscompose -type f | xargs chmod a-x
	# Frontend static files
	install -d $(ROOTPATH)/frontend
	cp -r pscompose/frontend/. $(ROOTPATH)/frontend/
	# install frontend npm dependencies
	cd $(ROOTPATH)/frontend && npm install
	# build the frontend CSS (color tokens + tailwind)
	cd $(ROOTPATH)/frontend && npm run build-css
	# build the frontend components index file
	cd $(ROOTPATH)/frontend && npm run generate-components-index
	# Remove the node modules now that npm steps are complete
	rm -rf $(ROOTPATH)/frontend/node_modules
	cp conf/settings.packaged.js $(ROOTPATH)/frontend/root/static/settings.js
	find $(ROOTPATH)/frontend -type f | xargs chmod a-x
	# Virtualenv with all Python dependencies
	python3 -m venv $(VENVPATH)
	$(VENVPATH)/bin/pip install --upgrade pip
	$(VENVPATH)/bin/pip install -r requirements.txt
	# Config (install -m already sets mode correctly)
	install -d $(CONFIGPATH)
	install -m 0644 conf/settings.yml $(CONFIGPATH)/settings.yml
	# Apache
	install -d $(HTTPD-CONFIGPATH)
	install -m 0644 apache/apache-pscompose.conf $(HTTPD-CONFIGPATH)/
	# systemd
	install -d $(SYSTEMD-CONFIGPATH)
	install -m 0644 systemd/perfsonar-pscompose.service $(SYSTEMD-CONFIGPATH)/
	install -m 0644 systemd/perfsonar-pscompose.socket $(SYSTEMD-CONFIGPATH)/
	install -m 0644 systemd/perfsonar-pscompose-frontend.service $(SYSTEMD-CONFIGPATH)/
	# Scripts
	install -d $(ROOTPATH)/scripts
	install -m 0755 scripts/pg_setup.sh $(ROOTPATH)/scripts/

