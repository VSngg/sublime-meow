import sublime
import sublime_plugin

def toggle_command_mode(buf, enable):
    if enable and buf.is_read_only():
        sublime.status_message('Buffer is read only')
    elif enable:
        buf.settings().set(key='block_caret', value=True)
        buf.settings().set(key='command_mode', value=True)
    else:
        buf.settings().set(key='block_caret', value=False)
        buf.settings().set(key='command_mode', value=False)

class MeowInsertModeCommand(sublime_plugin.TextCommand):
    """
    Switch to INSERT mode, put carets at the start of each selection.
    """
    def run(self, edit):
        toggle_command_mode(self.view, False)
        
class MeowInsertModeAppendCommand(sublime_plugin.TextCommand):
    """
    Switch to INSERT mode, put carets at the end of each selection.
    """
    def run(self, edit):
        self.view.run_command("move", {"by": "characters", "forward": True})
        toggle_command_mode(self.view, False)

class MeowEscapeCommand(sublime_plugin.TextCommand):
    """
    Smart escape command.
    """
    def run(self, edit):
        buf = self.view
        if len(buf.sel()) > 1:
            buf.run_command("single_selection")
        else:
            toggle_command_mode(buf, True)

 
class MeowCommandModeCommand(sublime_plugin.TextCommand):
    """
    Switch to COMMAND mode.
    """
    def run(self, edit):
        toggle_command_mode(self.view, True)

class MeowNextWordCommand(sublime_plugin.TextCommand):
    """
    Forward one word.
    """
    def run(self, edit):
        self.view.run_command("move", {"by": "subword_ends", "forward": True, "extend": True})

class MeowPrevWordCommand(sublime_plugin.TextCommand):
    """
    Backward one word.
    """
    def run(self, edit):
        self.view.run_command("move", {"by": "subwords", "forward": False, "extend": True})

class MeowChangeCommand(sublime_plugin.TextCommand):
    """
    Change selection
    """
    def run(self, edit):
        self.view.run_command("right_delete")
        toggle_command_mode(self.view, False)

class MeowOpenLineBelowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("move_to", {"to": "eol"})
        self.view.run_command("insert", {"characters": "\n"})

class MeowOpenLineAboveCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("move_to", {"to": "bol"})
        self.view.run_command("insert", {"characters": "\n"})
        self.view.run_command("move", {"by": "lines", "forward": False})

class MeowCopyLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("expand_selection", {"to": "line"})
        self.view.run_command("copy")

class MeowCutLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("expand_selection", {"to": "line"})
        self.view.run_command("cut")
