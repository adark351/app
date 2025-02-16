from flask import Flask ,render_template , request
import pandas as pd  
import joblib
import numpy as np
from model import model , predict
one_df=pd.read_csv('one.csv' )
df = pd.DataFrame([[0, 0, 0, 0, 0, 0]], columns=['Total Price', 'usage_Basic', 'usage_Entertainment', 'usage_Gaming', 'usage_High Performance', 'usage_Productivity'])

# Create a Flask app instance
app = Flask(__name__)
#import model
# model=joblib.load("model.joblib")
# Define a route and a view function
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/build')
def build():
    return render_template('build.html')
@app.route('/display')
def dispaly():
    return render_template('display.html')
@app.route('/update', methods=['POST'])
def update_data():
     df = pd.DataFrame([[0, 0, 0, 0, 0, 0]], columns=['Total Price', 'usage_Basic', 'usage_Entertainment', 'usage_Gaming', 'usage_High Performance', 'usage_Productivity'])
     lower = request.form['lower']
     upper = request.form['upper']
     usage = request.form['usage']
     # Set all usage columns to 0
     df[['usage_Basic', 'usage_Entertainment', 'usage_Gaming', 'usage_High Performance', 'usage_Productivity']] = 0
     # Set the selected usage column to 1
     df['usage_' + usage] = 1
     df['Total Price']=(int(lower)+int(upper))/2
     df1=predict(df)
     df1=df1.drop(['Unnamed: 0','CPU_speed','CPU_coreCount',	'CPU_threadCount',	'CPU_power' , 'CPU_core_count'	,'CPU_core_clock'	,'CPU_boost_clock' ,'Memory_speed/0'	,'Memory_speed/1'	,'Memory_modules/0'	,'Memory_modules/1', 'Motherboard_socket' ,'PowerSupply_wattage' ,'GPU_memory'	,'GPU_core_clock','GPU_boost_clock', 'usage_Basic',	'usage_Entertainment',	'usage_Gaming'	,'usage_High Performance'	,'usage_Productivity'],axis=1 )
     
     return render_template('display.html', tables=[df1.to_html(classes='data', header="true" , index=False)], lower=lower, upper=upper)

# Run the ap

if __name__ == '__main__':
   app.run(debug=True)