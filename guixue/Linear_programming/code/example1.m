%返回的最优解x是列向量
C = [-2, -3, 5];
A = [-2, 5, 1; 1, 3, 1];
b = [-10; 12];
Aeq = ones(1,3);
beq = 7;
lb = zeros(3,1); %下界是列向量
[x, fval] = linprog(C, A, b, Aeq, beq, lb);
%注意得到的是最小的-z
