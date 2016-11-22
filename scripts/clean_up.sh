find . -name "*.pyc" -exec rm -rf {} \;
find . -name "__pycache__" -exec rm -rf {} \;
rm -rf build/
rm -rf dist/
rm src/transliterate.egg-info -rf
rm builddocs.zip