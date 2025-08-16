"""
AutoFold JS Plugin for Sublime Text
-----------------------------------

Description:
    This Sublime Text plugin automatically folds class methods 
    (functions defined inside classes) when opening any JavaScript (.js) file. 

How it works:
    - Listens to the `on_load_async` event whenever a file is opened.
    - Checks if the file syntax is JavaScript (`source.js`).
    - Automatically folds code by level (level 2 = methods inside a class).

Installation:
    1. In Sublime Text, go to: Tools → Developer → New Plugin…
    2. Replace the default content with this code.
    3. Save the file as `auto_fold_js.py` inside `Packages/User`.

Notes:
    - Level 1 folds everything under top-level (e.g. inside class).
    - Level 2 folds class methods but keeps the class definition visible.
    - You can adjust the folding level depending on your preference.
"""

import sublime
import sublime_plugin

class AutoFoldListener(sublime_plugin.EventListener):
    def on_load_async(self, view):
        if view.match_selector(0, "source.js"):
            # Fold all functions/methods inside classes
            view.run_command("fold_by_level", {"level": 2})
