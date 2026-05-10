from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample User
user = {
    "name": "Vaishnavi",
    "bio": "Python Developer"
}

# Posts Data
posts = [
    {
        "id": 1,
        "content": "Welcome to my social media app!",
        "likes": 0,
        "comments": []
    }
]

followers = 10

# Home Page
@app.route('/')
def home():
    return render_template(
        'index.html',
        posts=posts,
        followers=followers
    )

# Profile Page
@app.route('/profile')
def profile():
    return render_template(
        'profile.html',
        user=user
    )

# Create Post
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():

    if request.method == 'POST':

        content = request.form['content']

        new_post = {
            "id": len(posts) + 1,
            "content": content,
            "likes": 0,
            "comments": []
        }

        posts.append(new_post)

        return redirect('/')

    return render_template('create_post.html')

# Like Post
@app.route('/like/<int:id>')
def like(id):

    for post in posts:
        if post["id"] == id:
            post["likes"] += 1

    return redirect('/')

# Add Comment
@app.route('/comment/<int:id>', methods=['POST'])
def comment(id):

    comment_text = request.form['comment']

    for post in posts:
        if post["id"] == id:
            post["comments"].append(comment_text)

    return redirect('/')

# Followers Page
@app.route('/followers')
def follower_page():
    return render_template(
        'followers.html',
        followers=followers
    )

if __name__ == '__main__':
    app.run(debug=True)