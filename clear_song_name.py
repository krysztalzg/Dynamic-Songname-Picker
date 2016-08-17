import re


def clear_song_name(song):
    song = song.replace('&apos;', '\'')
    song = song.replace('&amp;', '&')
    song = song.replace('- Lyrics', '')

    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*official[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*official video[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*official trailer[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*official teaser[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*official version[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*official music video[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*official lyrics video[\\s]*[\])]', '', song)

    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*lyrics[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*lyrics video[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*with lyrics', '', song)
    song = re.sub(r'(?i)[\\s]*-[\\s]*lyrics[\\s]*-', '', song)

    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*original[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*original video[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*original music video[\\s]*[\])]', '', song)

    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*uncensored[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*audio[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*full[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*full album[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*remastered[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*[a-z]* remix[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*[a-z]* cover[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*oficjalny klip[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*deluxe[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*deluxe edition[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*acoustic[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*acoutsic session[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*HD/HQ Lyrics in Video[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*music video[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*[a-z\\s]*live[a-z\\s]*[\\s]*[\])]', '', song)
    song = re.sub(r'(?i)[\\s]*M/V', '', song)

    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*hd 720p[\\s]*[\])][\\s]*', ' ', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*hd[\\s]*[\])][\\s]*', ' ', song)
    song = re.sub(r' HD', ' ', song)
    song = re.sub(r'(?i) long version', ' ', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*hq[\\s]*[\])][\\s]*', ' ', song)
    song = re.sub(r'(?i)[\\s]*[\[(][\\s]*good quality[\\s]*[\])][\\s]*', ' ', song)
    song = re.sub(r'(?i) good quality', ' ', song)

    return song
