#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{   int n;
    scanf("%d", &n);
    int i,j,start,end,size;
    size=2 * n - 1;
    start=0;
    end=size-1;
    int arr[size][size];
    while(n!=0)
    {
        for(i=start;i<=end;i++)
        {
            for(j=start;j<=end;j++)
            {
                if(i==start||i==end||j==start||j==end)
                arr[i][j]=n;
            }
           
        }
        start++;
        end--;
        n--;
    }   
for(i=0;i<size;i++)
{printf("\n");
for(j=0;j<size;j++)
{printf("%d ",arr[i][j]);
}
}
return 0;
}