#!/usr/bin/python3
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)



@app.teardown_appcontext
def close_db(error):
    """ This will close SQLAlchemy Sessions """
    storage.close()


@app.route('/1-hbnb/', strict_slashes=False)
def hbnb():
    """ Making amenities dynamic """
    sts_value = storage.all(State).values()
    sts_value = sorted(sts_value, key=lambda k: k.name)
    sts_list = []

    for state in sts_value:
        sts_list.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenty_values = storage.all(Amenity).values()
    amenty_values = sorted(amenty_values, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=sts_list,
                           amenities=amenty_values,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)