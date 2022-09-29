Spotify+
========================
## Spotipy Documentation
You can find all the documentation to use Spotipy and add features [here](https://spotipy.readthedocs.io/en/master/)

## Installation
Spotipy will need to be installed for this to work. It can be done through an IDE such as PyCharm or by using these commands.

`pip install spotipy`
or
`pip install spotipy --upgrade` 

## Quick Start
The first thing you need to do is create an app on https://developer.spotify.com/  <br>
This will provide you with three essential environment variables that we need to set: <br>
`SPOTIPY_CLIENT_ID` which will be the client ID on the Spotify app <br>
`SPOTIPY_CLIENT_SECRET` which can also be found on the Spotify developer page <br>
`SPOTIPY_REDIRECT_URI` which will be set on the developer page (usually a localhost such as http://localhost:8888/callback) <br>

### Setting these environment variables
Use the `export` command to set these variables. Another option is to edit the configuration on your IDE and set the envrionment variables there.

`export SPOTIPY_CLIENT_ID <Client ID>` <br>
`export SPOTIPY_CLIENT_SECRET <Client Secret>` <br>
`export SPOTIPY_REDIRECT_URI <Redirect URI>`<br>

### Running the script
This should be everything you need to run the scripts and use the various features

## Features
### Equal Queueing
When using a Spotify listening party, people will queue numerous songs at once and this usually means you end up listening to one person's songs for a while. <br>
With this script each person can enter a list of song names and it will play one song from each person's queue one at a time.
### Queue current artist
If you really like the current artist you're listening to you can use this script which will take the current artist you're listening to, find a song by them in your playlist and queue it next.
### Current mood playlist
Creates a playlist based on the last 5 songs you listened to, you can choose how many songs are added (Max 50) and whether you want to add to an existing playlist or create a new one.
### Statistics
You can get statistics about a playlist or about the 5 most recent songs you listened to. Statistics include:
<ul>
<li>danceability</li>
<li>energy</li>
<li>key</li>
<li>loudness</li>
<li>speechiness</li>
<li>acousticness</li>
<li>instrumentalness</li>
<li>liveness</li>
<li>valence</li> 
<li>tempo</li>
</ul>


