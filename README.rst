CatBot
======
CatBot - this is a bot for Telegram, created for making your life better, by sending photos of kittens to you.

Installing
----------

Create virtual env and activate it. And than in it:

.. code-block:: text

    pip install -r requirements.txt

Put cats' pics to images folder. Cats' files should be *.jpg or *.jped, for example cat.jpg.

Set up
------

Create file settings.py and add there:

.. code-block:: python

PROXY = {'proxy_url': 'socks5://your_proxy:1080', 'urllib3_proxy_kwargs': {'username': 'login', 'password': 'pass'}}

API_KEY = "your_api_key"

USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

Launch
------

When you activate env you need to launch:

.. code-block:: text

    python3 bot.py