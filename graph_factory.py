import calplot
import datetime
import pylab

import pandas as pd

def get_git_commit_style(data, oldest_msg_time, newest_msg_time):
    oldest_msg_time_formatted = pd.to_datetime(datetime.datetime.fromtimestamp(oldest_msg_time/1000), format='%d/%m/%Y').normalize()
    days_active = (newest_msg_time - oldest_msg_time) // 84000000
    groupchat_days = pd.date_range(oldest_msg_time_formatted, periods=days_active, freq='D')
    events = pd.Series(data, index=groupchat_days)
    calplot.calplot(events, cmap='Blues')
    pylab.savefig('graph-output/foo.png')
