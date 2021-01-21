import sys

import commands
from nubia import Nubia, Options
from extra.tfx_plugin import TFXPlugin


if __name__ == "__main__":
    plugin = TFXPlugin()
    shell = Nubia(
        name="tfx_template",
        command_pkgs=commands,
        plugin=plugin,
        options=Options(
            persistent_history=False, auto_execute_single_suggestions=False
        ),
    )
    sys.exit(shell.run())