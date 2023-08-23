# Run the Python script. You'll see output indicating that the Flask app is running.
# Open your web browser and navigate to http://127.0.0.1:5000/.
# You should see a simple webpage with an audio player. When you click the play button, it will fetch and play the audio file.
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Set the directory where your audio files are located
AUDIO_DIRECTORY = 'files'

@app.route('/')
def index():
    return """
    <html>
    <body>
        <h1>Music Player</h1>
        <audio controls>
            <source src="/play" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
    </body>
    </html>
    """

@app.route('/play')
def play_audio():
    audio_file = 'test.mp3'  # Replace with the name of your audio file
    return send_from_directory(AUDIO_DIRECTORY, audio_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
