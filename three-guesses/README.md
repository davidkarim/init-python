Alfred Script is named `Python three-guesses` and runs the following code:

```
curl -s -H "Accept:application/vnd.github.v3.raw" https://api.github.com/repos/davidkarim/init-python/contents/three-guesses/main.py
```
append ` > main.py` to the end to create file.

Then run:

```
python3 main.py
```
