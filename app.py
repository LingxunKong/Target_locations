from keplergl import KeplerGl
import pandas as pd
from flask import Flask

data = pd.read_csv('target_stores_Aug2024.csv',index_col=0)

# Initialize a Kepler map
map_1 = KeplerGl(height=600)

# Add the DataFrame to the map
map_1.add_data(data=data, name="Target Stores")

app = Flask(__name__)

@app.route('/')
def index():
    return map_1._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)