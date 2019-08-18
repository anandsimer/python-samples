from collections import namedtuple

# complex data structure with List of Dictionaries and
# each dictionary have a nested list.

mysample = [
    {
        'data': [
            [
                '15th August',
                '2018'
            ]
        ],
        'label': 'August Cal',
    },
    {
        'data': [
            [
                '16th January',
                '2000'
            ]
        ],
        'label': 'January Cal'
    }
]

# namedtuple for inner list items of data keys
data_inner_list = namedtuple('data_inner_list', ['day', 'year'])

data_as_dict = namedtuple('data_as_dict', ['data', 'label'])

for _, item in enumerate(mysample):
    mysample_parsed = data_as_dict(
        data_inner_list(
            item['data'][0][0],
            item['data'][0][1]
        ),
        item['label']
    )
    print(mysample_parsed.data.year + ' : ' + mysample_parsed.data.day)

