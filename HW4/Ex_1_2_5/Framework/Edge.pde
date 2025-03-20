class Edge {
  Node from; 
  Node to; 
  float minutes;
  String col; // Field to store the edge color
  
  Integrator saturation;
  Integrator brightness;
  
  // Constructor with four parameters including color
  Edge(Node from, Node to, float minutes, String col) {
    this.from = from; 
    this.to = to; 
    this.minutes = minutes;
    this.col = col; // Store the color string
    
    saturation = new Integrator(1, 0.1, 0.1);
    brightness = new Integrator(1, 0.1, 0.1);
  }
  
  // Returns the source node of this edge
  Node getFromNode() {
    return from;
  }
  
  // Returns the destination node of this edge
  Node getToNode() {
    return to;
  }
  
  // Returns the travel time in minutes for this edge
  float getMinutes() {
    return minutes;
  }
  
  // Draws the edge with appropriate color and thickness
  void draw() {
    // Convert color string to lowercase for case-insensitive comparison
    String colLower = col.toLowerCase();
    
    colorMode(HSB, 360, 100, 100);
    float hue = 0;
    
    // Set edge color based on the first letter of the color string
    if (colLower.charAt(0) == 'r') {
      hue = 0; // Red color for Red Line
    } else if (colLower.charAt(0) == 'g') {
      hue = 120; // Green color for Green Line
    } else if (colLower.charAt(0) == 'b') {
      hue = 240; // Blue color for Blue Line
    } else if (colLower.charAt(0) == 'o') {
      hue = 30; // Orange color for Orange Line
    } else {
      hue = 0;
    }
    
    saturation.update();
    brightness.update();
    
    if (saturation.value == 0 && brightness.value == 0.8) {
      stroke(100); // Gray color for non-active edges
    } else {
      stroke(hue, saturation.value * 100, brightness.value * 100);
    }
    
    strokeWeight(2); // Increase stroke weight for better visibility
    line(from.x, from.y, to.x, to.y); // Draw the line between nodes
    
    colorMode(RGB, 255);
  }
}
