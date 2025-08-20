// Last updated: 8/20/2025, 5:44:24 PM
bool isValid(char* s)
{
    int len=strlen(s);
    char st[len];
    int top =-1;
    for(int i=0;i<len;i++)
    {
        if(s[i]=='('||s[i]=='{'||s[i]=='['){
               st[++top]=s[i];
        }
        else
        {
             if(top==-1||(s[i]==')'&&st[top]!='(')||(s[i]==']'&&st[top]!='[')||(s[i]=='}'&&st[top]!='{'))
             return false;
             else
             top--;
        }
    }
    if(top==-1)
    return true;
    else
    return false;
}