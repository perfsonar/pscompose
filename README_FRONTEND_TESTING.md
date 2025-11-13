# Frontend Testing

We use the python version of playwright to do frontend / integration testing.

To get started:

```
python3 -m venv venv                # create the venv if you haven't already
source venv/bin/activate            # activate new venv
pip install -r dev_requrements.txt  # install playwright and pytest
playwright install                  # install browsers & bindings for playwright
venv/bin/playwright codegen http://localhost:5001  # create test code generation with live browser
```
