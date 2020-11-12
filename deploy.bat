rmdir /S /Q dist
pipenv run python setup.py sdist bdist_wheel
python -m twine upload --repository pypitest dist/*
