from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# List of possible treasure locations
locations = ["beach", "dock", "cave", "forest", "hill", 
"mountain", "valley", "river", "desert", "oasis", "village", "castle"]

@app.route('/')
def home():
    # Randomly select a treasure location
    treasure_location = random.choice(locations)
    return render_template("index.html", treasure_location=treasure_location, locations=locations)

@app.route('/guess', methods=['POST'])
def guess():
    # Get the player's guess from the form
    guess = request.form['guess'].lower()
    treasure_location = request.form['treasure_location']
    feedback = ""

    if guess == treasure_location:
        feedback = "🎉 Congratulations! You found the treasure! 🎉"
    else:
        index = locations.index(guess)
        tres_index = locations.index(treasure_location)
        
        if abs(index - tres_index) == 1:
            feedback = "🔹 You're very close!"
        elif abs(index - tres_index) == 2:
            feedback = "🔸 You're close!"
        else:
            feedback = "❌ You're not close at all!"
    
    return jsonify({'feedback': feedback})

if __name__ == "__main__":
    app.run(debug=True)
