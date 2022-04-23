from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Col
from requests import post

System.Clear()
System.Title("ByLinks")
System.Size(140, 40)

banner = r"""
            _,.-------------.._
         ,-'        j          `-.
       ,'        .-'               `.
      /          |                   '
     /         ,-'                    `
    .         j                         \
   .          |                          \
   : ._       |   _....._                 .
   |   -.     L-''       `.               :
   | `.  \  .'             `.             |
  /.\  `, Y'                 :           ,|
 /.  :  | \                  |         ,' |
\.    " :  `\                |      ,--   |
 \    .'     '-..___,..      |    _/      :
  \  `.      ___   ...._     '-../        '
.-'    \    /| \_/ | | |      ,'         /
|       `--' |    '' |'|     /         .'
|            |      /. |    /       _,'
|-.-.....__..|     |   `...:...--'''
|_|_|_L.L.T._/     |
\_|_|_L.T-''/      |
 |                /
/             _.-'
:         _..'
\__...--''   
"""[1:]

Anime.Fade(Center.Center(banner), Colors.rainbow, Colorate.Vertical, enter=True)

def bypassLink(link):
    try:
        response = post("https://api.bypass.vip/", data={"url": link}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if response.status_code != 200:
            input(Col.red + response.json()["response"] + Col.white)
            exit()
    except:
            input(Col.red + "Error! API is maybe down."+ Col.white)
            exit()
    
    Write.Print(f"""Successfully bypassed link in {response.json()["time_ms"]}ms\n""", Colors.green_to_white, interval=0.005)
    Write.Print(f"""Bypassed link: {response.json()["destination"]}\n""", Colors.white_to_green, interval=0.005)
    input()


def main():
        BYPASS_LINK = Write.Input("Le lien du site que vous voulez bypass > ", Colors.white_to_green, interval=0.005)
        bypassLink(BYPASS_LINK)
        return exit()

if __name__ == '__main__':
    while True:
        main()