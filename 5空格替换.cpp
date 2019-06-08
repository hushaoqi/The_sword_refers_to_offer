#include <iostream>
#include <String.h>
using namespace std;

class Solution {
public:
	void replaceSpace(char *str,int length) {
		int spaceNum=0;
         // 计算原字符串的长度
        for(int i=0;i<length;i++)
        {
            if(str[i]==' ')
                spaceNum++;
             
        }    
        //得到空格替换后的字符串长度
        int newIndex=length+2*spaceNum;
        char *index=str+length;
        //从后往前替换空格
        while(index>=str)
        {
            if(*index==' ')
            {
                str[newIndex--]='0';
                str[newIndex--]='2';
                str[newIndex--]='%';
            }
            else{
                str[newIndex--]=*index;
            }
            index--;
        }
	}
	
	
};
int main(){
   
 		char s[] = "we are happy";
		int len = strlen(s);
		cout<<len<<endl;
	    Solution Solu;
	    Solu.replaceSpace(s, len);
		cout<<s<<endl;
   		return 0;
	}
