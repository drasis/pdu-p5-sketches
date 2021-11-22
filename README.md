### Let's make stuff move around our screens!

- Today we'll be using a JavaScript library called [p5](https://p5js.org/reference/) to make some [animations](https://doronrasis.com/sketches/tri-morph.html)! Check out [@beesandbombs](https://twitter.com/beesandbombs) on Twitter for some inspiration
- p5 is based on a Java library called Processing. Java and JavaScript are totally different programming languages--weird!
- p5 is a "client-side" library. This means that the code we'll write will run in a browser (client), rather than run in some other computer that communicates with a browser (a "server").
- A lot of client-side JavaScript interacts with our web browser's "DOM" (document object model). DOM is a fancy way to say a bunch of [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) elements.
- p5 uses a different model than this. Instead of interacting with many different HTML elements, it creates a small rectangle in the DOM called a "canvas". Then it lets you do a bunch of fun stuff on that canvas.
- We are the artists, the browser is our canvas! Or something like that

### Our goals

- Get our environments set up to run our p5 sketches
- Learn about the basic structure of a p5 sketch (`setup` and `draw` functions, `frameCount`, 2D primatives, math functions)
- Make some fun animations!
- Bonus: talk about [Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise)

### Getting set up

Do you have `git` installed? If not, install it! Instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). You'll also want to install a text editor if you don't already have one ([Atom editor](https://atom.io/) is an excellent free option).

Then, give Doron your GitHub username so he can give you access to the repository. We can also decide to make this repo public, if we're all comfortable with our code living on the public web for anyone to see or use for free.

In your terminal, navigate to the directory where you want to download our p5 work (right now it's pretty small, ~500kb). Run `git clone https://github.com/drasis/pdu-p5-sketches.git`.

When you want to create a new sketch, navigate to the directory `sketches/<yourname>`, and create a file like `your-sketch-name.js` in your text editor. The only requirements for the filename are that it uses hyphens instead of spaces and ends with `.js`.

When you wanna see your sketch in action, run `python make-pages.py` from the root directory of the repository, and visit `http://localhost:8000/gallery/<yourname>` in your browser to see your work.

### Editing your sketches

Do you want to make a small tweak to your code without re-running the python script to see your change in action? There are two options:

- Check out [p5live](https://teddavis.org/p5live/), an interactive live coding environment
- Right-click on your browser when the sketch is open and click on `inspect` in the drop-down. Then click the `sources` tab, and tweak your script in `sketches/<yourname>/<script-name>.js`. The downside here is that the `setup` function won't get run again.

