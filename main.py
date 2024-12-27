import PySimpleGUI as sg
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="b244e2789c7c424880c15fbc5a47f5fc",
    client_secret="0cde25f4cf9f49e1955b024519d10209",
    redirect_uri="http://localhost:6969/callback",
    scope="user-top-read"
))
cursors = sg.TKINTER_CURSORS
sg.theme('Light Blue 2')

def make_window1():
    # Create the window1
    layout = [[sg.Button("Start You Spotify Shakedown", key='Start')]]
    window = sg.Window("Spotify Shakedown", layout, finalize=True)
    window['Start'].set_cursor(cursor='hand2')
    return window


def make_window2():
    
    topArtistResults = sp.current_user_top_artists(time_range="medium_term", limit=50)
    
    topArtist = topArtistResults['items'][0]
    secondArtist = topArtistResults['items'][1]
    thirdArtist = topArtistResults['items'][2]
    
    topArtistName = topArtist['name']
    secondArtistName = secondArtist['name']
    thirdArtistName = thirdArtist['name']

    layout = [[sg.Text('Your Top Artists')],
               [sg.Text("1 " + topArtistName)],
               [sg.Text("2 " + secondArtistName)],
               [sg.Text("3 " + thirdArtistName)],
               [sg.Button('< Prev'), sg.Button('Next >')]]

    return sg.Window('Artists', layout, finalize=True)


def make_window3():
    topSongResults = sp.current_user_top_tracks(time_range="medium_term", limit=50)

    topSong = topSongResults['items'][0]
    secondSong = topSongResults['items'][1]
    thirdSong = topSongResults['items'][2]

    topSongName = topSong['name']
    secondSongName = secondSong['name']
    thirdSongName = thirdSong['name']

    topSongArtist = ", ".join(artist['name'] for artist in topSong['artists'])
    secondSongArtist = ", ".join(artist['name'] for artist in secondSong['artists'])
    thirdSongArtist = ", ".join(artist['name'] for artist in thirdSong['artists'])

    layout = [[sg.Text('Your Top Songs')],
               [sg.Text("1 " + topSongName + " - " + topSongArtist)],
               [sg.Text("2 " + secondSongName + " - " + secondSongArtist)],
               [sg.Text("3 " + thirdSongName + " - " + thirdSongArtist)],
               [sg.Button('< Prev'), sg.Button('Exit')]]
    return sg.Window('Top Songs', layout, finalize=True)



window1, window2, window3 = make_window1(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
        break

    if window == window1:
        if event == "Start":
            window1.hide()
            window2 = make_window2()

    if window == window2:
        if event == 'Next >':
            window2.hide()
            window3 = make_window3()
        elif event in ('< Prev'):
            window2.close()
            window1.un_hide()
        elif event in (sg.WIN_CLOSED):
            window2.close()
            window3.close()
            window1.close()

    if window == window3:
        if event in ('< Prev'):
            window3.close()
            window2.un_hide()
        elif event in (sg.WIN_CLOSED, 'Exit'):
            window2.close()
            window3.close()
            window1.close()

window.close()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break



window.close()
