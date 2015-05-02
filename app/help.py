from webbrowser import open


def show_help():

    try:
        # This open function is from the module 'webbroswer'
        open("http://www.napcorps.com/")
    except Exception as e:
        print(e)
