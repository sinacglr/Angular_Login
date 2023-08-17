from flask import Flask
app=Flask(__name__)

def get_data():
    data = {
        'message': 'Rest Servisi',
        'status': 'success'
    }
    return data
if __name__ == '__main__':
    app.run(debug=True)
