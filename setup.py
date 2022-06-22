import cx_Freeze


executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="joga da combrinha em Python",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["sons","sprites"]}},

    executables = executables
)