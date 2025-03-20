import processing.pdf.*;

// nodes
int nodeCount; 
Node[] nodes = new Node[200]; // Increased array size for more nodes
HashMap nodeTable = new HashMap();

// selection
Node selection;

// record
boolean record; 

// edges
int edgeCount; 
Edge[] edges = new Edge[1000]; // Increased array size for more edges

// font
PFont font;

// tables for data
Table locationsTable;
Table connectionsTable;

// hover node
Node hoverNode = null;

void setup() {
  size(800, 600); // 增加画布大小，以便更好地显示网络
  font = createFont("SansSerif", 12); // 增加字体大小，使文本更易读
  loadData();
}

void loadData() {
  // Load locations.csv and connections.csv
  locationsTable = new Table("../../Ex_1_2_2/Using_Your_Own_Data/locations.csv");
  connectionsTable = new Table("../../TheTDataCollection/connections.csv");
  
  // First load all nodes with their locations
  for (int i = 0; i < locationsTable.getRowCount(); i++) {
    String stationName = locationsTable.getString(i, 0);
    float x = locationsTable.getFloat(i, 1);
    float y = locationsTable.getFloat(i, 2);
    
    // Create node with coordinates from locations.csv
    addNode(stationName, x, y);
  }
  
  // Then load all connections
  for (int i = 0; i < connectionsTable.getRowCount(); i++) {
    String fromStation = connectionsTable.getString(i, 0);
    String toStation = connectionsTable.getString(i, 1);
    String lineColor = connectionsTable.getString(i, 2);
    float minutes = connectionsTable.getFloat(i, 3);
    
    // Add edge with data from connections.csv
    addEdge(fromStation, toStation, minutes, lineColor);
  }
}

void addEdge(String fromLabel, String toLabel, float minutes, String col) {
  // find nodes
  Node from = findNode(fromLabel);
  Node to = findNode(toLabel);
  
  // old edge?
  for (int i = 0; i < edgeCount; i++) {
    if (edges[i].from == from && edges[i].to == to) {
      return; 
    }
  }
  
  // add edge with color parameter
  Edge e = new Edge(from, to, minutes, col);
  if (edgeCount == edges.length) {
    edges = (Edge[]) expand(edges);
  }
  edges[edgeCount++] = e; 
}

Node findNode(String label) {
  Node n = (Node) nodeTable.get(label);
  if (n == null) {
    return addNode(label, 0, 0); // Default coordinates if not found
  }
  return n; 
}

Node addNode(String label) {
  return addNode(label, random(50, width-50), random(50, height-50));
}

Node addNode(String label, float x, float y) {
  Node n = new Node(label, x, y, nodeCount);
  if (nodeCount == nodes.length) {
    nodes = (Node[]) expand(nodes);
  }
  nodeTable.put(label, n);
  nodes[nodeCount++] = n;
  return n; 
}

void draw() {
  if (record) {
    beginRecord(PDF, "output.pdf");
  }
  
  textFont(font); 
  smooth();
  
  background(255); 
  
  // draw the edges
  for (int i = 0; i < edgeCount; i++) {
    edges[i].draw();
  }
  
  // draw the nodes
  for (int i = 0; i < nodeCount; i++) {
    nodes[i].draw();
  }
  
  // Check for hover
  hoverNode = null;
  float closestDist = 10; // Hover detection radius
  for (int i = 0; i < nodeCount; i++) {
    float d = dist(mouseX, mouseY, nodes[i].x, nodes[i].y);
    if (d < closestDist) {
      hoverNode = nodes[i];
      closestDist = d;
    }
  }
  
  // Display station name in upper right corner when hovering
  if (hoverNode != null) {
    fill(0);
    textAlign(RIGHT, TOP);
    text(hoverNode.label, width - 10, 10);
  }
  
  if (record) {
    endRecord();
    record = false;
  }
}

void mousePressed() {
  if (mouseButton == LEFT) {
    float closest = 5;
    for (int i = 0; i < nodeCount; i++) {
      Node n = nodes[i];
      float d = dist(mouseX, mouseY, n.x, n.y);
      if (d < closest) {
        selection = n;
        closest = d;
      }
    }
  }
}

void mouseDragged() {
  if (selection != null) {
    selection.x = mouseX;
    selection.y = mouseY;
  }
}

void mouseReleased() {
  selection = null;
}

void keyPressed() {
  if (key == 'p') {
    record = true;
  }
}
