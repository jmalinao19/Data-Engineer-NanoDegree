<h1>Data Modeling with Postgres Project </h1>


<h2>Project Overview:</h2>
    Analyze data on songs and user activity for music streaming application. The scope is to further understand user behavior by knowing what songs they are listening to. The current state of the system doesn't have an easy way to query data. Data for the task currently lives in a directory of JSON logs on user activity and meta data of songs available in the application.


<h2>Project Tasks:</h2>
    Define fact and dimension tables in star schema model.Build an ETL pipeline (python) that transfers data from the 2 local directories into Postgres table (SQL)
    
   <h2>Data Sets:</h2>
   <h3> Song Dataset </h3>
    The first dataset is a subset of real data from the <a href= "http://millionsongdataset.com/">Million Song Dataset</a>. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID.<br>
    For example, here are filepaths to two files in this dataset.
   <p> <ul><li><code>song_data/A/B/C/TRABCEI128F424C983.json</code></li>
    <li><code>song_data/A/A/B/TRAABJL12903CDCF1A.json</code></li><br>
       </ul>
   And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.<br>
           <code> {"num_songs": 1,<br>"artist_id": "ARJIE2Y1187B994AB7",<br> "artist_latitude": null,<br> "artist_longitude": null,<br> "artist_location": "",<br> "artist_name": "Line Renaud",<br> "song_id": "SOUPIRU12A6D4FA1E1",<br> "title": "Der Kleine Dompfaff",<br> "duration": 152.92036,<br> "year": 0} </code></p>
        
   <h3>Log Dataset</h3>
    <p>The second dataset consists of log files in JSON format generated by this <a href="https://github.com/Interana/eventsim"> event simulator </a> based on the songs in the dataset above.These simulate activity logs from a music streaming   app based on specified configurations.<br>
        The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.<br>    
    <ul> <li><code>log_data/2018/11/2018-11-12-events.json</code></li>
    <li><code>log_data/2018/11/2018-11-13-events.json</code></li></p></ul>
    

   <h2> Schema for Song Play Analysis </h2>
   <h4> Fact Table  </h4>
    <ul>
        <li> <strong> Songplays </strong>-- records in log data associated with song plays </li>
        <ul>
            <li> songplay_id,start_time, user_id, level, song_id, artist_id, session_id, location, user_agent </li>
        </ul>
    </ul>
    
    
   <h4> Dimension Tables </h4>
   <ul> 
        <li> <strong>Users</strong> </li>
        <ul> 
            <li> user_id, first_name, last_name, gender, level </li>
        </ul>
        <li> <strong> Songs</strong> </li>
        <ul> 
            <li> song_id, title, artist_id, year, duration</li>
        </ul>
        <li> <strong>Artists </strong> </li>
        <ul> 
            <li> artist_id, name, location, latitude, longitude </li>
        </ul>
        <li> <strong>Time </strong> </li>
        <ul> 
            <li> start_time, hour, day, week, month, year, weekday </li>
        </ul>
    </ul>

   <h2> Project Files</h2>
   <ul>
        <li> <code>create_tables.py </code> -- drops and creates your tables. Run this file to reset tables before each running your ETL scripts.</li>
        <li> <code>etl.py </code> -- Reads and processes files from song_data and log_data and loads them into the tables.</li>
        <li> <code>sql_queries.py</code> -- has all SQL queries and is imported to <code>etl.py</code>, <code>create_tables.py</code>, and <code>etl.ipynb</code>.</li>
        <li> <code>test.ipynb</code> -- This tests the database by displaying the first few rows of each table</li>
        <li> <code>etl.ipynb</code> -- This file contains a workbook to help build out the etl.py file</li>
    </ul>
 
   <h2> Execution Steps </h2>
   <ol>
        <li> Run <code>create_tables.py</code> to create database and tables</li>
        <li> Run <code> etl.py </code> to process the song and log data </li>
        <li> Run <code>test.ipynb</code> to confirm the creation of your tables with the correct columns. Make sure to click "Restart Kernel" to close the connection to the database after running this notebook</li> 
    </ol>
    

