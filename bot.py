"""
Discord Bot - bot.py
Starts the bot from the JSON Config and setups any commands / events we have.


This does use a MongoDB Database.
"""

import json
import os
import pymongo


import discord

# Check for the Config file. We can't continue without it
if os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as c:
        config = json.load(c)