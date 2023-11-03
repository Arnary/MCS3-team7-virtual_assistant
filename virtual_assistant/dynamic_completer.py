from prompt_toolkit.completion import Completer,WordCompleter

class DynamicCompleter(Completer):
    def __init__(self, autocomplete_list):
        self.autocomplete_list = autocomplete_list
 

    def get_completions(self, document, complete_event):
        if ' ' in document.text_before_cursor:
            empty_completer = WordCompleter([])
            return empty_completer.get_completions(document, complete_event)
        else:
            first_argument_completer = WordCompleter(self.autocomplete_list)
            return first_argument_completer.get_completions(document, complete_event)