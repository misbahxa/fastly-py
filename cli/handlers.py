def outputsingle(response_data, format='inline'):
    if format == 'inline':
        separator = ': '
        for key in response_data.keys():
            data = response_data[key]
            if type(data) == str:
                if data.find('\n') != -1:
                    separator = ':\n'
            print("{0}{1}{2}".format(key, separator, data))
    elif format == 'raw':
        print(response_data)