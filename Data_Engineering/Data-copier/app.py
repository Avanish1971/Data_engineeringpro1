import sys
from config  import DB_details
from utils import get_table

def main():
    env=sys.argv[1]
    db_details=DB_details.get(env)
    tables=get_table('table_list')
    for idx,table in tables.iterrows():
        print(table)

if __name__=='__main__':
    main()