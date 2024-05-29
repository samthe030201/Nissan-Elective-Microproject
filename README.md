# Nissan-Elective-Microproject
## CSV Documentation
### 1. featured_Spotify_artist_info.csv
dates: Date that an artist was featured, str\n
ids: Unique Spotify IDs of each artist, str
names: Spotify artist name, str
monthly_listeners: The number of unique monthly listeners for each artist, collected during April and May 2024. This is the most reliable measure of an artist's popularity, that's publicly available on Spotify, float, 0 if absent
popularity: The Spotify-defined popularity metric, int
followers: The number of followers the artist has, int
genres: The musical genres associated with each artist: where more than one genre is associated with an artist, separate genres are contained within quotation marks and separated by commas; where only one genre is present, no quotations marks are used, str, empty if no genres
first_release: The year of an artist's first release, int, -1 if no releases
last_release: The year of an artist's most recent release, as of May 2024, int, -1 if no releases
num_releases: The total number of releases an artist has made, as of May 2024, capped at 20 (all numbers >20 are set to 20) int, -1 if no releases
num_tracks: The number of tracks in the most recent album/single that an artist has released, as of May 2024, int, -1 if no tracks
playlists_found: The Editorial playlists in which the artist was featured, on the date in question, str, follows the same formatting as genres
feat_track_ids: Spotify track IDs of the featured tracks

### 2. featured_Spotify_track_info.csv
ds: Unique Spotify IDs of each track, str
names: Name of the track, str
popularity: The Spotify-defined popularity metric, int
markets: The market code of the markets in which the track is available, int
artists: The Spotify IDs of the artists that created the track: where more than one artist has collaborated on a track, separate artists are contained within quotation marks and separated by commas; where only one artist is present, no quotations marks are used, str
release_date: The date on which the track was released, as provided by Spotify. Sometimes this is just a year, other times a specific day, str
count: The number of separate instances (dates and Editorial playlists) in which the track was featured, str
dates: The dates that the track was featured on any playlist, str
playlists_found: The Editorial playlists in which the track was featured, str, follows the same formatting as in featured_Spotify_artist_info.csv
duration_ms: The duration of the track in milliseconds, int
acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic, float, range 0-1
danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity, float, range 0-1
energy: Represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy, float, range 0-1
instrumentalness: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0, float, range 0-1
liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live, float, range 0-1
loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db, float
speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks, float, range 0-1
tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration, float
valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry), float
musicalkey: Equivalent to the 'key' field in the Spotify Web API syntax. The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1, int
musicalmode: Equivalent to the 'mode' field in the Spotify Web API syntax. Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0, int
time_signature: An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4", int, only 5 time signatures are represented
