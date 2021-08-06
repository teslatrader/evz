import pandas as pd
import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('year', nargs=argparse.REMAINDER)

years = dict(vars(parser.parse_args()))
years = eval(str(years['year']))


def write_time_serias(data_seria, filename):
    with open(f'{filename}.txt', 'w') as f:
        text = str(data_seria)
        wr = f.write(text)

def main():
    dates = []
    values = []
    frame = []
    for year in years:
        datetime_path = f'./{year}/datetime'
        frame = pd.read_csv(datetime_path, sep=',', header=None).values.tolist()
        dates += frame[0]

    for i in range(len(dates)):
        dates[i] = dates[i].replace(' D', 'D')

    for year in years:
        values_path = f'./{year}/values'
        frame = pd.read_csv(values_path, sep=',', header=None).values.tolist()
        values += frame[0]


    with open('dates_results.txt', 'w') as f:
        text = str(dates).replace('"', '')
        wr = f.write(text)

    open_seria = values[::4]
    high_seria = values[1::4]
    low_seria = values[2::4]
    close_seria = values[3::4]
    median_seria = []
    typical_seria = []
    weigthed_seria = []
    for i in range(len(open_seria)):
        median_seria.append((high_seria[i] + low_seria[i]) / 2)
        typical_seria.append((high_seria[i] + low_seria[i] + close_seria[i]) / 3)
        weigthed_seria.append((open_seria[i] + high_seria[i] + low_seria[i] + close_seria[i]) / 4)

    # write_time_serias(open_seria, 'open')
    # write_time_serias(high_seria, 'high')
    # write_time_serias(low_seria, 'low')
    # write_time_serias(close_seria, 'close')
    # write_time_serias(median_seria, 'median')
    # write_time_serias(typical_seria, 'typical')
    # write_time_serias(weigthed_seria, 'weighted')


if __name__ == '__main__':
    main()