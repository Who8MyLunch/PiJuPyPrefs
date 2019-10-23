
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



def apply():
    """Call all Jupyter settings functions
    """
    wide_display()
