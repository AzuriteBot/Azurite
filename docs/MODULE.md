# How to make a module
Azurite Discord Bot is designed to be modular and flexible. You can easily create your own module to extend the bot’s functionality. Follow this guide to build your first module.

# 1. Folder Structure


```commandline
MyModule/
├─ events/
├─ commands/
│  └─ MyCommand.py
├─ commandGroup/
│  └─ MyCommandGroup.py
├─ mainEvents.py
└─ mapping.json

```
> my_custom_events/ → contains event handler classes

> bot_commands/ → contains individual command classes

> groups/ → contains command groups (optional)

> mapping.json → metadata that tells Azurite how to load the module

You can customize folder names freely; just make sure to update the paths in mapping.json.

**Support:** ``.zip``

# 2. Mapping

```json
{
  "module": {
    "mainEvent": "mainEvents.py",
    "path": {
      "events": "my_custom_events",
      "commands": "bot_commands",
      "commandGroup": "groups"
    },
    "events": ["MyEvent"],
    "command": ["MyCommand"],
    "commandGroup": ["MyCommandGroup"]
  }
}
```
mainEvent -> mainEvent contains functions that run when the module is initialized

path -> specifies the folder path for events, commands, and command groups

events, command, commandGroup -> lists of class names to load

# 3. Create a command

The main class of a command must have the same name as its file. For example, if the file is Command.py, the primary class inside it must also be named Command

```py
import discord
from discord import app_commands
from discord.ext import commands

class pingCommand(commands.Cog):
    def __init__(self, app):
        self.app = app
        super().__init__()
    @app_commands.command(name='ping', description='ping')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)
        latency = self.app.latency
        await interaction.followup.send(f"Pong! ``{latency}`` ms")
```
Command classes must inherit from ``commands.Cog``

Use decorators like ``@app_commands.command()`` to define slash commands

# 5. Using Logger
Azurite provides a built-in Logger for modules to log messages cleanly. Example usage:

```py
from Azurite import Logger

Logger.INFO("Module loaded successfully")
Logger.WARN("Warn..")
Logger.SUCCESS("Success..")
Logger.ERROR("An error occurred while loading the module")
```
You can take a look at the logger here: [click here](https://github.com/Notkenftr/Azurite/blob/main/Azurite/Logger.py)

Always use Logger instead of print() for consistency and debugging

# 6. Edit mapping.json

```json
{
  "module": {
    "mainEvent": "mainEvents.py",
    "path": {
      "events": "my_custom_events",
      "commands": "bot_commands",
      "commandGroup": "groups"
    },
    "events": ["MyEvent"],
    "command": ["MyCommand"],
    "commandGroup": ["MyCommandGroup"]
  }
}
```
For example, after you finish creating a command, add the name of the file containing that command to the command list. Do the same for events and commandGroup. Make sure the folder paths in path correspond to where the files are located.

