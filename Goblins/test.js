function drawImage(canvas, traitsCoordinates) {
    if (!canvas) {
        console.error('Canvas element not found');
        return;
    }

    const ctx = canvas.getContext('2d');
    if (!ctx) {
        console.error('Failed to get 2D rendering context for the canvas');
        return;
    }

    const size = 600;

    // Clear the canvas
    ctx.clearRect(0, 0, size, size);

    // Example: Apply gradient based on some condition (e.g., moon phase)
    const phase = 0.25; // Replace with your actual phase calculation
    const category = 0; // Replace with your actual category logic

    if (category === 0) {
        if (phase >= 0.22 && phase < 0.28) {
            // First quarter moon (half moon)
            // Set background to a radial gradient
            const centerX = size / 2;
            const centerY = size / 2;
            const radius = size / 2;
            const gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, radius);
            gradient.addColorStop(0, 'red');
            gradient.addColorStop(0.4, 'yellow');
            gradient.addColorStop(0.7, 'green');
            gradient.addColorStop(1, 'blue');

            // Log gradient information
            console.log("Gradient:", gradient);
            console.log("Color Stops:");
            console.log("  Stop 0: red at 0");
            console.log("  Stop 1: yellow at 0.4");
            console.log("  Stop 2: green at 0.7");
            console.log("  Stop 3: blue at 1");

            // Fill the canvas with the gradient
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, size, size);

            // Stroke a rectangle around the canvas to visualize the gradient
            ctx.strokeStyle = 'black';
            ctx.lineWidth = 2;
            ctx.strokeRect(0, 0, size, size);
        } else if (phase >= 0.72 && phase < 0.78) {
            // Last quarter moon (half moon)
            // Set background to a conic gradient
            const centerX = size / 2;
            const centerY = size / 2;
            const gradient = ctx.createConicGradient(0, centerX, centerY);
            gradient.addColorStop(0, 'red');
            gradient.addColorStop(0.4, 'yellow');
            gradient.addColorStop(0.7, 'green');
            gradient.addColorStop(1, 'blue');

            // Log gradient information
            console.log("Gradient:", gradient);
            console.log("Color Stops:");
            console.log("  Stop 0: red at 0");
            console.log("  Stop 1: yellow at 0.4");
            console.log("  Stop 2: green at 0.7");
            console.log("  Stop 3: blue at 1");

            // Fill the canvas with the gradient
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, size, size);

            // Stroke a rectangle around the canvas to visualize the gradient
            ctx.strokeStyle = 'black';
            ctx.lineWidth = 2;
            ctx.strokeRect(0, 0, size, size);
        } else {
            const random = Math.random();
            if (random < 0.7) {
                // Draw entire canvas in a random color from backgroundColors array
                const backgroundColors = ['#FFDE00', '#FF6347', '#FF4040', '#3CB371', '#1E90FF', '#C71585'];
                const randomColor = backgroundColors[Math.floor(Math.random() * backgroundColors.length)];
                ctx.fillStyle = randomColor;
                ctx.fillRect(0, 0, size, size);
            } else {
                // Put a background trait based on randomIndex in the front of the selectedTraits array
                const traitsByCategory = { 0: ['trait1', 'trait2', 'trait3'] }; // Replace with actual traits
                const selectedTraits = [];
                const randomIndex = Math.floor(Math.random() * traitsByCategory[0].length);
                const selectedTrait = traitsByCategory[0][randomIndex];
                selectedTraits.unshift(selectedTrait);
            }
        }
    }

    // Continue with the rest of your drawing logic...
    // Draw the selected traits on the canvas
    for (const trait of selectedTraits) {
        const traitData = traitsCoordinates.find(t => t.trait === trait);
        if (traitData) {
            console.log(`Drawing trait: ${trait}`);
            for (const color in traitData.colors) {
                ctx.fillStyle = color;
                for (const coordinate of traitData.colors[color]) {
                    ctx.fillRect(coordinate[0], coordinate[1], 1, 1); // Assuming each pixel is 1x1
                }
            }
        } else {
            console.log(`No data found for trait: ${trait}`);
        }
    }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('myCanvas');
    const traitsCoordinates = [
        { trait: 'trait1', colors: { 'red': [[10, 10], [20, 20]] } },
        { trait: 'trait2', colors: { 'green': [[30, 30], [40, 40]] } },
        { trait: 'trait3', colors: { 'blue': [[50, 50], [60, 60]] } }
    ];
    drawImage(canvas, traitsCoordinates);
});