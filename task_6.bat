env/Scripts/activate
python -m pytest task_5_test.py
PYTEST_EXIT_CODE=$?

if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1

PAUSE