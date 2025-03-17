import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates= True, index_col = 'date')

# Clean data
threshold_upper = df['value'].quantile(.975)
threshold_lower = df['value'].quantile(.025)

df = df[(df['value'] >= threshold_lower) & (df['value'] <= threshold_upper)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df.index.year
    df_bar['Month'] = df.index.month
    df_grouped = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))

    df_grouped.plot(kind= 'bar', ax= ax)

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views per Month')

    month_labels = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    ax.legend(title= 'Months', labels= month_labels)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
    
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, axes = plt.subplots(1, 2, figsize= (15, 6))

    sns.boxplot(x='year', y='value', data= df_box, ax= axes[0], palette= 'Set1')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data= df_box, order= month_order, ax= axes[1], palette= 'Set2')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
