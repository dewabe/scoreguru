
### ScoreGuru – Scoring Rules and Development Environment Setup

ScoreGuru is an application that allows users to predict match results and evaluate predictions based on the following scoring system:

#### Scoring Rules
1. **Correct home team score:** +1 point  
2. **Correct away team score:** +1 point  
3. **Correctly predicting the match winner (home win, away win, or draw):** +1 point  
4. **Correctly predicting the exact draw score (e.g., 2–2):** +1 point  

In ScoreGuru, predictions are made for the **regular game time result**. If the match is decided in overtime or via penalty shootout, the result is considered a draw.

**Example:**  
- **Prediction:** Home team 4 – Away team 2  
- **Actual result:** Home team 4 – Away team 2  
  - Correct home team score: **+1 point**  
  - Correct away team score: **+1 point**  
  - Correct winner: **+1 point**  
  **Total:** 3 points  

An exact draw prediction gives an additional point, but no extra bonus points are awarded. The maximum score is 4 points.

---

### Development Environment Setup

Follow these instructions to set up the ScoreGuru application in your local development environment and initialize a league for the 2025 Ice Hockey World Championship.

#### 1. Install requirements
Ensure that you have Python 3.10 or newer installed, along with virtualenv. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

Install the required dependencies for development:

```bash
pip install -r requirements/development.txt
```

#### 2. Initialize the database
Run the following commands to initialize the database and apply migrations:

```bash
python manage.py migrate
```

#### 3. Load sample data
You can populate the development environment with sample data, including the teams and matches of the 2025 Ice Hockey World Championship. Run the following commands:

```bash
python manage.py loaddata fixtures/world_championship_2025.json
python manage.py loaddata fixtures/ww2025_games.json
```

#### 4. Start the development server
Start the local development server:

```bash
python manage.py runserver
```

Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### Getting Started with Testing

You can start testing the application as follows:
- **Create a new league:** In the application, create a new league and start entering match results.
- **Verify the scoring system:** Input match results and ensure that the application calculates the scores correctly according to the rules.

If you need additional assistance, feel free to ask! 😊
