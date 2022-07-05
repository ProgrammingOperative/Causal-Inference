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

        # node_attributes = {
        #     "diagnosis": { 
        #         "shape": "star",
        #         "style": "filled",
        #         "width": 0.6,
        #         "penwidth": "1", 
        #         "color": "#4a90e2d9",
        #         "orientation": 25, 
        #     },
        #     "fontsize": 0.1
        # }

        # graph_attributes = {
        #     "scale": "1",
        #     "size": 5,
        #     "label": "Breast Cancer Causality model",
        #     "fontcolor": "#FFFFFFD9",
        #     "fontname": "Helvetica",
        #     "fontsize": 25, # font size of the graph title
        #     "dpi": 200,  # resolution
        #     "labeljust": "l",  # left
        #     "labelloc": "t",  # top
        #     }

        viz = plot_structure(
            sm,
            graph_attributes= {"scale":"5", "size":5},
            all_node_attributes=NODE_STYLE.WEAK,
            all_edge_attributes=EDGE_STYLE.WEAK
            )


        return Image(viz.draw(format='png'))


    #correlation matrix
    def plot_correlation_heatmap(X:pd.DataFrame):
        """  
        args:
            X (pd.DataFrame): a dataframe of the independent variables
        
        returns:
            a heatmap of the correlation
        """

        corrmat = X.corr()
        f, ax = plt.subplots(figsize=(20, 9))
        sns.heatmap(corrmat, annot=True, linewidths=.5, fmt= '.1f',ax=ax)