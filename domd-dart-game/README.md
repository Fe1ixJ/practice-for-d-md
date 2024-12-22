# README.md

# Dömd Dart Game

## Overview
Dömd is a Python-based dart game application that allows users to input scores and simulates an opponent at different levels of difficulty. The game is designed to provide a fun and interactive experience for dart enthusiasts.

## Features
- User score input
- Opponent simulation with varying difficulty levels
- Score calculation and display

## Project Structure
```
domd-dart-game
├── src
│   ├── main.py          # Entry point of the application
│   ├── game             # Game logic and classes
│   │   ├── __init__.py
│   │   ├── player.py    # Player class for managing player attributes and scores
│   │   ├── opponent.py   # Opponent class for simulating an opponent
│   │   └── scoring.py    # Scoring class for score calculations
│   ├── tests            # Unit tests for the application
│   │   ├── __init__.py
│   │   ├── test_player.py # Tests for Player class
│   │   ├── test_opponent.py # Tests for Opponent class
│   │   └── test_scoring.py  # Tests for Scoring class
│   └── utils            # Utility functions and constants
│       ├── __init__.py
│       └── constants.py  # Constants used throughout the application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd domd-dart-game
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To start the game, run the following command:
```
python src/main.py
```

## Game Rules
- Players take turns to input their scores.
- The opponent will simulate scores based on the selected difficulty level.
- The game continues until a predetermined score is reached.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.