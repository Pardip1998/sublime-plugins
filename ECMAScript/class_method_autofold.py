import sublime
import sublime_plugin

class AutoFoldListener(sublime_plugin.EventListener):
    def on_load_async(self, view):
        if view.match_selector(0, "source.js"):
            # Fold all functions/methods inside classes
            view.run_command("fold_by_level", {"level": 2})
