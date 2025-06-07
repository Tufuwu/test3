.venv:
	python -m venv .venv
	source .venv/bin/activate && make setup dev
	echo 'run `source .venv/bin/activate` to develop diff-match-patch'

venv: .venv

setup:
	python -m pip install -Ur requirements-dev.txt

dev:
	python setup.py develop

release: lint test clean
	python setup.py sdist wheel
	python -m twine upload dist/*

format:
	python -m isort diff_match_patch
	python -m black diff_match_patch

lint:
	python -m isort --diff diff_match_patch
	python -m black --check diff_match_patch

test:
	python -m unittest -v diff_match_patch.tests
	python -m mypy diff_match_patch/diff_match_patch.py

clean:
	rm -rf build dist html README MANIFEST *.egg-info

distclean: clean
	rm -rf .venv
