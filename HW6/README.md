first step: setting python's API
![Screenshot (95).png](Screenshot%20%2895%29.png)
Second step: search for (couple,coupleby,create,createby,declare and declarein) reference kinds.
couple,coupleby:
Indicates a coupling link as counted in the OO coupling metrics. A link is created from a class to any external class (a class that is not in the extends/implements hierarchy) that is referenced.
public class c1 {
 ...
}

public class c2 {
 cl obj;
}
Reference kind string	Entity performing references	Entity being referenced
Java Couple	                      c2	                           c1
Java Coupleby	                  c1	                           c2
and now using understand for the java codes placced in java8 project in this repo:
![Screenshot (107).png](Screenshot%20%28107%29.png)
create,createby:
Indicates that an instance of a class is created (new operator) in a scope.
class c1 {
 ...
}

class c2 {
 c1 a = new c1();
}
Reference kind string	Entity performing references	Entity being referenced
Java Create	                        c2	                           c1
Java Createby	                    c1	                           c2
and now using understand  for the java codes placced in java8 project in this repo:
![Screenshot (108).png](Screenshot%20%28108%29.png)
declare,declarein:
Indicates that a package is declared in a file or in a (parent) package.
package technology.tabula.debug;

import java.awt.BasicStroke;
import java.awt.Color;

class Debug {
...
}

Reference kind string	Entity performing references	            Entity being referenced
Java Declare	             Debug.java	                            technology, technology.tabula.debug
Java Declarein	        technology, technology.tabula.debug	        Debug.java

and now using understand  for the java codes placced in java8 project in this repo:
![Screenshot (109).png](Screenshot%20%28109%29.png)
and when i wanted to try in openunderstand i got this error below:
![Screenshot (110).png](Screenshot%20%28110%29.png)