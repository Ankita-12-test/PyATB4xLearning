def add_ui_before_and_after(func):

    def ui():
        print("Start the browser")
        print("ready to run ui")
        func()
        print("stop the ui")
        print("close the browser")
    return ui()

@add_ui_before_and_after
def run_ui():
    print("Run the ui")

@add_ui_before_and_after
def check():
    print("check everything workking fine")