#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import io
from PIL import Image
import base64


def image_file_to_bytes(image64, size):
    image_file = io.BytesIO(base64.b64decode(image64))
    img = Image.open(image_file)
    img.thumbnail(size, Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    imgbytes = bio.getvalue()
    return imgbytes


def ShowMeTheButtons():
    bcolor = ('black', 'black')
    wcolor = ('white', 'black')

    sg.ChangeLookAndFeel('Black')
    sg.SetOptions(auto_size_buttons=True, border_width=0, button_color=sg.COLOR_SYSTEM_DEFAULT)

    toolbar_buttons = [ [sg.Text('Who says Windows have to be ugly when using tkinter?', size=(45,3))],
                         [sg.Text('All of these buttons are part of the code itself', size=(45,2))],

        [sg.Button('Next', image_data=image_file_to_bytes(button64, (100,50)),button_color=wcolor, font='Any 15', pad=(0,0), key='-NEXT-'),
        # [sg.Button('Exit', image_data=image_file_to_bytes(black64, (100,50)),button_color=bcolor, font='Any 15', pad=(0,0), key='_close_'),],
        sg.Button('Submit', image_data=image_file_to_bytes(red_pill64, (100,50)),button_color=wcolor, font='Any 15', pad=(0,0), key='-SUBMIT-'),
        sg.Button('OK', image_data=image_file_to_bytes(green_pill64, (100,50)),button_color=bcolor, font='Any 15', pad=(0,0), key='-OK-'),
        sg.Button('Exit', image_data=image_file_to_bytes(orange64, (100,50)),button_color=bcolor, font='Any 15', pad=(0,0), key='-EXIT-'),],
                        ]

    # layout = toolbar_buttons
    layout =  [[sg.Frame('Nice Buttons', toolbar_buttons, font=('any 18'), background_color='black')]]

    window = sg.Window('Demo of Nice Looking Buttons', layout,
                       no_titlebar=False,
                       grab_anywhere=True,
                       keep_on_top=True,
                       use_default_focus=False,
                       font='any 15',
                       background_color='black', finalize=True)

    # ---===--- Loop taking in user input --- #
    while True:
        event, values = window.Read()
        print(event)
        if event in ('-EXIT-', None):
            break           # exit button clicked

if __name__ == '__main__':

    # To convert your PNG into Base 64:
    #   Go to https://www.base64-image.de/
    #   Drag and drop your PNG image onto the webpage
    #   Choose "Copy image"
    #   Create a string variable name to hold your image
    #   Paste data from webpage as a string
    #   Delete the "header" stuff - up to the data portion (data:image/png;base64,)
    orange64 = 'iVBORw0KGgoAAAANSUhEUgAAAiIAAADLCAMAAABkvgh7AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAANtvJ99sId5tIt5uI91tJNxuJNxuJttvKN90NN91Ntt3PN52ONx3Otx3PNt4Pdp4Ptx4PepfD+pfEOtgD+piD+tkD+ttD+dnFOdoE+doFOVoFuNqG+JrHOFrHuFsHuRpGORpGuRqGORqGupgEOpiEOpkEOlmEOhnEupoEOpoEupqFettEetsF+tuFOxqFetrGOtsGetvHOxrGOxsGOxtGuxuG+xuHexxFutwH+xxGOxyGOxyGuxxHuBsIOJvJ+NvKORvKONwKeNwKuJxLONyLeJyLuRwKeRwKuRxLOtxIexyIexzJOx0JOx1Ju11KOx2KOx2Kux5Iux4Kux5Le1/LeFyMOFzMuB0NOB1Nux7MOx8MOx8Mu19NO1+NO1+Ntd7RdV8RtN+S9J/TdF/TtV9SNR9Stl5QNl6Qdh6Qth7RK+Tfa+Tfq6Ufr+JZb+JZr+KZ7uMbr6KaL6LaryMbLyNb7yOb7WPdLuNcLqOcLmOcrmPdLOQd7SQdrKReLKRerGSerCTfLCTfrmQde2AN+2AOO2BOu2COu6DPO6EPe6EPsWDV8OFXcOFXsOGXcOGXsaDWMSEWsqCVs+AUM2AUs6CU82CVMqDWMmEWtCAT9CAUMKHYMCIYsCIZMCKZu6FQO6GQe6GQu6HRO6IRe6JRu6KR+6KSO+LSu+MS++MTO+OTe+OTu+OUO+RUu+TVfCNTvCOTvCPUPCQUfCQUvCSU/CRVPCSVPCSVvCUV/CUWPCVWvGWWvGXXPGYXvCWYPGaYfGcYvGcZPKdZvKeZ/GdavKeaPKebfKebvKgavKhbPKibfGibvKjcPGkcfKmdPKiePOod/OpePSpePSqevSrfPSsfPSsfvSqg/SugfWwgvWwhPWyhfWyhvWxi/Wyj/W0ifW2jfa4j/a1kPW2kva2lfW2lvW4kPa6kfa7kva5lvW7lPa8lPW8lve+l/a4mva5nPa6nPa7nva+mPa+mva/nPa8oPa9ovbAm/bAnfXAnvbCofbEo/XGp/bGqPbIqQAAAC/NnaUAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGHRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjFjKpxLAAAJXElEQVR4Xu3de3zVdR3H8Xb9/sJh60LlOTtubdIZEyckSdedMzkdZyRGIePmZdqki8s0KllJmtGCTAXRlUAyrireUeZga2JRkooYRWR0JbXMLsIqZ5fT7/L5nRvj9/md0/fhw/Px/fyHP+D33fb4vPj+LvsxXpMA8IREgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgJF7Ih1Xf3bVsuu/AYXu+mUrL+u8iqbqIcdErvhme0V8SjQCIpwWe+0nli+k2R5NTolc0jYzqpQBcigV+UDltZ57SQ6JfLqyRRXRyiCIis7u7qAhj8B3Ip1tLdg/pFLR0Z+hOR/JbyIrWxGIZCp289E2Ep+J3HzEFqLKy0qhUJUfeUkZnf8lGnYWX4l0tDfTOg5VEqoJNNTXh6EgmaMLBKuaymmcJFLRSfPO5CuRtgitYisPBehDQUFrqC3O2EtUxRdo4Bn8JHJhlNawlNZh85Aj2JQeiRp9JY08nY9Euk+nFUwq1ECLgww1ZTRaS+R8mnk6PpEF8dTDkNIgLQxiHFdNw7U0d9PU07CJdLw+tRUVpy5Cxo19+bz9lYI+n5cNfdhcjWGZf2jsCTTJcDiUmnBR/HKaewqbSHfqQqSJrkLGvuuctZu3jOgBD1u99B7Fg6a+Vwrrk8kNfRX+0XE2+qg527adsc38M723d01yK3lbqhH1SZp7CpfIolnJw4udQk44ddPOn/3q6b+M6K8+/c2vF+jXVw29X/ALI7N+Z3jome+f/QZ7pOG6VCMtl9Dkk7hElifvd0uPs1cb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'

    green_pill64 = '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'

    red_pill64 = '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'

    button64 = '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'

    ShowMeTheButtons()

