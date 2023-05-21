<!DOCTYPE html>
<html>
<head>
    <title>🚀 Space Adventure with Python Turtle 🐢</title>
    <style>
        body {
            background-color: #0D0221;
            color: #66FCF1;
            font-family: 'Courier New', Courier, monospace;
        }
        h1, h2, h3 {
            color: #45A29E;
        }
        details {
            background-color: #1F2833;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        pre {
            background-color: #0B0C10;
            color: #C5C6C7;
            padding: 10px;
            border-radius: 5px;
        }
        code {
            color: #66FCF1;
        }
    </style>
</head>
<body>

<h1>🚀💥 Space Adventure with Python Turtle 🐢</h1>

<p>Hello, young coder! 👋👾 Are you ready for an exciting journey to create a beautiful space scene using Python? </p>

<h2>🎯 Objective</h2>

<p>Your mission is to create a <strong>Space Adventure</strong> using Python's turtle module. You will draw a night sky filled with stars 🌠, a beautiful planet 🌍, and a spaceship 🛸 ready for a journey into the unknown!</p>

<h2>🧰 What You Need</h2>

<ol>
    <li>Python installed on your computer 🐍</li>
    <li>A code editor like VSCode, Atom, or Sublime Text 💻</li>
    <li>Excitement to learn and code! 🔥💡</li>
</ol>

<h2>📝 Instructions</h2>

<h3>1. Set Up Your Project 🌟💻</h3>

<p>Create a new Python file and call it `space_adventure.py`.</p>

<p>Import the turtle module like so:</p>

<details>
<summary>Click for Hint</summary>

<pre><code>import turtle
# create a new turtle
space_turtle = turtle.Turtle()
</code></pre>

</details>

<h3>2. Draw Stars in the Sky 🌠🌌</h3>

<p>We'll start by painting the canvas black, setting our turtle color to white, and creating a bunch of stars.</p>

<details>
<summary>Click for Hint</summary>

<pre><code># function to draw a star
def draw_star(turtle, size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
</code></pre>

</details>

<p>Can you use a loop to draw multiple stars at random places?</p>

<h3>3. Draw a Planet 🌍🌑</h3>

<p>Now, let's draw a big, beautiful planet. You can choose the color!</p>

<details>
<summary>Click for Hint</summary>

<pre><code># function to draw a circle (for our planet)
def draw_planet(turtle, size, color):
    turtle.penup()
    turtle.goto(0, -size)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
</code></pre>

</details>

<h3>4. Draw a Spaceship 🚀🛸</h3>

<p>Last but not least, let's draw a spaceship ready for take-off!</p>

<details>
<summary>Click for Hint</summary>

<pre><code>def draw_spaceship(turtle, size):
    turtle.penup()
    turtle.goto(-size/2, -size*2)
    turtle.color("grey")
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(size)
        turtle.right(60)
        turtle.forward(size)
        turtle.right(120)
    turtle.right(60)
    turtle.forward(size)

    turtle.end_fill()
</code></pre>

</details>

<h3>5. Show Off Your Creation! 🖼️🎆</h3>

<p>Once you've drawn your stars, planet, and spaceship, it's time to admire your work! Complete your code with this line to hold the drawing screen open:</p>

<pre><code>turtle.done()</code></pre>

<h2>✨💫 That's It!</h2>

<p>Congrats, explorer! 🥳👏 You've just created a stunning space adventure using Python and Turtle!</p>

<p>Remember, this is your universe. You can add more stars, planets, or even a fleet of spaceships. Let your imagination run wild! 💭✨</p>

<p>Happy Coding! 🎉🎊</p>

</body>
</html>
