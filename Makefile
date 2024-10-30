
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
