from flask import Flask, render_template
import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

app = Flask(__name__)

@app.route('/showLineChart')
def line():
	count = 500
	xScale = np.linspace(0, 100, count)
	yScale = np.random.randn(count)

	# Create a trace
	trace = go.Scatter(
	    x = xScale,
	    y = yScale
	)

	data = [trace]
	graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
	return render_template('index.html',
	                           graphJSON=graphJSON)

@app.route('/showMultiChart')
def multiLine():
    count = 500
    xScale = np.linspace(0, 100, count)
    y0_scale = np.random.randn(count)
    y1_scale = np.random.randn(count)
    y2_scale = np.random.randn(count)

    # Create traces
    trace0 = go.Scatter(
        x = xScale,
        y = y0_scale
    )
    trace1 = go.Scatter(
        x = xScale,
        y = y1_scale
    )
    trace2 = go.Scatter(
        x = xScale,
        y = y2_scale
    )
    data = [trace0, trace1, trace2]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
                           graphJSON=graphJSON)