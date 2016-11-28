from collections import defaultdict

def parse_row(input_row, parsers):
    return [try_or_none(parser)(value) #parser(value)
            if parser is not None else value
            for value, parser in zip(input_row, parsers)]

def parse_rows_with(reader, parsers):
    for row in reader:
        yield parse_row(row, parsers)

# assume that fn would get one input
# if an error occurs, replace fn with a function that returns None.
def try_or_none(fn):
    def fn_or_none(x):
        try: return fn(x)
        except: return None
    return fn_or_none

def try_parse_field(field_name, value, parser_dict):
    parser = parser_dict.get(field_name)
    if parser is not None: # if field name is not exist, returns None
        return try_or_none(parser)(value)
    else:
        return value

def parse_dict(input_dict, parser_dict):
    return { field_name : try_parse_field(field_name, value, parser_dict)
             for field_name, value in input_dict.iteritems() }

def picker(field_name):
    return lambda row: row[field_name]

def pluck(field_name, rows):
    return map(picker(field_name), rows)

def group_by(grouper, rows, value_transform=None):
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)

    if value_transform is None:
        return grouped
    else:
        return { key:value_transform(rows)
                 for key, rows in grouped.iteritems() }

def percent_price_change(yesterday, today):
    return today['closing_price'] / yesterday['closing_price'] - 1

def day_over_day_changes(grouped_rows):
    ordered = sorted(grouped_rows, key=picker('date'))

    # to create pairs (yesterday, today)
    # zip a list don't include today and a list include today
    return [{'symbol': today['symbol'],
             'date': today['date'],
             'change': percent_price_change(yesterday, today) }
            for yesterday, today in zip(ordered, ordered[1:])]

# to obtain the final rate of change, add 1 to each rate of changes, then multiply all of them, and substract 1.
# for example, if the previous day is +10% and the next day is -20%, the final rate of change is as follows.
def combine_pct_changes(pct_change1, pct_change2):
    return (1+pct_change1) * (1+pct_change2) - 1

def overall_change(changes):
    return reduce(combine_pct_changes, pluck('change', changes))

if __name__ == "__main__":
    import dateutil.parser as dp
    import csv
    import pprint
    
    data = []
    '''
    with open("../scratch/comma_delimited_stock_prices.csv", "rb") as f:
        reader = csv.reader(f)
        for line in parse_rows_with(reader, [dp.parse, None, float]):
            data.append(line)
        for row in data:
            if any(x is None for x in row):
                print row
    '''
    with open("../scratch/stocks.txt", "rb") as f:         
        reader = csv.DictReader(f, delimiter='\t')
        data = [parse_dict(row, {'symbol':str, 'date':dp.parse, 'closing_price':float})
                for row in reader]
        '''
        for row in data[:5]:
            #if any(x is None for x in row):
            print row

        max_aapl_price = max(row['closing_price']
                             for row in data
                             if row['symbol'] == 'AAPL')
        
        #symbols = set(row['symbol'] for row in data)
        by_symbol = defaultdict(list)
        for row in data:
            by_symbol[row['symbol']].append(row)

        max_price_by_symbol = { symbol : max(row['closing_price'] for row in grouped_rows)
                                        for symbol, grouped_rows in by_symbol.iteritems() }
        '''
        max_price_by_symbol = group_by(picker('symbol'),
                                       data,
                                       lambda rows:max(pluck('closing_price', rows)))

        # key is symbol, value is list of "change" dicts
        changes_by_symbol = group_by(picker("symbol"),
                                     data,
                                     day_over_day_changes)
        
        # collect all "change" dicts into one big list
        all_changes = [change
                       for changes in changes_by_symbol.values()
                       for change in changes]

        #print max(all_changes, key=picker('change'))
        #print min(all_changes, key=picker('change'))

        # (1 + 10%) * (1 - 20%) - 1 = 1.1 * 0.8 - 1 = -12%
        overall_change_by_month = group_by(lambda row: row['date'].month,
                                           all_changes,
                                           overall_change)
        pprint.pprint(overall_change_by_month)
        

        
