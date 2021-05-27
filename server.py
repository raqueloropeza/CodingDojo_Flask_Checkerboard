from flask import Flask, render_template

#index route displays 8 by 8 checkerboard
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html', rows=8, columns=8)

#integer passed will display rows for checkerboard specified in url
@app.route('/<int:rows>')
def onlyRows(rows):
    return render_template('index.html', rows=rows, columns=8)

#integers passed in url will display rows and columns for checkerboard specified in route
@app.route('/<int:rows>/<int:columns>')
def rowsAndColumns(rows, columns):
    return render_template('index.html', rows=rows, columns=columns)

if __name__=="__main__":
    app.run(debug=True)