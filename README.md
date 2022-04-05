# py-crypto-tracker
Python Cryptocurrency price tracker with use of https://coinmarketcap.com/api/pricing/ API

## Setup virtual environment
1. Clone the repository:\
   ```sh
   git clone https://github.com/gherud/py-crypto-tracker.git
   ```
2. Go to the directory:\
   ```sh
   cd py-crypto-tracker
   ```
3. Create venv directory:\
   ```sh
   python -m venv {VENV_NAME}
   ```
4. Source virtual environment:
   - For Linux:\
      ```sh
      source {VENV_NAME}/Scripts/activate
      ```
   - For Windows:\
      ```powershell
      source {VENV_NAME}\Scripts\activate.bat
      ```
5. Install libraries required to run the script:
   - Execution purposes:\
     ```sh
     pip install -e .
     ```
   - Testing purposes:\
     ```sh
     pip install -e .[dev]
     ```


## Run the application:
1. Copy `config.yaml` and name it `local_config.yaml`.
2. Update `api_key` and `bot_token` in `local_config.yaml`.
3. The rest of the fields do not need to be updated.
4. You are set up, now run e.g. `track -c btc`!
