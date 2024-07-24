# Functions for interacting with the database and general data manipulation
from ..utils.spotify import sp, fetch_all_items
from ..models import Playlist

# TODO: see if I need this? I seem to already be doing it with filters?
# def make_time_readable(seconds):
#     seconds = seconds % (24 * 3600)
#     hour = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60

#     return "%d:%02d:%02d" % (hour, minutes, seconds)

# Save Playlist to Database
def save_playlist_to_db(spotify_id, snapshot_id, name, collaborative, public):
    try:
        result = sp.playlist_items(playlist_id=spotify_id)
    except Exception as e:
        print(e)
    else:
        tracks = result["items"]

    while result["next"]:
        try:
            result = sp.next(result)
        except Exception as e:
            print(e)
        else:
            tracks.extend(result["items"])

    #Get total duration of all tracks in the playlist
    total_duration = calculate_total_duration(tracks)

    number_of_tracks = len(result["items"])
    print(number_of_tracks)

    average_track_length = calculate_average_track_length(total_duration, number_of_tracks)

    pl = Playlist(
        spotify_id=spotify_id,
        snapshot_id=snapshot_id,
        name=name,
        collaborative=collaborative,
        public=public,
        total_duration=total_duration,
        average_track_length=average_track_length,
        # number_of_tracks=number_of_tracks,
    )

    pl.save()
    print("Playlist saved")

# Calculate Total Playlist Duration in Seconds
def calculate_total_duration(tracks): 
    total_duration = (
        sum(
            item["track"]["duration_ms"] for item in tracks if item["track"] is not None
        )
    ) / 1000
    return total_duration

# Calculate Average track Length
def calculate_average_track_length(total_duration, number_of_tracks):
        if total_duration:
            average_track_length = int(round(total_duration / number_of_tracks, 0))
            print(average_track_length)
        else:
            average_track_length = None
        return average_track_length