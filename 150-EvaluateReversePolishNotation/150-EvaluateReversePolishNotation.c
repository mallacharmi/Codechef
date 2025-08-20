// Last updated: 8/20/2025, 5:43:41 PM
int evalRPN(char** tokens, int tokensSize) {
    int st[10001];
    int top=-1;
    for(int i=0;i<tokensSize;i++)
    {
        //tokens[i]-->current string "-13" //strlen()
        //tokens[i][0]--->+,-,*,/---->operator
        char ch = tokens[i][0];
        int size = strlen(tokens[i]);//length of current string
        //operator (symbol)case
        if(size==1 && (ch=='+' || ch=='-'|| ch=='*' || ch=='/')){
            int op2 = st[top];
            top--;
            int op1= st[top];
            top--;
            int res;
            if(ch=='+') res =op1+op2;
            else if(ch=='-')res =op1-op2;
            else if(ch=='*')res=op1*op2;
            else if(ch=='/')res=op1/op2;
            //push the res back in the stack
            st[++top]=res;
        }else{//operand (number )case
           //atoi()
           st[++top] = atoi(tokens[i]);
        } 
    }
    return st[top];
}