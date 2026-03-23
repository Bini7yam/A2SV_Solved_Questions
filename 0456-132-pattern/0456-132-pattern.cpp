


class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        vector<int>&a = nums;
        int n = (int)a.size();
        vector<int> mxs;
        vector<int> mns;
       
        for(int i=0;i<n;++i){
            if(mns.empty()||a[i]<a[mns.back()])mns.push_back(i);
            while(!mxs.empty() && a[mxs.back()] <= a[i])mxs.pop_back();
            int r = mxs.empty()?-1:mxs.back();
            int ll=0,rr=(int)mns.size()-1,l=i;
            while(ll<=rr){
                int m = (ll+rr)/2;
                if(a[mns[m]] < a[i])l=mns[m],rr=m-1;
                else ll = m+1;
            }
            if(l <r)return 1;
            mxs.push_back(i);
        }
        return 0;
    }
};