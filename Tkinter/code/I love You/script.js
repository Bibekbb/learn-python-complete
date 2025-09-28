// const canvas = document.getElementById("neonCanvas");
// const ctx = canvas.getContext("2d");

// canvas.width = window.innerWidth;
// canvas.height = window.innerHeight;

// function drawArc(x, y, r, start, end, color, glow) {
//   ctx.beginPath();
//   ctx.arc(x, y, r, start, end);
//   ctx.strokeStyle = color;
//   ctx.shadowColor = color;
//   ctx.shadowBlur = glow;
//   ctx.lineWidth = 5;
//   ctx.stroke();
// }

// function animate() {
//   ctx.clearRect(0, 0, canvas.width, canvas.height);

//   const time = Date.now() * 0.002;

//   drawArc(canvas.width / 2 - 100, canvas.height / 2 - 150, 80, Math.PI, Math.PI * 2, "#00f0ff", 20);
//   drawArc(canvas.width / 2 + 100, canvas.height / 2 + 150, 80, Math.PI * 1.5, Math.PI * 2, "#ff00c8", 20);

//   requestAnimationFrame(animate);
// }

// animate();
