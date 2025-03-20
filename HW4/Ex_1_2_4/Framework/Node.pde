class Node {
  String label;
  float x, y; 
  int index;  
  
  Node(String label, float x, float y, int index) {
    this.label = label; 
    this.x = x;
    this.y = y;
    this.index = index;
  }
  
  int getIndex() {
    return index;
  }

  void draw() {
    stroke(0); 
    strokeWeight(1);
    
    // Make nodes more visible
    fill(255);  
    ellipse(x, y, 10, 10); // Increased size for better visibility
    
    // Highlight node if it's being hovered over
    if (this == hoverNode) {
      noFill();
      stroke(255, 0, 0);
      strokeWeight(2);
      ellipse(x, y, 15, 15); // Larger highlight circle
    }
  }
}
