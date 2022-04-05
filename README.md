# py-crypto-tracker
Python Cryptocurrency price tracker with use of https://coinmarketcap.com/api/pricing/ API

## Setup virtual environment
1. Clone the repository:\
   `git clone https://github.com/gherud/py-crypto-tracker.git`
2. Go to the directory:\
   `cd py-crypto-tracker`
3. Create venv directory:\
   `python -m venv {VENV_NAME}`
4. Source virtual environment:
   - For Linux:\
      `source {VENV_NAME}/Scripts/activate`
   - For Windows:\
      `source {VENV_NAME}\Scripts\activate.bat`
5. Install libraries required to run the script:
   - Execution purposes:\
     `pip install -e .`
   - Testing purposes:\
     `pip install -e .[dev]`
