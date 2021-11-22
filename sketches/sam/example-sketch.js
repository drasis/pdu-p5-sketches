const canvasWidth = 750;
const canvasHeight = 500;

function setup() {
	createCanvas(canvasWidth, canvasHeight);
}

function draw() {
	background("springgreen");
	let x = width/2 * (1 + sin(.01 * frameCount));
	circle(x, height/2, 100, 100);
}