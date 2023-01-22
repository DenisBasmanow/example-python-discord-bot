# Example Python Discord Bot

**For launch:**
1. Install Python 3 (https://www.python.org/downloads/).
2. Download the repository and open the folder with the repository files in the terminal.
3. (optional) Create Python virtual environment. <br>
3.1. Execute command ``python -m venv venv`` (or ``python3 -m venv venv``). <br>
3.2. Enter the virtual environment. For UNIX systems ``source venv/bin/activate``, for windows ``venv\Scripts\activate.bat``.
4. Install requirements ``pip install -r requirements.txt`` (or ``pip3 install -r requirements.txt``).
5. Set up environment variables. <br>
5.1. Create file ``.env``. <br>
5.2. In file ``.env`` write (replace ``token`` with your bot's token):
```py
BOT_TOKEN=token
```
6. Execute command ``python main.py`` (or ``python3 main.py``) for launch bot.
