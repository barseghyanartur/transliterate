find . -name "*.pyc" -exec rm -rf {} \;
find . -name "__pycache__" -exec rm -rf {} \;
find . -name "*.orig" -exec rm -rf {} \;
find . -name "*.py,cover" -exec rm -rf {} \;
rm -rf build/
rm -rf dist/
rm -rf .cache/
rm -rf htmlcov/
rm src/transliterate.egg-info -rf
rm builddocs.zip