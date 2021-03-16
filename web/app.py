# ------------------------------------------------
# Program by Sergii Sokolov
#
#
# Version      Date           Info
# 1.0          17-Mar-2021    Initial Version
#
# ----------------------------------------------
from flask import Flask, request, render_template
import random

application = Flask(__name__)

images = [
  "https://img.buzzfeed.com/buzzfeed-static/static/2020-01/22/22/asset/de71054fd8a6/sub-buzz-1858-1579731628-8.jpg?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2020-01/23/0/asset/dff4b266d51f/sub-buzz-1980-1579740441-1.png?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-12/4/16/asset/79b290eb361c/sub-buzz-108-1575477628-4.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-10/9/14/asset/043617b3dae4/sub-buzz-4171-1570633017-1.jpg?downsize=600:*&output-format=auto&output-quality=auto", 
  "https://img.buzzfeed.com/buzzfeed-static/static/2018-04/18/17/asset/buzzfeed-prod-web-06/sub-buzz-20002-1524085640-1.png?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-05/29/20/asset/buzzfeed-prod-web-01/sub-buzz-25166-1559174431-1.jpg?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-10/2/18/asset/c5e27dbd3a6b/sub-buzz-3353-1570039704-1.jpg?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-06/3/10/asset/buzzfeed-prod-web-03/sub-buzz-8276-1559573886-7.jpg?downsize=600:*&output-format=auto&output-quality=auto"
]


@application.route("/")
def index():
    url = random.choice(images)
    host = request.host
    return render_template("index.html", url=url, host=host)

@application.route("/about")
def aboutpage():
    return render_template("about.html")



if __name__ == "__main__":
    application.debug = True
    application.run()
