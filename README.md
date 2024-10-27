# Habit Tracker

A simple habit tracker application built using Flask, where users can add daily habits, mark them as completed, and track missed habits.

## Features

- Add new daily habits.
- Mark habits as completed.
- View habits for a specific date.
- Track missed habits if they are not completed on their specified date.

## Technologies Used

- **Backend:** Flask (Python)
- **Database:** MongoDB (assumed based on your code)
- **Frontend:** HTML, CSS (Assumed from `index.html` and `add_habit.html`)
- **Containerization:** Docker
- **CI/CD:** Jenkins

## Installation

### Prerequisites

- Python 3.x
- MongoDB
- Virtualenv (optional but recommended)
- Docker (for containerization)

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Sachinsharmak/Habit-Tracker-App.git
    cd Habit-Tracker-App
    ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up MongoDB**

    Ensure MongoDB is running on your machine. If you don't have it installed, follow the [MongoDB installation guide](https://docs.mongodb.com/manual/installation/).

5. **Configure Environment Variables**

    Create a `.env` file in the root directory with the following content:

    ```env
    FLASK_ENV=development
    FLASK_APP=app.py
    MONGO_URI=mongodb://localhost:27017/habit_tracker
    ```

    Adjust the `MONGO_URI` if your MongoDB setup is different.

## Running the Application

1. **Start the Flask Application**

    ```bash
    flask run
    ```

2. **Access the Application**

    Open your browser and go to [http://localhost:5000](http://localhost:5000).

## Docker Integration

1. **Build the Docker Image**

    ```bash
    docker build -t sachin8927/habit-tracker .
    ```

2. **Run the Docker Container**

    ```bash
    docker run -p 5000:5000 sachin8927/habit-tracker
    ```

    Access the application at [http://localhost:5000](http://localhost:5000).

## CI/CD with Jenkins

The project uses Jenkins for continuous integration and deployment. The Jenkins pipeline includes the following stages:

1. **Checkout:** Clones the repository.
2. **Build:** Builds the Docker image.
3. **Test:** Runs tests (not yet implemented).
4. **Push to DockerHub:** Pushes the Docker image to DockerHub (requires valid DockerHub credentials).
5. **Deploy:** Success.

Make sure to configure Jenkins with valid DockerHub credentials for successful deployment.

## Usage

- **Home Page:** View and manage habits for the selected date.
- **Add Habit:** Use the form to add a new habit with a specified date.
- **Complete Habit:** Mark a habit as completed using the provided form.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
