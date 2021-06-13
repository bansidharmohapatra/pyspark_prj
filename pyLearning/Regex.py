import re


def main():
    """


    animals= " Cat Rat cat rat Elephat, deer"
    matched_animals= re.findall("[crCR]at", animals )
    print(matched_animals)
    #replace the matched object
    regex=re.compile("[cr]at")
    x=regex.sub("matched",animals)
    print(x)
    :return:
    """

    email= "abc@gmail.com xyxakdkd@hotmail.in ieueueu@yahoo.org ramarek@gmail.com"
    regex=re.compile("\w*@\w*\.\w{2,3}")
    x=regex.findall(email)
    print(x)


if __name__ =="__main__":
    main()