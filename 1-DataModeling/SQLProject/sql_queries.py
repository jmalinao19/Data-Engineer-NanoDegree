# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users "
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL Primary key,
    start_time TIMESTAMP NOT NULL,
    user_id INT,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id int,
    location VARCHAR,
    user_agent VARCHAR
)
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY UNIQUE,
    first_name VARCHAR,
    last_name VARCHAR,
    gender CHAR, 
    level VARCHAR
)
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs(
    song_id VARCHAR PRIMARY KEY UNIQUE,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT
)
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY UNIQUE,
    name VARCHAR,
    location VARCHAR,
    lat FLOAT,
    long FLOAT
)
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS times (
    start_time BIGINT,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday varchar
)
""")


# INSERT RECORDS
songplay_table_insert = ("""INSERT INTO songplays (songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""INSERT INTO users (user_id,first_name,last_name, gender, level) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""INSERT INTO songs (song_id,title,artist_id,year,duration) values (%s,%s,%s,%s,%s) ON Conflict DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists(artist_id,name,location,lat,long) values (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

time_table_insert = (""" INSERT INTO times (start_time,hour,day,week,month,year, weekday) values (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    Select songs.song_id, artists.artist_id FROM songs 
    JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title =%s
    AND artists.name =%s
    AND songs.duration =%s
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]