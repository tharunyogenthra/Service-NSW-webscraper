import PySimpleGUI as sg

#sg.theme_previewer()
sg.theme("Reddit")

locations = [
    'Albury',
    'Armidale',
    'Auburn',
    'Ballina',
    'Bankstown',
    'Batemans Bay',
    'Bathurst',
    'Bega',
    'Blacktown',
    'Blue Mountains',
    'Bondi Junction',
    'Botany',
    'Broken Hill',
    'Brookvale',
    'Burwood',
    'Casino',
    'Castle Hill',
    'Cessnock',
    'Chatswood',
    'Coffs Harbour',
    'Cooma',
    'Cootamundra',
    'Corrimal',
    'Cowra',
    'Deniliquin',
    'Dubbo',
    'Eden',
    'Engadine',
    'Erina',
    'Finley',
    'Forbes',
    'Glen Innes',
    'Gosford',
    'Goulburn',
    'Grafton',
    'Griffith',
    'Gunnedah',
    'Hay',
    'Haymarket',
    'Hornsby',
    'Hurstville',
    'Inverell',
    'Kempsey',
    'Kiama',
    'Leeton',
    'Lightning Ridge',
    'Lismore',
    'Lithgow',
    'Liverpool',
    'Macarthur',
    'Maclean',
    'Maitland',
    'Marrickville',
    'Miranda',
    'Mittagong',
    'Moree',
    'Moruya',
    'Mount Druitt',
    'Mudgee',
    'Murwillumbah',
    'Muswellbrook',
    'Nambucca Heads',
    'Narooma',
    'Narrabri',
    'Narrandera',
    'Nelson Bay',
    'Newcastle',
    'Nowra',
    'Nyngan',
    'Orange',
    'Parkes',
    'Parramatta',
    'Penrith',
    'Port Macquarie',
    'Queanbeyan',
    'Raymond Terrace',
    'Revesby',
    'Richmond',
    'Rockdale',
    'Roselands',
    'Ryde',
    'Silverwater',
    'Singleton',
    'Springwood',
    'Tamworth',
    'Taree',
    'Tenterfield',
    'Toronto',
    'Toukley',
    'Tuggerah',
    'Tumut',
    'Tuncurry',
    'Tweed Heads',
    'Ulladulla',
    'Wagga Wagga',
    'Walgett',
    'Wallsend',
    'Warners Bay',
    'Warrawong',
    'Warriewood',
    'Wauchope',
    'Wellington',
    'Wentworth',
    'West Wyalong',
    'Wetherill Park',
    'Wollongong',
    'Wynyard',
    'Yass',
    'Young'
]

layout = [
    [sg.Text('Name')],
    [sg.Input(key='-INPUT1-', enable_events=True, size = (40, 1))],
    [sg.Text('Booking No')],
    [sg.Input(key='-INPUT2-', enable_events=True, size=(40, 1))],
    [sg.Text('Select Locations')],
    [sg.Input("Search here", do_not_clear=True, size=(40,1),enable_events=True, key='_INPUT_')],
    [sg.Listbox(locations, size=(40, 15), enable_events=True, key='_LIST_')],
    [sg.Button('Submit', key = "-SUBMIT-"), sg.Button('Exit', key = "-EXIT-")]
]

window = sg.Window('Driving thingy', layout)

selectedLocations = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-EXIT-":
        break
    if event == "-SUBMIT-":
        surname = values["-INPUT1-"]
        bookingID = values["-INPUT2-"]
        #print(a,b)
        window.close()
        break

    if values['_INPUT_'] != '':                         # if a keystroke entered in search field
        search = values['_INPUT_']
        if search != "Search here":
            new_values = [x for x in locations if search.lower() in x.lower()]  # do the filtering
            window.Element('_LIST_').Update(new_values)     # display in the listbox
    else:
        window.Element('_LIST_').Update(locations)          # display original unfiltered list
    if event == '_LIST_' and len(values['_LIST_']):     # if a list item is chosen
        location = (values['_LIST_'])
        if location[0] not in selectedLocations:
            selectedLocations.append(location[0])

