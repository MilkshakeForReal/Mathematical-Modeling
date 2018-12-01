function dispath(R, i, j)
k = 1;
m = i;
n = j;
path(1) = j;
while(R(m, n)~= i)
    k = k +1;
    path(k) = R(m,n);
    n = int16(R(m,n));
end
disp(i)
for k = size(path,2):-1:1
    disp(path(k))
end