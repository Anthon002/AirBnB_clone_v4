

from models import storage
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from os import environ
import uuid
from flask import Flask, render_template
app = Flask(__name__)



@app.teardown_appcontext
def close_db(error):
    """ closes sql alchemy """
    storage.close()


@app.route('/3-hbnb/', strict_slashes=False)
def hbnb():
    """making flask dynamic """
    _sts = storage.all(State).values()
    _sts = sorted(_sts, key=lambda k: k.name)
    st_ct = []

    for state in _sts:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    _amnties = storage.all(Amenity).values()
    _amnties = sorted(_amnties, key=lambda k: k.name)

    _plcs = storage.all(Place).values()
    _plcs = sorted(_plcs, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=_amnties,
                           places=_plcs,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Entry function"""
    app.run(host='0.0.0.0', port=5001)