
import matplotlib.pyplot as plt



def apply():
    """Apply all MPL settings
    """
    # print(plt.style.available)
    # plt.style.use('seaborn-paper')
    plt.style.use('seaborn-notebook')

    plt.rcParams['figure.max_open_warning'] = 1000

    plt.rcParams['figure.figsize'] = (12, 6)
