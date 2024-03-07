l = [ 1,5,7,9,3,10,11,15]
i=0
while i < len(l):
    print(i)
    if(l[i]==7):
        i = 6
    else:
        i=i+1

l1=[9,3,10]
if l1 in l:
    print("Found")

a=1
if a==1:
    print("One")
    a=a+1
elif a==i:
    print("Unknown")


s='abcdefghhgfedecba'
def isValid(s):
    d = {}
    for x in s:
        d[x] = d.get(x,0)+1

    print(d)           
    uniq = set(d.values())
    print(uniq)
    if len(uniq) == 1 :
        return "YES"
    elif len(uniq) == 2:
        d_sort = sorted(d.items(),key=lambda x:x[1])
        print(d_sort)
        (min_s,min_count),(max_s,max_count)=d_sort[0],d_sort[-1]
        
        print(d_sort[len(d_sort)-2])
        if (d_sort[len(d_sort)-2][1] == min_count and (max_count-min_count) <= 1) or (d_sort[0][1] == min_count and d_sort[1][1] == max_count):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

print(isValid('aabbc'))
#print(isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))
