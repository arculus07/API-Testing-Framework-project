# API Testing Framework

Hi! I'm Ayush, an AI/ML student, and this is my API testing project built to apply for a role at Cred. I created this in just 6 hours to show I can learn fast and tackle new challenges, even though my background is in machine learning. This project tests a public API using Python, and I’m excited to share what I’ve done!

## What This Project Is About
This is a simple testing framework that checks if a public API (JSONPlaceholder) works correctly. I used Python, `requests`, and `pytest` to write automated tests that make sure the API handles requests like fetching data, creating posts, and dealing with errors. I also added a CI/CD pipeline with GitHub Actions to run tests automatically and tried Postman to test the API manually.

## Why I Built This (Instead of Using My ML Project)
I originally wanted to add testing to my Seed Quality Analysis project, which uses machine learning to classify soybean images. That project shows my Python and problem-solving skills, but it’s not focused on software testing, which Cred’s job needs. Integrating testing into it (like adding unit tests or an API) would’ve taken too long and felt forced, especially with only 6 hours.

So, I decided to create this new project because:
- It directly matches Cred’s requirements: writing automated tests, working with APIs, using Python, and setting up CI/CD.
- It’s simpler and faster to build from scratch, letting me focus on testing without ML complexity.
- As a beginner in testing, I could learn tools like `pytest` and GitHub Actions quickly and show my potential.

This was a risk—I’m an ML student, not a testing expert—but I wanted to prove I can adapt and learn for Cred’s role.

## What the Project Does
- **Automated Tests**: Tests the JSONPlaceholder API (https://jsonplaceholder.typicode.com/) for:
  - **GET**: Fetching lists of posts or a single post by ID.
  - **POST**: Creating new posts with valid and invalid data.
  - **Edge Cases**: Handling errors like invalid IDs (e.g., post #999).
- **Reusable Code**: Organized tests in a clean structure for easy maintenance.
- **CI/CD**: Uses GitHub Actions to run tests automatically whenever I push code.
- **Manual Testing**: I tried Postman to test the API by hand, checking responses myself.
- **Validation**: Checks status codes (e.g., 200 for success, 404 for errors) and JSON data.

## How to Set It Up
Want to try it? Here’s how to run the project on your computer:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/api-testing-cred
   cd api-testing-cred
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Tests**:
   ```bash
   pytest tests/
   ```
   You should see something like “5 passed” if all tests work!

## What I Learned
Building this in 6 hours was intense but fun! As an ML student, I’m used to coding models, not tests, so this was new. Here’s what I got out of it:
- **Testing Basics**: Learned how `pytest` makes it easy to write and run automated tests.
- **APIs**: Got hands-on with APIs, seeing how they handle requests and errors.
- **CI/CD**: Set up GitHub Actions for the first time, which was cool to see tests run automatically.
- **Time Management**: Pulled this off under pressure, showing I can learn fast.
- **Passion**: Even though testing is new to me, I loved solving problems and want to keep learning!

I also have an ML project (Seed Quality Analysis) that shows my Python and analytical skills, which I mentioned in my CV to give a full picture of what I can do.

## Contact Me
- **Email**: ranjanayush918@gmail.com

[//]: # (- **GitHub**: https://github.com/<your-username>)

Thanks for checking out my project! I’m excited about Cred’s mission and hope to bring my learning mindset to your team. Let me know if you have questions!