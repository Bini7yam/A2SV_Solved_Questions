/**
 * @param {number[]} height
 * @return {number}
 */
/*var maxArea = function(height) {
    
};*/
function maxArea(height){

let k=height.length,a=[...height],s=0,c
  for(j=k-1;a.length;j--){
   if(a[0]<=a[j]){
  c=j*(a[0]>a[j]?a[j]:a[0]);c>s?s=c:0;a.shift();j=a.length 
}}
a=[...height].reverse()
  for(j=k-1;a.length;j--){
   if(a[0]<=a[j]){
  c=j*(a[0]>a[j]?a[j]:a[0]);c>s?s=c:0;a.shift();j=a.length 
}    
  }
  return s
    }








    

    

    


     
      
   
     
    
    
   
  
  
