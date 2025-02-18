.PHONY: build check install dist sources srpm rpm pypi clean

PYTHON   ?= python3
NAME     := psh
RPM_NAME := python-$(NAME)
VERSION  := $(shell sed -n s/[[:space:]]*Version:[[:space:]]*//p $(RPM_NAME).spec)

TEST_ENV_PATH         := test-env
CHECK_PYTHON_VERSIONS := 2 3

build:
	$(PYTHON) setup.py build

check:
	@mkdir -p "$(TEST_ENV_PATH)"
	@set -e; for version in $(CHECK_PYTHON_VERSIONS); do \
		echo; echo "Testing $(NAME) with python$$version..."; echo; \
		env_path="$(TEST_ENV_PATH)/python$$version"; \
		if [ ! -e "$$env_path" ]; then \
			virtualenv --python python$$version --distribute "$$env_path" && \
				"$$env_path/bin/pip" install psys pytest || { rm -rf "$$env_path"; false; }; \
		fi; \
		"$$env_path/bin/python" setup.py test; \
	done

install:
	$(PYTHON) setup.py install --skip-build $(INSTALL_FLAGS)


dist: clean
	$(PYTHON) setup.py sdist
	cp dist/$(NAME)-*.tar.gz .

sources: clean
	@git archive --format=tar --prefix="$(NAME)-$(VERSION)/" \
		$(shell git rev-parse --verify HEAD) | gzip > $(NAME)-$(VERSION).tar.gz

srpm: dist
	rpmbuild -bs --define "_sourcedir $(CURDIR)" $(RPM_NAME).spec

rpm: dist
	rpmbuild -ba --define "_sourcedir $(CURDIR)" $(RPM_NAME).spec

pypi: dist
	$(PYTHON) -m twine upload dist/*

clean:
	find . -depth -type d -name __pycache__ -exec rm -rf {} \;
	rm -rf build dist $(NAME)-*.tar.gz $(NAME).egg-info *.egg $(TEST_ENV_PATH)
