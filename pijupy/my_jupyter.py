
import IPython



def wide_display():
    """Apply HTML style to force notebook to occupy full browser width
    """
    text = """
    <style>
        div#notebook-container    { width: 100%; }
        div#menubar-container     { width:  65%; }
        div#maintoolbar-container { width:  99%; }
    </style>
    """

    html = IPython.display.HTML(data=text)

    IPython.display.display(html)



def ipython():
    """My favorite ipython settings
    """
    try:
        IPy = get_ipython()

        IPy.run_line_magic('load_ext', 'autoreload')
        IPy.run_line_magic('autoreload', 2)

        IPy.Completer.use_jedi = False
    except ImportError:
        pass


def apply():
    """Call all Jupyter settings functions
    """
    wide_display()
    ipython()
