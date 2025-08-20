// Last updated: 8/20/2025, 5:42:48 PM
int calPoints(char** operations, int operationsSize) {
    int st[1001];
    int top =-1;
    for(int i = 0 ;i < operationsSize ;i++)
    {
       char ch = operations[i][0];
       if(ch != 'C' && ch!='D'&& ch!='+')
       {
        st[++top] = atoi(operations[i]);
       }
       else if(ch == 'C')
       {
         top--;
       }
       else if(ch == 'D')
       {
           int new = st[top]*2;
           st[++top]=new;
       }
       else
       {
        if(top > 0)
        {
            int new = st[top] + st[top -1];
            st[++top] = new;
        }
       }
    }
    int sum = 0;
    for(int i=top; i>=0; i--) sum+= st[i];
    return sum;
}