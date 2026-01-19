import pandas as pd
from flask import Flask, render_template, request,jsonify
import openai
from googlesearch import search
import logging
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
def load_data(filepath):
    # Ensure proper loading
    df = pd.read_csv(filepath)
    logging.info(f"DataFrame loaded with columns: {df.columns.tolist()}")
    return df

def get_recommendations(df, percentage, selected_program, background_education):
    # Extracting minimum score required for the program
    df['Minimum_Score_Required'] = df['Criteria_of_Admission'].str.extract('(\d+)').astype(float)

    # Filter for specific programs based on background and percentage
    specific_program_matches = df[(df['Minimum_Score_Required'] <= percentage) &
                                  (df['Program'] == selected_program) &
                                  (df['background_education'].str.contains(background_education, case=False, na=False))]

    # Filter for any program where the user's score meets or exceeds the minimum requirement
    general_matches = df[df['Minimum_Score_Required'] <= percentage]

    # Convert results to HTML format
    if specific_program_matches.empty:
        specific_program_html = "<p>No specific program matches found that match your criteria.</p>"
    else:
        specific_program_html = "<h3>Specific Program Recommendations</h3>"
        specific_program_html += specific_program_matches[['University_Name', 'Program', 'Degree_Level', 'Minimum_Score_Required', 'background_education']].to_html(index=False)

    if general_matches.empty:
        general_html = "<p>No general university matches found where your score meets the minimum requirements.</p>"
    else:
        general_html = "<h3>You can also get admission here</h3>"
        general_html += general_matches[['University_Name', 'Program', 'Degree_Level', 'Minimum_Score_Required']].to_html(index=False)

    return specific_program_html, general_html



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        percentage = float(request.form.get("percentage"))
        selected_program = request.form.get("selected_program")
        background_education = request.form.get("background_education")
        dataframe = load_data('model/updated.csv')
        
        # Get both specific and general recommendations
        specific_recommendations, general_recommendations = get_recommendations(dataframe, percentage, selected_program, background_education)
        
        # Pass both results to the template
        return render_template("result.html", specific_recommendations=specific_recommendations, general_recommendations=general_recommendations)
    return render_template("form.html")



@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message']

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure this is a chat model
            messages=[
                {"role": "user", "content": user_message}
            ],
        )
        gpt_response = response.choices[0].message['content'].strip()

        # Example condition to trigger a Google search
        if "As of my last update" in gpt_response:
            # Perform a Google search and return the first result
            for j in search(user_message, num=1, stop=1):
                return jsonify({"response": j})
        else:
            return jsonify({"response": gpt_response})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
