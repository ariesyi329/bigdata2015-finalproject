import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

def axis_helper(ax, left=True, bottom=True, right=False, top=False,
                grid=False, xtick=True, ytick=True, color='dimgrey'):

    ax.grid(grid)
    ax.spines["right"].set_visible(right)
    ax.spines["top"].set_visible(top)
    ax.spines["left"].set_visible(left)
    ax.spines["bottom"].set_visible(bottom)
    if left is True:
        ax.spines['left'].set_color(color)
        ax.tick_params(axis='y', colors=color)
        ax.get_yaxis().tick_left()
    if bottom is True:
        ax.spines['bottom'].set_color(color)
        ax.tick_params(axis='x', colors=color)
        ax.get_xaxis().tick_bottom()
    if right is True:
        ax.spines['right'].set_color(color)
    if top is True:
        ax.spines['top'].set_color(color)
    
    if ytick is False:
        ax.yaxis.set_ticks_position('none')
    if xtick is False:
        ax.xaxis.set_ticks_position('none')



def legend_helper(title=None, loc='center left', 
                  bbox_to_anchor=(1,0.5),
                  frame_lw=0.5, frame_fc='w', frame_ec='grey',
                  frame_alpha=1, text_color='grey'):
    if title is None:
        title = ''
    legend=plt.legend(title=title, loc=loc,
                      bbox_to_anchor=bbox_to_anchor)
    frame=legend.get_frame()
    frame.set_linewidth(frame_lw)
    frame.set_facecolor(frame_fc)
    frame.set_edgecolor(frame_ec)
    frame.set_alpha(frame_alpha)
    for text in legend.get_texts():
        text.set_color(text_color)

def plot(df, columns_name):
    ax = df[columns_name].plot(kind='bar', color = 'skyblue', figsize=(16,6),alpha=0.5, width=0.8, edgecolor='w',legend=True)
    axis_helper(ax)
    legend_helper(bbox_to_anchor=(0.865,0.925))
    plt.xticks(rotation=0)
    plt.ylabel('Tip Percentage (%)', color = 'dimgrey')
    plt.xlabel('Pickup Time', color = 'dimgrey')
    plt.ylim([min(df[columns_name])-1.5,max(df[columns_name]+0.5)])

def main(df,name):
    for i in ['cluster0', 'cluster1', 'cluster2']:
        plot(df, i)
        #plt.show()
        plt.savefig(name+"_"+i+".png", dpi=200)
        plt.close()

if __name__ == "__main__":
    df_weekend= pickle.loads(open('df_cluster_weekend_timeseries','r').read())
    df_workday= pickle.loads(open('df_cluster_workday_timeseries','r').read())
    main(df_weekend,'weekend')
    main(df_workday,'workday')


