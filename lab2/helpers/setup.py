import seaborn as sns
import matplotlib.pyplot as plt

def setup():
    setup_visualization()

def setup_visualization():
    """Настройка параметров визуализации"""
    sns.set_theme(
        style="whitegrid",
        context="notebook",
        palette="viridis"
    )
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['figure.dpi'] = 100
