import csv
import pandas as pd

# the argument of selectData
# func:      function id
#                1: retrieve the data of specific station 
#                   and sort by `borrow time` and 'return time'
# df       : dataframe of {borrowTime,borrowId,returnTime,returnId}
# start    : yyyy/mm/dd hh:mm:ss
# end      : yyyy/mm/dd hh:mm:ss
# stationId: 9-digit id

# return value of selectData
# pandas dataframe of borrowTime of <stationId> in time <start> to <end> &
# pandas dataframe of returnTime of <stationId> in time <start> to <end>

def selectData(df,start,end,stationId):

    # split time information(not use for now)
    sYear=start[0:4]; sMonth=start[5:7]; sDay=start[8:10];
    sHour=start[11:13]; sMinute=start[14:16]; sSecond=start[17:];
    eYear=end[0:4]; eMonth=end[5:7]; eDay=end[8:10];
    eHour=end[11:13]; eMinute=end[14:16]; eSecond=end[17:];

    # borrowTime list & returnTime list
    bTimeList=[]; rTimeList=[];

    # borrowTime
    bTimeList=df.loc[df['借車站代號']==stationId]       # select by stationId
    bTimeList.sort_values(["借車時間"],axis=0,ascending=True,inplace=False)     # sorted by borrow time
    bTimeList=bTimeList[bTimeList['借車時間'].between(start,end)]       # interval between start-end

    # same task for returnTime
    rTimeList=df.loc[df['還車站代號']==stationId]
    rTimeList.sort_values(["還車時間"],axis=0,ascending=True,inplace=False)
    rTimeList=rTimeList[rTimeList['還車時間'].between(start,end)]

    return bTimeList['借車時間'],rTimeList['還車時間']

def main():
    df=pd.read_csv('D:/NSYSU Program/Graduate_Project/Data/youbike_result/result_01.csv',encoding='utf-8')
    selectData(df,"2020/12/31 22:00:00","2021/01/01 12:00:00",501203072)

if __name__=='__main__':
    main()