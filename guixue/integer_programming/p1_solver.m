rng('shuffle');
p=0;
tic
for i=1:10^6
    x=99*rand(5,1);
    x1=floor(x);x2=ceil(x);
    [f,g] = mengte(x1);
    if sum(g<=0)==4   %满足约束
        if f >= p      %得到的更大
            x0=x1;p=f;
        end
    end
    [f,g]=mengte(x2);
    if sum(g<=0)==4
        if p<=f
            x0=x2;p=f;
        end
    end
end
x0,p
toc
    