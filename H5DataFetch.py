# -*- coding: utf-8 -*

import os
import glob
import hdf5_getters
import pandas as pd

basedir=".\\metadata"

def get_all_rows(basedir,ext='.h5') :
    rows = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
#            print(os.path.join(root, f))
            h5 = hdf5_getters.open_h5_file_read(f)
            num_songs=hdf5_getters.get_num_songs(h5)
#            print(num_songs)
            
            for i in range(num_songs):
                print(i)
                obj={}
                obj['artist_name']=hdf5_getters.get_artist_name(h5,i).decode('UTF-8')  
                obj['artist_familiarity']=hdf5_getters.get_artist_familiarity(h5,i)
                obj['artist_hotness']=hdf5_getters.get_artist_hotttnesss(h5,i)
                obj['artist_id']=hdf5_getters.get_artist_id(h5,i).decode('UTF-8')
#                obj['artist_mbid']=hdf5_getters.get_artist_mbid(h5,i).decode('UTF-8')
                obj['artist_playmeid']=hdf5_getters.get_artist_playmeid(h5,i)
                obj['artist_7digitalid']=hdf5_getters.get_artist_7digitalid(h5,i)
#                obj['artist_latitude']=hdf5_getters.get_artist_latitude(h5,i)
#                obj['artist_longitude']=hdf5_getters.get_artist_longitude(h5,i)
#                obj['artist_location']=hdf5_getters.get_artist_location(h5,i).decode('UTF-8')
                obj['artist_name']=hdf5_getters.get_artist_name(h5,i).decode('UTF-8')
                obj['release']=hdf5_getters.get_release(h5,i).decode('UTF-8')
                obj['song_hotttnesss']=hdf5_getters.get_song_hotttnesss(h5,i)
                obj['title']=hdf5_getters.get_title(h5,i).decode('UTF-8')
  
    #            obj['artist_terms']=hdf5_getters.get_artist_terms(h5)
#                obj['artist_terms_freq']=hdf5_getters.get_artist_terms_freq(h5)
#                obj['artist_terms_weight']=hdf5_getters.get_artist_terms_weight(h5)
    #            obj['audio_md5']=hdf5_getters.get_audio_md5(h5).decode('UTF-8')
                obj['danceability']=hdf5_getters.get_danceability(h5,i)
                obj['duration']=hdf5_getters.get_duration(h5,i)
                obj['end_of_fade_in']=hdf5_getters.get_end_of_fade_in(h5,i)
                obj['energy']=hdf5_getters.get_energy(h5,i)
                obj['key']=hdf5_getters.get_key(h5,i)
                obj['key_confidence']=hdf5_getters.get_key_confidence(h5,i)
                obj['loudness']=hdf5_getters.get_loudness(h5,i)
                obj['mode']=hdf5_getters.get_mode(h5,i)
    #            obj['start_of_fade_out']=hdf5_getters.get_start_of_fade_out(h5)
                obj['tempo']=hdf5_getters.get_tempo(h5,i)
                obj['time_signature']=hdf5_getters.get_time_signature(h5,i)
    #            obj['time_signature_confidence']=hdf5_getters.get_time_signature_confidence(h5)
                obj['track_id']=hdf5_getters.get_track_id(h5,i).decode('UTF-8')
    #            obj['segments_start']=hdf5_getters.get_segments_start(h5)
    #            obj['segments_confidence']=hdf5_getters.get_segments_confidence(h5)
    #            obj['segments_pitches']=hdf5_getters.get_segments_pitches(h5)
    #            obj['segments_timbre']=hdf5_getters.get_segments_timbre(h5)
    #            obj['segments_loudness_max']=hdf5_getters.get_segments_loudness_max(h5)
    #            obj['segments_loudness_max_time']=hdf5_getters.get_segments_loudness_max_time(h5)
    #            obj['segments_confidence']=hdf5_getters.get_segments_confidence(h5)
    #            obj['segments_loudness_start']=hdf5_getters.get_segments_loudness_start(h5)
    #            obj['sections_start']=hdf5_getters.get_sections_start(h5)
    #            obj['sections_confidence']=hdf5_getters.get_sections_confidence(h5)
    #            obj['beats_start']=hdf5_getters.get_beats_start(h5)
    #            obj['beats_confidence']=hdf5_getters.get_beats_confidence(h5)
    #            obj['bars_start']=hdf5_getters.get_bars_start(h5)
    #            obj['bars_confidence']=hdf5_getters.get_bars_confidence(h5)
    #            obj['tatums_start']=hdf5_getters.get_tatums_start(h5)
    #            obj['artist_mbtags']=hdf5_getters.get_artist_mbtags(h5)
    #            obj['artist_mbtags_count']=hdf5_getters.get_artist_mbtags_count(h5)
                obj['year']=hdf5_getters.get_year(h5,i)
                rows.append(obj)
        h5.close()
    return rows

all_titles=get_all_rows(basedir)
df=pd.DataFrame(all_titles)
df.head()
df.to_csv (r'.\export_dataframe_new.csv', index = False, header=True)


print("DONE")

#print(all_titles)
#print(len(all_titles))