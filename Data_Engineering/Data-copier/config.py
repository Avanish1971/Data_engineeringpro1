import os

DB_details={
    'dev':{
        'source_Db':{
            'DB_type':'Mysql',
            'host':'localhost',
            'DB_Name':'DB_source',
            'username':os.environ.get('Source_DB_User'),
            'password':os.environ.get('Source_DB_Password')
        },

        'Target_Db':{
            'DB_type':'postgres',
            'host':'localhost',
            'DB_Name':'DB_target',
            'username':os.environ.get('Target_DB_User'),
            'password':os.environ.get('Target_DB_Password')
        }
    }
}