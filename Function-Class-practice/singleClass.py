class accessFiles():
    def Subfields():
        print("Sub-fields in AI are:")
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in list:
            print(temp)
            
    def OddEven():
        num=int(input("Enter a Number: "))
        if(num%2)==0:
            print(num,"is Even number")
            msg="is Even number"
        else:
            print(num,"is Odd number")
            msg="is Odd number"
            return msg
        
    def Eligible():
        gen=input("Your Gender: ")
        age=int(input("Your Age: "))
        if(age<=21):
            print("Not Eligible")
            cat="Not Eligible"
        else:
            print("Eligible")
            cat="Eligible"
            return cat
        
    def percentage():
        sub1=int(input("Subject1: "))
        sub2=int(input("Subject2: "))
        sub3=int(input("Subject3: "))
        sub4=int(input("Subject4: "))
        sub5=int(input("Subject5: "))
        total=sub1+sub2+sub3+sub4+sub5
        print("total: ",sub1+sub2+sub3+sub4+sub5)
        percent=total/500*100
        print("percentage: ",percent)
        
    def triangle():
        h=int(input("Height: "))
        b=int(input("Breadth: "))
        Area_formula=h*b/2
        print("Area formula",h*b/2)
        Area_of_Triangle= Area_formula
        print("Area of Triangle",h*b/2)
        h1=int(input("Height1: "))
        h2=int(input("Height2: "))
        b1=int(input("Breadth: "))
        perimeter_formula=h1+h2+b1
        print("perimeter formula: ",h1+h2+b1)
        print("perimeter of triangle: ",perimeter_formula)