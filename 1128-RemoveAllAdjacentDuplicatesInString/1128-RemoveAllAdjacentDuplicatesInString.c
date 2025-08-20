// Last updated: 8/20/2025, 5:42:47 PM
char* removeDuplicates(char* s) {
    //Dynamic array
    char *st = malloc(strlen(s) + 1);
    int top=-1;
    st[++top] = s[0];
    for(int i=1;i< strlen(s);i++)
    {
         if(top!=-1 && st[top] == s[i])
         {
            top--;
         }
         else
         {
            st[++top] = s[i];
         }
    }
    st[++top] ='\0';
    return st;
}