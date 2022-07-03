import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from IPython.display import Image
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go  
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE




class Plot:
    
    def __init__(self) -> None:
        pass

    def feature_vs_target(self, df, x):    

        fig,ax = plt.subplots(nrows = 10, ncols = 3, figsize = (12,24),dpi=80)
        axes = ax.ravel()

        for col,ax in zip(x.columns,axes):
            # plots
            sns.kdeplot(df[col], ax = ax, shade = True ,
                        palette=["red", "green"],
                        alpha = 0.5, linewidth = 1, ec = 'black',
                        hue = df['diagnosis'], hue_order = ['M','B'],
                        legend = False)

            # plot setting
            xlabel = ' '.join([value.capitalize() for value in str(col).split('_') ])
            ax.axes.set_xlabel(xlabel,{'font':'serif','size':10, 'weight':'bold'}, alpha = 1)

        plt.tight_layout(pad= 2,h_pad = 1, w_pad = 1)

        fig.text(0.615,1, "\n       Benign",{'font':'serif','size':14, 'weight':'bold', 'color':"green"}, alpha = 1)
        fig.text(0.735,1, '|',{'font':'serif','size':16, 'weight':'bold'})
        fig.text(0.75,1, "  Malignant",{'font':'serif','size':14, 'weight':'bold','color':"red"}, alpha = 1)

        fig.show()


    def vis_sm(self, sm):
        viz = plot_structure(
            sm,
            graph_attributes={"scale": "2.0", 'size': 2.5},
            all_node_attributes=NODE_STYLE.WEAK,
            all_edge_attributes=EDGE_STYLE.WEAK)
        return Image(viz.draw(format='png'))