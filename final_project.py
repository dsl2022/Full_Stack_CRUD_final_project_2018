from flask import Flask

app = Flask(__name__)



@app.route('/')
@app.route('/restaurant')
def showRestaurants():
    return "This page will show all my restaurants"

@app.route("/restaurant/new")
def newRestaurant():
    return "This page will be for making new restaurant"

@app.route("/restaurant/restaurant_id/edit")
def editRestaurant():
    return "This page will be for editing restaurant"#  %s" % restaurant_id

@app.route("/restaurant/restaurant_id/delete")
def deleteRestaurant():
    return "This page will be for deleting restaurant"# %s" % restaurant_id

@app.route("/restaurant/restaurant_id ?rstaurant/restaurant_id/menu")
def showMenu():
    return "This page is the menu for rstaurant"#  %s" % restaurant_id|

@app.route("/restaurant/restaurant_id/menu/new")

def newMenuItem():
    return "This page is for making a new menu item for restaurant"# %s" %s restaurant_id|

@app.route("/restaurant/restaurant_id/menu/menu_id")
def editMenuItem():
    return "This page is for editing menu item"#  %s" % menu_id|

@app.route("/restaurant/restaurant_id/menu/menu_id/delete")
def deleteMenuItem():
    return "This page is for deleting menu item" #  %s" % menu_id |


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)