//Digit DP
//Given an integer N, count the total number of digit 1 appearing in all non-negative integers 
//less than or equal to N.
//Ex: n = 13
//    Output : 6

// Based on whether the position is tight bound or not we have choices for each position

// Count the total number of digit '1' appending in all positive no's that are
// less than or equal to given very big number N.
// e.g if nums="15"
// [1,10,11,12,13,14,15] => total number of ones = 1+1+2+1+1+1+1=8(ans)

#include<bits/stdc++.h>
using namespace std;

int dp[10][2][10];

class Solution {
public:
    int countDigitOne(int nums) {
        
        memset(dp,-1,sizeof(dp));

   int i=0,tight=1,countOnes=0;  

   // for i=0, tight=1 becouse we cannot put all digits to this position
        
        string str=to_string(nums);
        
   return find(i,tight,countOnes,str);

        
    }
    
int find(int i,int tight,int countOnes,string nums){
    
  if(i==nums.size())
  return countOnes;

  if(dp[i][tight][countOnes]!=-1)
  return dp[i][tight][countOnes];

  int ub;   // upperBound digit of position i

  if(tight==1)
  ub=nums[i]-'0';
  else
  ub=9;

  int ans=0;

  for(int d=0;d<=ub;d++){

   ans=ans+find(i+1,tight && (d==ub),countOnes + (d==1),nums);
      
  }

  return dp[i][tight][countOnes]=ans;
 }
   int brute_force(int nums){
       int ans=0;
       for(int i=1;i<=nums;++i){
           string str=to_string(i);
           ans+=count(str.begin(),str.end(),'1');           
       }
       return ans;       
       
   }

};
