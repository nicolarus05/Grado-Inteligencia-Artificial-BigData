%1. Crea matriz de 3x3 con randon (aleatorio) 
A = randi(3,3)

%2. Crea una matriz y encuentra su traspuesta 
B = [1,2,3; 4,5,6; 7,8,9];

BT=B';

disp('Matriz original B:')
disp(B)

disp('Matriz traspuesta BT:')
disp(BT)

%3. Calcula la suma de cada columna - X 
S = sum(A)

%4. Haz la raíz cuadrada de la siguiente matriz: A = [1 4 9, 16 25 36] -X 
a = [1 4 9, 16 25 36]

R = sqrt(a)