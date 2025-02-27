"""Our first example plugin."""


class ExampleTwo:
    """Second Example Plugin."""
    name = 'off-by-default-example-plugin'
    version = '1.0.0'

    off_by_default = True

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        """Do nothing."""
        yield (1, 0, 'X200 The off-by-default plugin was enabled',
               'OffByDefaultPlugin')
