import datetime
import uuid
from flask import Blueprint, request, redirect, url_for, render_template, current_app

# Define a Blueprint for the habits functionality
pages = Blueprint(
    "habits", __name__, template_folder="templates", static_folder="static"
)

# Context processor to add a date range helper to templates
@pages.context_processor
def add_calc_date_range():
    def date_range(start: datetime.datetime):
        """Generate a list of dates around the specified start date."""
        return [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]

    return {"date_range": date_range}

def today_at_midnight() -> datetime.datetime:
    """Return the current date at midnight."""
    today = datetime.datetime.today()
    return datetime.datetime(today.year, today.month, today.day)

@pages.route("/")
def index():
    """Render the homepage with habits and completions for the selected date."""
    date_str = request.args.get("date")
    try:
        selected_date = datetime.datetime.fromisoformat(date_str) if date_str else today_at_midnight()
    except ValueError:
        # If date_str is invalid, fall back to today
        selected_date = today_at_midnight()

    habits_on_date = current_app.db.habits.find({"added": {"$lte": selected_date}})
    completions = [
        habit["habit"]
        for habit in current_app.db.completions.find({"date": selected_date})
    ]

    return render_template(
        "index.html",
        habits=habits_on_date,
        selected_date=selected_date,
        completions=completions,
        title="Habit Tracker - Home",
    )

@pages.route("/complete", methods=["POST"])
def complete():
    """Mark a habit as completed for the given date."""
    date_string = request.form.get("date")
    habit_id = request.form.get("habitId")

    try:
        date = datetime.datetime.fromisoformat(date_string)
    except ValueError:
        # Handle invalid date formats gracefully
        return redirect(url_for("habits.index"))

    if habit_id:
        current_app.db.completions.insert_one({"date": date, "habit": habit_id})

    return redirect(url_for("habits.index", date=date_string))

@pages.route("/add", methods=["GET", "POST"])
def add_habit():
    """Render a form to add a new habit or handle form submission."""
    today = today_at_midnight()
    if request.method == "POST":
        habit_name = request.form.get("habit")
        if habit_name:
            current_app.db.habits.insert_one(
                {"_id": uuid.uuid4().hex, "added": today, "name": habit_name}
            )
        return redirect(url_for("habits.index", date=today.isoformat()))

    return render_template(
        "add_habit.html",
        title="Habit Tracker - Add Habit",
        selected_date=today
    )
