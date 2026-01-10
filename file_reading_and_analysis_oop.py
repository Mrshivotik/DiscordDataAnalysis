import matplotlib.pyplot as plt
import matplotlib.ticker
import matplotlib.dates as mdates
from collections import Counter
import datetime

class Analysis:
    """Analyses a text file."""
    
    def __init__(self, file_directory):
        """Initializes the file for further analysis."""
        with open(file_directory, 'r') as file:
            temp_list = [line.strip() for line in file]
            self.__datetime_list = [datetime.datetime.strptime(date, '%Y-%b-%d') for date in temp_list]
            self.__counted_times = Counter(self.__datetime_list)
    
    def empty_dates(self):
        """Creates empty dates to fill the dates when there were no messages sent."""
        dt = datetime.timedelta(days = 1)
        only_dates_from_dict = self.__counted_times.keys()
        start_date = min(only_dates_from_dict)
        end_date = max(only_dates_from_dict)
        all_dates = [] # Initializing a list with all dates
        while start_date <= end_date:
            all_dates.append(start_date)
            start_date += dt
        return all_dates

    def addition_and_filtering(self):
        """Adds empty dates to the dictionary, and filters it."""
        final_data = self.__counted_times.copy()
        for dates in self.empty_dates():
            final_data.setdefault(dates, 0)
        filter_dates = sorted(final_data.keys())
        plot_dates = [date for date in filter_dates]
        plot_values = [final_data[date] for date in filter_dates]
        return plot_dates, plot_values

class GraphPlotting:
    """Plots a graph from data."""

    def __init__(self, x, y, color = None, title = None, xlabel = None, ylabel = None, grid = None, xrotation = None, yrotation = None):
        """Initializes a graph.
        
        Graph properties should be input here."""
        self.__x = x
        self.__y = y
        self.__color = color
        self.__title = title
        self.__xlabel = xlabel
        self.__ylabel = ylabel
        self.__grid = grid
        self.__xrotation = xrotation
        self.__yrotation = yrotation
    
    def graphplot(self): # Function for ploting data
        """Plots data on the graph."""
        fig, ax = plt.subplots() # Create a figure containing a single Axes.
        ax.plot(self.__x, self.__y, color = self.__color) # Plot some data on the Axes.
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d %Y'))
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 1))
        ax.tick_params(axis='x', labelrotation = self.__xrotation)
        ax.tick_params(axis='y', labelrotation = self.__yrotation)
        plt.title(self.__title)
        plt.xlabel(self.__xlabel)
        plt.ylabel(self.__ylabel)
        plt.grid(self.__grid)
        plt.show()

file = Analysis(r'D:\pythonproject\data\data.txt')
x, y = file.addition_and_filtering()

graphplot = GraphPlotting(x, y, 'red', 'Message statistics', 'Time', 'Message count', True, 75)
graphplot.graphplot()

__version__ = 1.40