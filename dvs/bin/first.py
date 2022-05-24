"""
Train a new model with your awesome parameters
"""
import typer

from dvs.utils import setup_logger

import math
import pandas as pd
import matplotlib.pyplot as plt


def radar_chart(df, row, color, title, ticks, trick_labels):
    categories=list(df)[0:]
    N = len(categories)

    angles = [n / float(N) * 2 * math.pi for n in range(N)]
    angles += angles[:1]
     
    plt.rc('figure', figsize=(12, 12))
 
    ax = plt.subplot(1,1,1, polar=True)
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
 
    plt.xticks(angles[:-1], categories, color='black', size=12)
    ax.tick_params(axis='x', rotation=5.5)
    
    ax.set_rlabel_position(0)
    plt.yticks(ticks, trick_labels, color="black", size=10)
    plt.ylim(0, max(ticks))
 
    
    values=df.reset_index().loc[row].values.tolist()[1:]
    values += values[:1]
    ax.plot(angles, values, color = color, linewidth=1, linestyle='solid')
    ax.fill(angles, values, color = color, alpha = 0.5)
 
    title = "Radar showing performance in each subject for "+ title
    plt.title(title, fontsize=20, x = 0.5, y = 1.1)
 

def main():
    typer.echo(f"Running {__file__}")
    df = pd.DataFrame(
        {
            'Power':        [2, 4, 5, 4, 5],
            'Speed':        [4, 4, 2, 4, 3],
            'Range':        [5, 1, 5, 1, 0],
            'Durability':   [1, 1, 5, 4, 1],
            'Precision':    [3, 1, 5, 1, 1],
            'Potential':    [4, 1, 5, 3, 2],
        }, index=['A', 'B', 'C', 'D', 'E']
    )
    print(df)
    fills = ["#487eb0", "#6a89cc", "#81cfe0", "#00b5cc", "#52b3d9"]
    for row in range(0, len(df.index)):
        plt.figure()
        radar_chart(row=row, df=df, title=df.index[row], color=fills[row],
            ticks=[1,2,3,4,5], trick_labels=["1", "2", "3", "4", "5"])
        plt.show()



if __name__ == "__main__":
    setup_logger()
    typer.run(main)
