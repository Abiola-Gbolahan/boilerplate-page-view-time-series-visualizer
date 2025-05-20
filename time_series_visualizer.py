import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df=pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col= 'date')

# Clean data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
# Filter out values outside the bounds
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]


def draw_line_plot():
    df_copy = df.copy()
    # Draw line plot
    plt.figure(figsize=(14, 6))
    plt.plot(df_copy.index, df_copy['value'], color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_copy = df.copy()
    
    # Resample the data to get monthly averages
    df_monthly = df_copy.resample('M').mean()
    df_monthly['year'] = df_monthly.index.year
    df_monthly['month'] = df_monthly.index.month_name()
    
    # Pivot the data for plotting
    df_pivot = df_monthly.pivot(index='year', columns='month', values='value')
    
    # Define the order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    plt.figure(figsize=(14, 8))
    ax = df_pivot[month_order].plot(kind='bar')
    plt.title('Average Daily Page Views by Month and Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

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
    # Set up the figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_copy, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_copy, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
   
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
