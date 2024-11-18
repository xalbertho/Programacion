Vector v = new Vector(2, 5);
  
    // Creamos el vector en (2, 5)
  Vector v = new Vector(2, 5);
  
  // Mostramos en consola los valores (x, y)
  v.Print();
  
  // Resultado en consola
  // [ 2, 5 ] 
  
    // Creamos el vector en (2, 5)
  Vector v = new Vector(2, 5);
  
  // Obteniendo los valores (x, y) como un arreglo
  float[] valores = v.GetValues();
  
    // Valores (x, y) a asignar
  float[] valores = new float[]{ 1, 2 };
  
  // Creando el vector en (2, 5)
  Vector v = new Vector(2, 5);
  
  // Actualizando los valores (x, y) del vector
  v.SetValues(valores);
  
  // Mostrando los valores (x, y) del vector
  v.Print();
  
  // Resultado en consola
  // [ 1, 2 ]
  
    // Creamos el poligono
  Polygon p = new Polygon();
  
  // Añadimos sus vertices
  p.Add(20, 20);
  p.Add(60, 70);
  p.Add(100, 20);
  
    // Creamos el poligono
  Polygon p = new Polygon();
  
  // Añadimos sus vertices
  p.Add(20, 20);
  p.Add(60, 80);
  p.Add(100, 20);
  
  // Mostramos sus vertices en consola
  p.Print();
  
  // Resultado en consola
  // [ 20, 20 ]
  // [ 60, 80 ]
  // [ 100, 20 ]
  
    // Creamos el poligono
  Polygon p = new Polygon();
  
  // Añadimos sus vertices
  p.Add(20, 20);
  p.Add(60, 80);
  p.Add(100, 20);
  
  // Eliminamos el ultimo vertice del poligono
  p.Remove();
  
  // Mostramos sus vertices en consola
  p.Print();
  
  // Resultado en consola
  // [ 20, 20 ]
  // [ 60, 80 ]
    // Creamos el poligono
  Polygon p = new Polygon();
  
  // Añadimos sus vertices
  p.Add(20, 20);
  p.Add(60, 80);
  p.Add(100, 20);
  
  // Dibujamos el poligono en el picture box de nuestro WindowsForm
  p.Draw(picturebox);