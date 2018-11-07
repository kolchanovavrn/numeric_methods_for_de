Initialization:
FLASK
  - creation an object of class Flask, calling it’s functions app.route 
    -  function following it with the <path> to which the request will come. The request for the address “/” will be set by the function that comes after @ app.route (“/“)
    - result() function call 
    - here we rendering template or getting the information from it. In case, 
      - if the main method - “get” - sending the HTML form and allowing user to fill it.
      - else - the main parameter - “post” means that we should take given by user values and make an object of class GraphBuilder 
- Creation an object of class GraphBuilder 
- For building graph of function values we need lists of points == > 
  - creation an object of class Methods and filling the fields of GraphBuilder by Methods functions, that returns all necessary values
- For building graphs of Local Errors and Maximum Error we also need lists of points ⇒
  - creation an object of class Errors and filling the fields of GraphBuilder by local_error() and max_error() functions, that returns all necessary values.
  - local_error() - shows the difference of values given by Numeric Method and Exact solution. 
  - max_error() - shows the influence of step ( amount of parts, that X axis is divided on) on a function value, given by Numeric methods, by getting the maximum difference.
- Graphs are builded in GraphBuilder.build() and saved in directory /static as graphs.png
- We sending back the information given by user and also A FLAG SHOW_IMAGE, which plays important role in HTML
- HTML page contains if/else , where checks, should the picture be showed. If yes - attaches an image by its address in project
