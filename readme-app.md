## Initialize

```sh
cd app
# Create virtial env in root folder
python3.9 -m venv .venv
source .env/bin/activate

# Install required packages
pip install -r requirements.txt
```

## Run APP

```sh
# envs
export FLASK_ENV=development


# run flask app
python app.py
```
