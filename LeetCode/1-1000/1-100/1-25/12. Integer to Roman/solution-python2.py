class Solution:
    # Copy / paste from the "fastest" solution on LeetCode.  This is almost
    # malicious compliance levels of ridiculous as it breaks for numbers
    # larger than 3999 (the exact max of the constraints) and doesn't lend
    # itself to well to scaling past that.  Also, once submitted, it was only
    # slightly faster/more memory efficient than my original solution.
    def intToRoman(self, num: int) -> str:
        m=["","M","MM","MMM"]
        c=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        x=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        i=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        
        th=m[num//1000]
        hu=c[(num%1000)//100]
        te=x[(num%100)//10]
        o=i[num%10]
        
        return(th+hu+te+o)
        

