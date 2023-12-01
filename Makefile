SRC_DIR := $(CURDIR)/src

migrations:
	poetry run alembic upgrade head

run_app:

	PYTHONPATH=$(SRC_DIR) poetry run python3.11 $(SRC_DIR)/memories

start: migrations run_app