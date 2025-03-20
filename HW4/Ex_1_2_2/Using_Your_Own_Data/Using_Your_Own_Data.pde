PImage mapImage;
Table stationTable; 

int currentRow = -1; 
PrintWriter writer; 

// Zoom and pan variables
float scale = 1.0;
float translateX = 0;
float translateY = 0;
float scaleStep = 0.1;
float panStep = 10;

void setup() {
  size(640, 400);
  mapImage = loadImage("mbta-map.gif");
  // Load stations.csv from the TheTDataCollection directory
  stationTable = new Table("../../TheTDataCollection/stations.csv");
  writer = createWriter("locations.csv");
  cursor(CROSS); 
  println("Instructions:");
  println("- Mouse wheel or +/- keys: Zoom map");
  println("- Arrow keys: Pan map");
  println("- Spacebar: Reset zoom and pan");
  println("- Mouse click: Mark current station location");
  println("- ESC key: Exit program");
  println("\nClick the mouse to begin marking station locations.");
}

void draw() {
  background(200);
  
  // Apply zoom and pan
  pushMatrix();
  translate(translateX, translateY);
  scale(scale);
  
  // Draw the map
  image(mapImage, 0, 0); 
  
  // Draw marked stations (optional)
  if (currentRow > 0) {
    stroke(255, 0, 0);
    strokeWeight(1);
    noFill();
    for (int i = 0; i < currentRow; i++) {
      // Add code here to display marked stations
    }
  }
  
  popMatrix();
  
  // Display current zoom and pan information
  fill(0);
  textAlign(LEFT, TOP);
  text("Zoom: " + nf(scale, 1, 2) + "x  |  Pan: (" + int(translateX) + ", " + int(translateY) + ")", 10, height - 20);
  
  // Display current station name
  if (currentRow != -1 && currentRow < stationTable.getRowCount()) {
    fill(255);
    rect(10, 10, 300, 30);
    fill(0);
    text("Click to mark location: " + stationTable.getString(currentRow, 0) + " (" + (currentRow+1) + "/" + stationTable.getRowCount() + ")", 15, 30);
  }
}

void mousePressed() {
  if (currentRow != -1) {
    String stationName = stationTable.getString(currentRow, 0);
    
    // Calculate actual coordinates (considering zoom and pan)
    float actualX = (mouseX - translateX) / scale;
    float actualY = (mouseY - translateY) / scale;
    
    // Save to CSV file with comma separator
    writer.println(stationName + "," + int(actualX) + "," + int(actualY));
    println("Marked: " + stationName + " at location (" + int(actualX) + ", " + int(actualY) + ")");
  }
  
  currentRow++;
  if (currentRow == stationTable.getRowCount()) {
    writer.flush();
    writer.close(); 
    println("All stations have been processed. Locations saved to locations.csv");
    exit(); 
  } else {
    String name = stationTable.getString(currentRow, 0);
    println("Choose location for " + name + "."); 
  } 
}

void mouseWheel(MouseEvent event) {
  // Zoom using mouse wheel
  float e = event.getCount();
  scale -= e * scaleStep;
  scale = constrain(scale, 0.5, 5.0);
}

void keyPressed() {
  // Control zoom and pan using keyboard
  if (key == '+' || key == '=') {
    scale += scaleStep;
    scale = constrain(scale, 0.5, 5.0);
  } else if (key == '-' || key == '_') {
    scale -= scaleStep;
    scale = constrain(scale, 0.5, 5.0);
  } else if (key == ' ') {
    // Reset zoom and pan with spacebar
    scale = 1.0;
    translateX = 0;
    translateY = 0;
  }
  
  // Control pan using arrow keys
  if (keyCode == UP) {
    translateY += panStep;
  } else if (keyCode == DOWN) {
    translateY -= panStep;
  } else if (keyCode == LEFT) {
    translateX += panStep;
  } else if (keyCode == RIGHT) {
    translateX -= panStep;
  }
}
