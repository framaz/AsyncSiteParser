import asyncio
from Inputs.consoleinput import ConsoleInput, ConsoleDebugInput
from Sites.dvach import Dvach
from hooks.dvachhooks import DvachShowHook, DvachFileDownloader
from asyncparser import AsyncParser
from Inputs.consoleinput import ConsoleDebugInput

site = Dvach("https://2ch.hk/b/res/219877715.html")
hook = DvachFileDownloader()
site.add_hook(hook)
parser = AsyncParser()
parser.add_content_provider(site)

parser.add_input_source(ConsoleDebugInput())
parser.start()
