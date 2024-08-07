rm -rf build dist eztools.egg-info
find . | grep -E "(__pycache__|\.pyc|\.pyo)$" | xargs rm -rf