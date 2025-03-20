class Edge {
  Node from; 
  Node to; 
  float minutes;
  String col; // Field to store the edge color
  
  // Constructor with four parameters including color
  Edge(Node from, Node to, float minutes, String col) {
    this.from = from; 
    this.to = to; 
    this.minutes = minutes;
    this.col = col; // Store the color string
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
    // Set edge color based on the first letter of the color string
    if (col.charAt(0) == 'r') {
      stroke(230, 19, 16); // Red color for Red Line
    } else if (col.charAt(0) == 'g') {
      stroke(1, 104, 66); // Green color for Green Line
    } else if (col.charAt(0) == 'b') {
      stroke(0, 48, 140); // Blue color for Blue Line
    } else if (col.charAt(0) == 'o') {
      stroke(255, 131, 5); // Orange color for Orange Line
    }
    
    strokeWeight(2); // Increase stroke weight by one (from 1 to 2)
    line(from.x, from.y, to.x, to.y); // Draw the line between nodes
  }
}
