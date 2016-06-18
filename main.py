import cherrypy
import requests, bs4

class work(object):
      //Python Web Crawler   
    @cherrypy.expose
    def generate(self):
        res = requests.get('http://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G')
    
        res.raise_for_status()
        noStarchSoup = bs4.BeautifulSoup(res.text)
        elems = noStarchSoup.select('#tab7Content')
        type(elems)
         //To modify the output keyword from Crawler,for above it's elems[0].getText()
        return """<html>   
        <head></head>
        <style> 
        p{
        color:blue;
        text-align:centre;
        }
        </style>
        <body>
        <p>elems[0].getText()</p>
    `   
        </body>
        </html>"""
        
       
   

if __name__ == '__main__':
   cherrypy.quickstart(work())