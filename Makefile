.PHONY: install-poetry
install-poetry:
	pip install poetry

.PHONY: install
install: install-poetry
	poetry lock -n
	poetry install -n

.PHONY: test
test: install
	poetry run pytest

# Example: make docker VERSION=latest
# Example: make docker IMAGE=some_name VERSION=0.1.0
.PHONY: docker
docker:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile --no-cache

# Example: make clean_docker VERSION=latest
# Example: make clean_docker IMAGE=some_name VERSION=0.1.0
.PHONY: clean_docker
clean_docker:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

.PHONY: clean_build
clean:
	rm -rf build/

.PHONY: clean
clean: clean_build clean_docker
