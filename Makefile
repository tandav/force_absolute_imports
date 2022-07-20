.PHONY: test
test:
	python -m pytest -v tests

.PHONY: bump2version
bump2version:
	bump2version $(STEP)
