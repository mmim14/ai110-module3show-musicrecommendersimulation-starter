# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

The program takes in a list of songs with attributes like genre, mood, energy, temp, valence, etc and uses content-based filtering to recommend music.  

I paraphrased how Claude Code explained recommendation system. 

Recommendation techniques:
	1. Collaborative Recommendation: (behavioral signals) find users with similar interest and recommend what they enjoyed; 
		- item-based: uses what users liked before, etc. Uses matrix factorization (SVD, ALS) to find latent patterns in user-item interaction matrices 
	2. Content-Based Filtering: analyzes the content like audio features (tempo, key, energy, valence), metadata (artist, genre, release year, lyrics sentiment), video signals (thumbnails, transcripts, watch duration)

I will prioritze content-based filtering because it's music recommendation system and the attributes of songs matters most. 

---

## How The System Works

Explain your design in plain language.

The program will take in a list of songs as csv file and score the songs using a scoring rule and build a list of songs to recommend based on ranking rules.  


Some prompts to answer:

- What features does each `Song` use in your system
  - I will be using genre, mood, energy, and acousticness as features and content-based filtering to recommend songs
- What information does your `UserProfile` store
  - It will store the songs they listened to fully, what they liked, and the genre they chose
- How does your `Recommender` compute a score for each song
  - This is recommended by Claude Code:
    - score = genre_match (0 or 1)          × 2.0   ← binary, high weight
      + mood_match  (0 or 1)          × 1.5
      + energy_closeness              × 1.0   ← 1 - |user.target_energy - song.energy|
      + acoustic_match                × 0.5   ← if likes_acoustic and acousticness > 0.6
    , and I think it's a very good scoring system except I will increase the acoustic_match score to 1 because I find myself to care about if a song is acoustic or not a lot. My accoustic scorin system,
      score = genre_match (0 or 1)          × 2.0   ← binary, high weight
      + mood_match  (0 or 1)          × 1.5
      + energy_closeness              × 1.0   ← 1 - |user.target_energy - song.energy|
      + acoustic_match                × 1.0   ← if likes_acoustic and acousticness > 0.6
- How do you choose which songs to recommend
  - I'm going to randomly select out of top 3 to add variance. 
You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

