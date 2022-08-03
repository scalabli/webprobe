import sys


if sys.version_info > (3, 7):
    from quo import container
    from quo.widget import Box, Label

    content = Box(
            Label("Webprobe requires Python <=3.8\n\nPress `Ctrl-C` to quit", style="fg:red")
            )

    container(content, bind=True, full_screen=True)
