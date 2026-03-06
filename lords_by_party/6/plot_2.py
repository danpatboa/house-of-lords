import os

import pandas as pd
import matplotlib.pyplot as plt
import plot_params as ppar

#import lobals

IN_DIR= os.path.join('lords_by_party','5','{}')
MPS_PATH = os.path.join('lords_by_party','5','mps.csv')
OUT_PATH = os.path.join('lords_by_party','7','{}')

df_mps = pd.read_csv(MPS_PATH)
df_mps['date'] = pd.to_datetime(df_mps['date'])


for in_file in os.listdir(IN_DIR.format('')):

    if 'mps' not in in_file and 'mf' not in in_file:
        print(in_file)

        df = pd.read_csv(IN_DIR.format(in_file))


        df['date'] = pd.to_datetime(df['date'])

        fig, ax, ax_right = ppar.pre_settings()

        ax.set_title('Lords vs MPs numbers', x=0.03, loc='left',fontsize=24)

        ax.plot(df['date'], df['total'], label='Total', color='#c00000', linewidth=1.5)
        ax.plot(df_mps['date'], df_mps['number'], label='Total', color="#006548", linewidth=1.5)

        ticks = pd.date_range(
            start=df['date'].min(),
            end=df['date'].max(),
            freq='5YS'   # 5-year start frequency
        )

        ax.set_xticks(ticks)
        ax.set_xticklabels([d.year for d in ticks])

        ppar.post_settings(fig,ax,ax_right)

        out_file = in_file.replace('.csv','_mps_test.png')
        plt.savefig(OUT_PATH.format(out_file), dpi=300, facecolor=fig.get_facecolor())
