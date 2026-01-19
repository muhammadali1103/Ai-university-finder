
# AI University Finder

**AI University Finder** is an intelligent web tool that helps students discover the best universities and departments based on their academic background, program choice, and scores. The app provides personalized recommendations for higher education and admission opportunities.

## Features

- Students enter their academic percentage, program, and background education.
- AI-powered suggestions for specific programs that match the criteria.
- General university recommendations where the student's score meets minimum requirements.
- Integration with OpenAI GPT for interactive guidance and Google search fallback.
- Preloaded database (`model/updated.csv`) with universities, departments, programs, admission criteria, and background education requirements.
- Built with Python, Flask, HTML, CSS, and Pandas.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/muhammadali1103/Ai-university-finder.git
cd "University Selection System"
````

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

> **Important:** `.env` is ignored by Git and should never be committed.

---

## Usage

Run the Flask app:

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000/` to start using the tool.

---

## Model Data (`model/updated.csv`)

The CSV contains preloaded information about universities, departments, programs, degree levels, admission criteria, and acceptable background education. Sample entries:

| University_Name | Department                       | Program                               | Degree_Level  | Criteria_of_Admission                     | background_education                              |
| --------------- | -------------------------------- | ------------------------------------- | ------------- | ----------------------------------------- | ------------------------------------------------- |
| NUML            | Faculty of English Studies       | BS English (Linguistics & Literature) | Undergraduate | Minimum 70% in Intermediate or equivalent | ICS, Pre-Engineering, Pre-Medical, Equivalent     |
| TUF             | School of Arts & Social Sciences | BS English                            | Undergraduate | Minimum 65% in Intermediate or equivalent | ICS, Pre-Engineering, Pre-Medical, Equivalent     |
| TUF             | School of Arts & Social Sciences | BS Interior Design                    | Undergraduate | Minimum 50% in Intermediate or equivalent | ICS, FA, Pre-Engineering, Pre-Medical, Equivalent |
| TUF             | School of Arts & Social Sciences | BS Graphic Design                     | Undergraduate | Minimum 50% in Intermediate or equivalent | ICS, FA, Pre-Engineering, Pre-Medical, Equivalent |
| GCUF            | Department of English            | BS English                            | Undergraduate | Minimum 60% in Intermediate or equivalent | ICS, Pre-Engineering, Pre-Medical, Equivalent     |
| GCUF            | Department of Fine Arts          | BS Fine Arts                          | Undergraduate | Minimum 45% in Intermediate or equivalent | ICS, FA, Pre-Engineering, Pre-Medical, Equivalent |
| UAF             | Department of Sociology          | BS Sociology                          | Undergraduate | Minimum 65% in Intermediate or equivalent | ICS, FA, Pre-Engineering, Pre-Medical, Equivalent |
| UAF             | Department of Education          | BS Education                          | Undergraduate | Minimum 48% in Intermediate or equivalent | ICS, FA, Pre-Engineering, Pre-Medical, Equivalent |

> This allows the AI tool to recommend universities and departments based on student input.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




