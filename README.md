### Get setup to develop for the take home assignment.

1. <b>Install Pyenv to switch between different Python versions.</b> <br>
   https://github.com/pyenv/pyenv, windows: https://github.com/pyenv-win/pyenv-win
2. <b>Install the python version specified in /nira-data-pipeline/.python-version using Pyenv.</b> <code> pyenv install 3.9.6 </code>
3. <b>Navigate into the /nira-data-pipeline directory and double check that you've set up pyenv correct. </b> <br>
   When you run <code>python --version</code>, the version should match the version specified at /nira-data-pipeline/.python-version. <br>
   Pyenv works by reading the .python-version file and automaticaly switching to the right python version.
4. <b>Install poetry</b> https://python-poetry.org/docs/
5. <b>Configure Poetry to create .venv folders in the project</b> <code>poetry config virtualenvs.in-project true</code>
6. <b>Navigate into the pipeline folder</b> <code>cd /nira-data-pipeline/pipeline</code>
7. <b>Install dependencies</b> <code>poetry install</code>
8. <b>Activate the virtual environment.</b> <code> poetry shell </code>
9. <b>Double check that the right version of python is being used in the virtual environment.</b> <code>python --version</code>
10. <b>Make sure that the dependencies were installed.</b> <code>poetry show</code>
11. <b>Spin up dagit. </b> <code>poetry run dagit</code>
12. <b>Navigate to localhost:3000. You should see dagster running there </b>
13. <b>In the ui, run the "smoketest" job. </b> You should see the job print "Successfully ran smoketest".
