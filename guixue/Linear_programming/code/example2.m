%以模型一为例子
%因为可以不投，可增加一项0表示不投
a=0; %a为风险率上限，初始不冒任何风险
M = 1;
r = [0 28 21 23 25] * 0.01; %收益率
p = [0 1 2 4.5 6] * 0.01;  %费率
q = [0 2.5 1.5 5.5 2.6] * 0.01;   %风险率
c = p-r;  %优化目标
A = diag(q); %不等式约束矩阵
Aeq = 1+p;  %等式系数  
beq = M; %等式约束
lb = zeros(5,1); %变量下界

while(1.1-a)>1
   b = a * ones(5, 1); 
   vlb=[0,0,0,0,0];vub=[];
   [x,val]=linprog(c, A, b, Aeq, beq, vlb);
   a
   x'
   z = -val
   plot(a,z,'.'),axis([0 0.1 0 0.5])
   hold on
   a=a+0.001;
end 
xlabel('a'),ylabel('最优收益z')
