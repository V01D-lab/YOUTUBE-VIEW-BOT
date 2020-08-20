import subprocess
import webbrowser
import time


def opening_text():
    print("""
                                      hello there, my name is V01D
                      I made this program to give view (just for fucking fun)
                    I didn't make this program to harm anyone or damage anything 
     I simply made it for fun and for people to boost their videos with the shity algorithm of an application known as 

                                                  ##YOUTUBE##
     """)

    time.sleep(3)

    print("""
    #####
     I would recommend doing only small numbers at a time as this program is simply spamming new tabs of url that you input 
                              (then closing them) 15 at a time is my personal recommendation.
                                  **YOU NEED FIREFOX INSTALLED AND A WINDOWS MACHINE**
    #####
    """)

    time.sleep(3)

    print("""
                                 -------------------------------------------------
                                |  my github --> https://github.com/mohamedatheer |
                                 -------------------------------------------------
                              If you have any errors, feel free to report them on github...
    """)

    time.sleep(2)

    print("""
                                                  anyways enjoy the 'bot' 

    """)

    time.sleep(3)


opening_text()


def main():
    vid_url = input("vid URL --> ")
    num_of_views = int(input("amount of view --> "))

    def opening_web():
        webbrowser.register('firefox', None,
                            webbrowser.BackgroundBrowser("C:/Program Files/Mozilla Firefox/firefox.exe"))
        webbrowser.get('firefox').open_new_tab(vid_url)

    for i in range(num_of_views):
        opening_web()
        print(i)

    def killing_of_the_links():
        subprocess.run('TASKKILL /F /IM firefox.exe')

    kill_input = input("press enter to kill all the tabs")

    if kill_input == "":
        killing_of_the_links()
    else:
        killing_of_the_links()


main()
sid = input("do you want to restart (yes or no) --> ")

if sid == 'yes':
    main()
else:
    exit()

