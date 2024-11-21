
.PHONY: run_api
run_api:
	fastapi run pscompose/api/api.py

.PHONY: docker-build
docker-build:
	@echo "Building docker image..."
	$(eval HASH := $(shell docker build -q .))
	echo ${HASH}

.PHONY: docker
docker: docker-build
	docker run -p "8080:80" -it ${HASH}

.PHONY: css-watch
css-watch:
	@echo "Starting tailwind via npm to watch for CSS changes..."
	cd pscompose/frontend && npm run css-watch

.PHONY: run-mockups
run-mockups:
	@echo "Starting simple HTTP server on http://localhost:8000/"
	cd pscompose/frontend && python3 -m http.server
