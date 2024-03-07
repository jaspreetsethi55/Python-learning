#!/user/bin/python3.4

name = 'Jaspreet' ##Global Variable
age = 28 ##Global variable

print("Global:{} {}".format(name,age)) ##Getting Global variable
#Global:Jaspreet 28


##Local variable only exists up to the time functions are called i.e. their live-life is the only time while functions are getting executed
def student(name,age): ##Local variable
    name = 'Jaspreet Sethi'
    print("Local:{} {}".format(name,age))  ##Getting Local variable  ##output: Local:Jaspreet Sethi 28

    def same_student(iname,iage): ##iname,iage are local to this function
        print("Enclosed:{} {}".format(name,age)) ##Getting Enclosed(from above function) ##output: Enclosed:Jaspreet Sethi 28
        print("Local to this(inner) function:{} {}".format(iname,iage)) ##Local to inner function ##output: Enclosed:Jaspreet Singh Sethi 28
        print("Built In(len):{}".format(len(name))) ##Getting built-in variable ####output: Built In(len):14

    return same_student

student_1 = student(name,age)
student_1('Jaspreet Singh Sethi',age)

