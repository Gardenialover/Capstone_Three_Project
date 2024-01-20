DATA_DIR = '../data'
TRAIN_FILE_PATH = "../data/raw/drugsComTrain_raw.tsv"
TEST_FILE_PATH = "../data/raw/drugsComTest_raw.tsv"

DTYPES = {
    'id': 'int64',
    'drugname': 'str',
    'condition': 'str',
    'review': 'str',
    'rating': 'float64',
    'date': 'datetime64[ns]',
    'usefulcount': 'int64'
}
